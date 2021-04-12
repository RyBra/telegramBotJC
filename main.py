import telebot
from telebot import types
from .settings import TOKEN

bot = telebot.TeleBot(TOKEN)


def anime_check(message):
    return {'anime', 'аниме'} & set(message.lower().split())


name = ''
surname = ''
age = 0
check_age = True


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    global check_age

    if check_age:
        try:
            age = int(message.text)
            check_age = False
            bot.register_next_step_handler(message, final)
        except Exception:
            bot.send_message(message.from_user.id,
                             'Цифрами, пожалуйста')
            bot.register_next_step_handler(message, get_age)


def final(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да',
                                         callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет',
                                        callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' \
               + surname + '?'
    bot.send_message(message.from_user.id, text=question,
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        pass


bot.polling(none_stop=True, interval=0)





