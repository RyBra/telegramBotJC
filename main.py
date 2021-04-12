import telebot
from telebot import types
from .settings import TOKEN

bot = telebot.TeleBot(TOKEN)


def anime_check(message):
    return {'anime', 'аниме'} & set(message.lower().split())
    # message = message.lower()
    # splited_message = message.split(' ')
    #
    # for msg in splited_message:
    #     if msg == "аниме" or msg == "anime":
    #         return True
    # return False


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


bot.polling(none_stop=True, interval=0)

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     print(message.from_user.id)
#     if message.text == "kek)":
#         bot.send_message(message.from_user.id,
#                          'Это Дима')
#     elif message.text.lower() == "pek":
#         bot.send_message(message.from_user.id,
#                          'tuk')
#     elif message.text.lower() == "С др":
#         bot.send_message(message.from_user.id,
#                          'Бан Сереге')
#     elif anime_check(message.text):
#         bot.send_message(message.from_user.id,
#                          'chel')
