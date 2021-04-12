import telebot
from telebot import types
from .settings import TOKEN

TOKEN = '1793430012:AAGA6YlLwIVz1G_xh8inXXIsKTRd6PTXRfo'
bot = telebot.TeleBot(TOKEN)

name = ''
surname = ''
age = 0
change_age = False
#check_age = False

@bot.message_handler(content_types=['text'])

def start(message):
    print(message.text)
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как вас зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Напиши /reg")

def get_name(message):
    print(message.text)
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у вас фамилия?")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    print(message.text)
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько вам лет?")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    #print(message.text)
    global age
    global check_age
    check_age = True
    if check_age:
        try:
            age = int(message.text)
            check_age = False
        except Exception:
            bot.send_message(message.from_user.id, "Цифрами, пожалуйста")
            bot.register_next_step_handler(message, get_age)

    #bot.send_message(message.from_user.id, "Тебе " + str(age) + " лет, тебя зовут " + name + " " + surname + "?")

def final(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text = "Да", callback_data = "yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text = "Нет", callback_data = "no")
    keyboard.add(key_no)
    question = "Тебе " + str(age) + " лет, тебя зовут " + name + " " + surname + "?"
    bot.send_message(message.from_user.id, text = question, reply_markup = keyboard)


#def get_text_messages(message):
    #print(message)
    #if message.text.lower() == "привет":
        #bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    #elif message.text.lower() == "кто я?" or "кто я":
        #bot.send_message(message.from_user.id, "Вы " + str(message.from_user.first_name))
    #elif message.text.lower() == "/help":
        #bot.send_message(message.from_user.id, "Напиши привет")
    #else:
        #bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help.")


bot.polling(none_stop=True, interval=0)