import setting
import telebot

bot = telebot.TeleBot(setting.TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет! Я Simple Testing Bot!')
        bot.send_message(message.from_user.id, 'А как зовут тебя?')
        bot.register_next_step_handler(message, get_name)

    else:
        bot.send_message(message.from_user.id, 'Напиши /start')


def get_name(message):
    global name
    name = message.text
    if message.text.isalpha():
        bot.send_message(message.from_user.id, 'Красивое имя! А сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(message.from_user.id, 'Странное у тебя имя, напиши еще раз.')
        bot.register_next_step_handler(message, get_name)


def get_age(message):
    global age
    age = message.text
    if message.text.isdigit():
        bot.send_message(message.from_user.id, 'Ого, так много! А где ты живешь?')
        bot.register_next_step_handler(message, get_from)
    else:
        bot.send_message(message.from_user.id, 'Я таких цифр не знаю, напиши еще раз.')
        bot.register_next_step_handler(message, get_age)


def get_from(message):
    global place
    place = message.text
    if message.text.isalpha():
        str = 'Спасибо за персональные данные ' + name + '.'
        str = str + ' Я уже знаю, что тебе ' + age + ' лет.'
        str = str + ' И ты из города ' + place + '. '
        bot.send_message(message.from_user.id, str)
        bot.send_message(message.from_user.id, 'Если хочешь расскать о себе еще, введи /more'
                                               ' если хочешь начать заново, введи /start')
        bot.register_next_step_handler(message, get_choose)
    else:
        bot.send_message(message.from_user.id, 'Не слышал о таком, может ты ошибся? Напиши еще раз.')
        bot.register_next_step_handler(message, get_from)


def get_choose(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет! Я Simple Testing Bot!')
        bot.send_message(message.from_user.id, 'А как зовут тебя?')
        bot.register_next_step_handler(message, get_name)
    if message.text == '/more':
        bot.send_message(message.from_user.id, 'Извини, эта функция пока недоступна, поэтому давай начнем сначала.')
        bot.send_message(message.from_user.id, 'Привет! Я Simple Testing Bot!')
        bot.send_message(message.from_user.id, 'А как зовут тебя?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, введи нужную команду еще раз.')
        bot.register_next_step_handler(message, get_choose)


bot.polling()