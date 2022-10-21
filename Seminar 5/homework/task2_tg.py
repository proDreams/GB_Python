from random import choice, randint
import telebot

token = ''
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
    bot.send_message(message.chat.id, 'Введите количество конфет: ')
    candy_count = message.text
    bot.send_message(message.chat.id, f'{candy_count}')


# can_take_candy = int(input('Введите максимальное количество конфет за ход: '))
# players = int(input('Выберете режим игры:\n'
#                     '1. С Искусственным-недоинтеллектом\n'
#                     '2. Два игрока\n'))
# play(candy_count, can_take_candy, players)

bot.polling(none_stop=True, interval=0)
