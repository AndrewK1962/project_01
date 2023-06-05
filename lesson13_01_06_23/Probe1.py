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