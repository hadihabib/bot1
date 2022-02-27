import telebot
import time

TOKEN='5248166922:AAEker2q1Sx64kNYtirMKBMBw7gLpTes7oA'
bot= telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    print(message.text)

@bot.message_handler(commands=["hi"])
def start(message):
    bot.send_message(message.chat.id, "hii")    


while True:
       try:
           bot.polling()
       except:
           time.sleep(5)    