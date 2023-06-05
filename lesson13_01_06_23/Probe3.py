# Вложенные в сообщения кнопки
import telebot
from telebot import types

bot = telebot.TeleBot('6283878842:AAEnaVbLfEyuJwvb34o4dQ3sJ_kQZWMjWoE')

@bot.message_handler(commands=['test'])
def test(message):
  markup = types.InlineKeyboardMarkup()
  kn1 = types.InlineKeyboardButton("Кнопка 1",callback_data='test1')
  markup.row(kn1)
  kn2 = types.InlineKeyboardButton("Кнопка 2",callback_data='test2')
  kn3 = types.InlineKeyboardButton("Кнопка 3",url = 'https://ya.ru/')
  markup.row(kn2,kn3)
  bot.send_message(message.chat.id, "Привет", reply_markup=markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
  if callback.data == "test1":
    bot.send_message(callback.message.chat.id, "Кнопка 1 работает")

bot.polling(none_stop=True)
