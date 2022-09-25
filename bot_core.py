import telebot
import spreadsheet
from telebot import types

token = '5692398615:AAFeVNfA4UZGbTE0-hJY9rexq2AI2DCF2Y4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Понедельник")
               , types.KeyboardButton("Вторник")
               , types.KeyboardButton("Среда")
               , types.KeyboardButton("Четверг")
               , types.KeyboardButton("Пятница")
               , types.KeyboardButton("Суббота"))
    bot.send_message(message.chat.id, "Привет✌\nЗдесь ты сможешь указать актуальное расписание!")
    bot.send_message(message.chat.id, "Выбери день, который тебя интересует 👇", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Понедельник":
        bot.send_message(message.chat.id, "https://habr.com/ru/users/lubaznatel/")
    elif message.text == 'Вторник':
        pass
    elif message.text == 'Среда':
        pass
    elif message.text == 'Четверг':
        pass
    elif message.text == 'Пятница':
        pass
    elif message.text == 'Суббота':
        pass


bot.infinity_polling()
