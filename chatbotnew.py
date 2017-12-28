import sys
import time
import telebot
import json
import traceback


#get token from command-line

TOKEN = "437747070:AAGZFFQ2UJp2C-csmPFkpRo6zuICpiVnfeg"
bot = telebot.TeleBot("437747070:AAGZFFQ2UJp2C-csmPFkpRo6zuICpiVnfeg")
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
       telebot.types.InlineKeyboardButton(
          'Gnowledge Lab' , url='https://abcde.metastudio.org/welcome'
          )
       )
    bot.send_message(
       message.chat.id,
       'Greetings! I am your new assistant.\n' +
       'To get the information about Gnowledge Lab, click the button below.\n' +
       'To get help press /help.',
       reply_markup=keyboard
   )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        '1. To register as a new user press /register. To login as a member press /login.\n' +
        '2. To search for information press /search. \n' +
        '3. To end chat with me press /done. \n'
        )

@bot.message_handler(commands=['register' 'login'])
def reg_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
       telebot.types.InlineKeyboardButton(
          'Register' , url='https://abcde.metastudio.org/accounts/register'
          ),
        telebot.types.InlineKeyboardButton(
          'Login' , url='https://abcde.metastudio.org/accounts/login'
          
       )
      ) 
    bot.send_message(
       message.chat.id,
       'Kindly register to become a member of the organization. To register click on Register  or Login. \n' ,
       reply_markup=keyboard
       )
     
@bot.message_handler(commands=['done'])
def done_command(message):
   bot.send_message(
    message.chat.id,
    'Okay Bye! See you soon. \n'
    )
   bot.polling(none_stop=False)

bot.polling(none_stop=True)     
