import telebot

bot = telebot.TeleBot('6283878842:AAEnaVbLfEyuJwvb34o4dQ3sJ_kQZWMjWoE')

@bot.message_handler(content_types=['text', 'document', 'photo'])
def define(message):
  if message.text:
    bot.send_message(message.chat.id, "Это текст!!!")
  elif message.photo:
    bot.send_message(message.chat.id, "Это фото!!!")
  elif message.document:
    bot.send_message(message.chat.id, "Это документ!!!")

bot.polling(none_stop=True)
