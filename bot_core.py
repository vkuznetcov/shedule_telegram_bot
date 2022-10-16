import telebot
import re
import spreadsheet
from telebot import types

token = '5692398615:AAFeVNfA4UZGbTE0-hJY9rexq2AI2DCF2Y4'
bot = telebot.TeleBot(token)
time_pattern = re.compile('^\d{0,2}:\d{2} мск$')
cur_weekday = None


def weekdays_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Понедельник")
               , types.KeyboardButton("Вторник")
               , types.KeyboardButton("Среда")
               , types.KeyboardButton("Четверг")
               , types.KeyboardButton("Пятница")
               , types.KeyboardButton("Суббота"))
    return markup


@bot.message_handler(commands=['start'])
def start_message(message, hello_message=True):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Записаться на занятие'))
    # markup.add(types.KeyboardButton('Изменить запись занятий'))
    if hello_message:
        bot.send_message(message.chat.id, "Привет✌\nЗдесь вы сможете указать актуальное расписание!")
    bot.send_message(message.chat.id, "Выберите, что бы вы хотели сделать 👇", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Записаться на занятие':
        bot.send_message(message.chat.id, "Выберите, что бы вы хотели сделать 👇", reply_markup=weekdays_markup())
        print(message.chat.id)
    if message.text in ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        global cur_weekday
        cur_weekday = message.text
        for time in spreadsheet.get_free_time(message.text):
            markup.add(types.KeyboardButton(time))
        bot.send_message(message.chat.id, 'Пожалуйста, выберите удобное время 👇', reply_markup=markup)
    elif time_pattern.match(message.text):
        if cur_weekday is None:
            bot.send_message(message.chat.id, 'Перед выбором времени нужно выбрать день недели',
                             reply_markup=weekdays_markup())
            return
        user_info = '@' + message.from_user.username \
            if message.from_user.username is not None \
            else (message.contact if message.contact is not None else message.from_user.full_name)
        spreadsheet.update_user_schedule(user_info
                                         , cur_weekday
                                         , message.text)
        bot.send_message(message.chat.id, 'Запись успешно выполнена!')
        print(user_info)
        bot.send_message(997567679, user_info + ' записался на ' + message.text + ' в ' + cur_weekday)
        cur_weekday = None
        start_message(message, hello_message=False)


print('bot started')
bot.infinity_polling()
