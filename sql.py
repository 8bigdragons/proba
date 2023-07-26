import telebot
import sqlite3
from telebot import types
bot = telebot.TeleBot('6654201797:AAGL9XKox4I_Qr3Z4WUnh4vmGt7YnQV5Lkw')
name = None
password = None



'''global again
def again(message, f):
    if message.text.lower() == "again":
        f(message)
    elif message.text.lower() == "stop":
        stop(message)'''



@bot.message_handler(commands = ['start'])
def start(message):
    conn = sqlite3.connect('money.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key,name varchar(50),pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "Put your name")
    bot.register_next_step_handler(message,user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "Put your password")
    bot.register_next_step_handler(message,user_pass)

def user_pass(message):
    global password
    password = message.text.strip()
    bot.send_message(message.chat.id, "I've started registration. Write Okey, if you're agree")
    bot.register_next_step_handler(message, user_registration)

def user_registration(message):
    conn = sqlite3.connect('money.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users(name,pass) VALUES ('%s','%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Users', callback_data= 'users'))
    bot.send_message(message.chat.id, "You've been registered", reply_markup=markup)

@bot.callback_query_handler(func = lambda callback : True)
def callback_message(callback):
    conn = sqlite3.connect('money.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM USERS')
    users = cur.fetchall()
    info = ''
    for i in users:
        info += f'Name: {i[1]}, Password: {i[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(callback.message.chat.id,info)

bot.polling(none_stop = True)