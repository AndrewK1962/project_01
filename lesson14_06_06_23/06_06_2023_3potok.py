

#pip install telebot

import telebot

bot = telebot.TeleBot('6283878842:AAEnaVbLfEyuJwvb34o4dQ3sJ_kQZWMjWoE')



@bot.message_handler(commands=['start', 'powel'])
def start(message):
  mes =f'Привет, {message.from_user.first_name}, {message.from_user.last_name}'
  bot.send_message(message.chat.id, mes)

@bot.message_handler(commands=['help'])
def start(message):
  bot.send_message(message.chat.id,"Список доступных команд...")

@bot.message_handler()
def get_text(message):
  bot.send_message(message.chat.id,"Извините, не понимаю вас. Вопсользуйтесь командой /help")
  print (message.text)



bot.polling(none_stop=True)

import telebot

bot = telebot.TeleBot('') # здесь должен быть токен  телебота

@bot.message_handler(content_types=['text', 'document', 'photo'])
def define(message):
  if message.text:
    bot.send_message(message.chat.id, "Это текст!!!")
  elif message.photo:
    bot.send_message(message.chat.id, "Это фото!!!")
  elif message.document:
    bot.send_message(message.chat.id, "Это документ!!!")

bot.polling(none_stop=True)

# Вложенные в сообщения кнопки
import telebot
from telebot import types

bot = telebot.TeleBot('')# здесь должен быть токен  телебота

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

# Вложенные в чат кнопки
import telebot
from telebot import types

bot = telebot.TeleBot('')# здесь должен быть токен  телебота
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