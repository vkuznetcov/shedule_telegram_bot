import telebot
import re
import spreadsheet
from telebot import types
from enum import Enum


class Modes(Enum):
    MOVE = 'move'
    CANCEL = 'cancel'
    NONE = 'none'


token = '5692398615:AAFeVNfA4UZGbTE0-hJY9rexq2AI2DCF2Y4'
bot = telebot.TeleBot(token)
time_pattern = re.compile('^\d{0,2}:\d{2} мск$')
entry_pattern = re.compile('^[А-я]{5,11} \d{0,2}:\d{2} мск$')
cur_weekday = None
mode = Modes.NONE


def weekdays_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Понедельник")
               , types.KeyboardButton("Вторник")
               , types.KeyboardButton("Среда")
               , types.KeyboardButton("Четверг")
               , types.KeyboardButton("Пятница")
               , types.KeyboardButton("Суббота"))
    return markup

def create_entry(message):
    markup = weekdays_markup()
    markup.add(types.KeyboardButton('Отмена'))
    bot.send_message(message.chat.id, "Выберите день для новой записи 👇", reply_markup=markup)
    print(message.chat.id)

@bot.message_handler(commands=['start'])
def start_message(message, hello_message=True):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Записаться на занятие'))
    markup.add(types.KeyboardButton('Изменить запись занятий'))
    markup.add(types.KeyboardButton('Просмотреть мои записи'))
    if hello_message:
        bot.send_message(message.chat.id, "Привет✌\nЗдесь вы сможете указать актуальное расписание!")
    bot.send_message(message.chat.id, "Выберите, что бы вы хотели сделать 👇", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    user_info = '@' + message.from_user.username \
        if message.from_user.username is not None \
        else (message.contact if message.contact is not None else message.from_user.full_name)

    if message.text == 'Записаться на занятие':
        create_entry(message)

    elif message.text == 'Изменить запись занятий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Отменить запись'))
        markup.add(types.KeyboardButton('Перенести запись'))
        markup.add(types.KeyboardButton('Отмена'))
        bot.send_message(message.chat.id, 'Выберите, что бы вы хотели сделать 👇', reply_markup=markup)

    elif message.text == 'Отменить запись':
        global mode
        mode = Modes.CANCEL
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        try:
            for entry in spreadsheet.get_entries_by_user(user_info)[0]:
                markup.add((types.KeyboardButton(entry[0] + ' ' + entry[1])))
            markup.add(types.KeyboardButton('Отмена'))
        except spreadsheet.ZeroEntries as exc:
            bot.send_message(message.chat.id, str(exc))
            start_message(message, hello_message=False)
        else:
            bot.send_message(message.chat.id, 'Выберите запись для отмены 👇', reply_markup=markup)

    elif message.text == 'Перенести запись':
        mode = Modes.MOVE
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        try:
            for entry in spreadsheet.get_entries_by_user(user_info)[0]:
                markup.add((types.KeyboardButton(entry[0] + ' ' + entry[1])))
            markup.add(types.KeyboardButton('Отмена'))
        except spreadsheet.ZeroEntries as exc:
            bot.send_message(message.chat.id, str(exc))
            start_message(message, hello_message=False)
        else:
            bot.send_message(message.chat.id, 'Выберите запись для отмены 👇', reply_markup=markup)

    elif message.text == 'Просмотреть мои записи':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for entry in spreadsheet.get_entries_by_user(user_info)[0]:
            bot.send_message(message.chat.id, entry[0] + ' ' + entry[1])
        start_message(message, hello_message=False)

    elif message.text in ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        global cur_weekday
        cur_weekday = message.text
        try:
            for time in spreadsheet.get_free_time(message.text):
                markup.add(types.KeyboardButton(time))
            markup.add(types.KeyboardButton('Отмена'))
        except spreadsheet.ZeroEntries as exc:
            bot.send_message(message.chat.id, str(exc))
            start_message(message, hello_message=False)
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, выберите удобное время 👇', reply_markup=markup)

    elif time_pattern.match(message.text):
        if cur_weekday is None:
            bot.send_message(message.chat.id, 'Перед выбором времени нужно выбрать день недели',
                             reply_markup=weekdays_markup())
            start_message(message, hello_message=False)
        try:
            spreadsheet.update_user_schedule(user_info, cur_weekday, message.text)

        except spreadsheet.OccupiedEntry as exc:
            bot.send_message(message.chat.id, str(exc))
            start_message(message, hello_message=False)
        else:
            bot.send_message(message.chat.id, 'Запись успешно выполнена!')
            print(user_info)
            bot.send_message(997567679, user_info + ' записался на ' + message.text + ' в ' + cur_weekday)
            cur_weekday = None
            start_message(message, hello_message=False)
    elif entry_pattern.match(message.text):
        if mode is Modes.CANCEL:
            day, time = tuple(message.text.split(' ', 1))
            spreadsheet.update_user_schedule(user_info, day, time, delete=True)
            bot.send_message(message.chat.id, 'Запись успешно удалена!')
            bot.send_message(997567679, user_info + ' удалил запись в ' + day + ' ' + time)
            start_message(message, hello_message=False)
        elif mode is Modes.MOVE:
            day, time = tuple(message.text.split(' ', 1))
            spreadsheet.update_user_schedule(user_info, day, time, delete=True)
            create_entry(message)
    elif message.text == 'Отмена':
        start_message(message, hello_message=False)



print('bot started')
bot.infinity_polling()
