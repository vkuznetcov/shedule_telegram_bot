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
def start_message(message):
    bot.send_message(message.chat.id, "Привет✌\nЗдесь ты сможешь указать актуальное расписание!")
    bot.send_message(message.chat.id, "Выбери день, который тебя интересует 👇", reply_markup=weekdays_markup())
    # print(message.chat.id, message.from_user.username)
    # print(message.from_user.first_name, message.from_user.last_name)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text in ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        global cur_weekday
        cur_weekday = message.text
        for time in spreadsheet.get_free_time(message.text):
            markup.add(types.KeyboardButton(time))
        bot.send_message(message.chat.id, 'Пожалуйста, выберите удобное время 👇', reply_markup=markup)
    elif time_pattern.match(message.text):
        spreadsheet.update_user_schedule(message.from_user.username
                                         , cur_weekday
                                         , message.text)
        bot.send_message(message.chat.id, 'Выбери день', reply_markup=weekdays_markup())

print('bot started')
bot.infinity_polling()
