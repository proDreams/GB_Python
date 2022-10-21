from random import choice, randint
import telebot

token = '5547883029:AAHXpDkCp3v4ctgLSZeydOwjDFiQCaEYRpg'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''Добро пожаловать в игру с конфетами!
Правила игры:
На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
''')


bot.polling(none_stop=True)
