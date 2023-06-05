# Вложенные в чат кнопки
import telebot
from telebot import types

bot = telebot.TeleBot('6283878842:AAEnaVbLfEyuJwvb34o4dQ3sJ_kQZWMjWoE')
@bot.message_handler(commands=['test'])
def test(message):
  markup = types.ReplyKeyboardMarkup()
  kn1 = types.KeyboardButton("Кнопка 1")
  kn2 = types.KeyboardButton("Кнопка 2")
  markup.row(kn1,kn2)
  kn3 = types.KeyboardButton("Кнопка 3")
  kn4 = types.KeyboardButton("Кнопка 4")
  markup.row(kn3,kn4)
  bot.send_message(message.chat.id, "Привет", reply_markup=markup)
  bot.register_next_step_handler(message,reply)

def reply(message):
  if message.text == "Кнопка 2":
    bot.send_message(message.chat.id, "Кнопка 2 работает")
  elif message.text == "Кнопка 3":
    doc = open("telebot.pdf",'rb')
    bot.send_document(message.chat.id, doc)

bot.polling(none_stop=True)