from random import choice, randint
import telebot

token = ''
bot = telebot.TeleBot(token)
candy_count = 0
can_take_candy = 0
player_one_name = ''
player_two_name = 'Искусственный-недоинтеллект'
current_take = 0
player_turn = 1
turn = 1


@bot.message_handler(commands=['start'])
def start_message(message):
    hello = bot.send_message(message.chat.id, '''Добро пожаловать в игру с конфетами!
Правила игры:
На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
''')
    bot.send_message(message.chat.id, 'Введите количество конфет: ')
    bot.register_next_step_handler(hello, candy_count_req)


def candy_count_req(message):
    global candy_count
    candy_count = int(message.text)
    bot.send_message(message.chat.id, 'Введите максимальное количество конфет за ход: ')
    bot.register_next_step_handler(message, can_take_candy_req)


def can_take_candy_req(message):
    global can_take_candy
    can_take_candy = int(message.text)
    bot.send_message(message.chat.id, 'Введите имя первого игрока: ')
    bot.register_next_step_handler(message, play)


def play(message):
    global player_one_name
    global player_two_name
    player_one_name = message.text
    coin = choice(['Орёл', 'Решка'])
    if coin == 'Орёл':
        bot.send_message(message.chat.id, f'Выпал Орёл, первым ходит {player_one_name}')
        bot.send_message(message.chat.id, f'В банке с конфетами: {candy_count}')
        bot.send_message(message.chat.id, f'Введите количество конфет от 1 до {can_take_candy}: ')
        bot.register_next_step_handler(message, play_process)
    else:
        player_one_name, player_two_name = player_two_name, player_one_name
        bot.send_message(message.chat.id, f'Выпала Решка, первым ходит {player_one_name}')
        bot.send_message(message.chat.id, f'В банке с конфетами: {candy_count}')
        bot.send_message(message.chat.id, f'Введите количество конфет от 1 до {can_take_candy}: ')
        bot.register_next_step_handler(message, play_process)


def play_process(message):
    global candy_count
    global player_turn
    global turn
    global can_take_candy
    if candy_count > 0:
        if turn == 1:
            player_turn = player_one_name
            player_take = check_take(message)
            bot.send_message(message.chat.id, f'Игрок {player_one_name} забирает из банки {player_take}')
            candy_count -= player_take
            bot.send_message(message.chat.id, f'В банке осталось конфет: {candy_count}')
            bot.send_message(message.chat.id, f'Введите количество конфет от 1 до {can_take_candy}: ')
            turn = 2
            bot.register_next_step_handler(message, play_process)
        else:
            player_turn = player_two_name
            player_take = check_take(message)
            bot.send_message(message.chat.id, f'Игрок {player_two_name} забирает из банки {player_take}')
            candy_count -= player_take
            bot.send_message(message.chat.id, f'В банке осталось конфет: {candy_count}')
            bot.send_message(message.chat.id, f'Введите количество конфет от 1 до {can_take_candy}: ')
            turn = 1
            bot.register_next_step_handler(message, play_process)
    elif turn == 2:
        bot.send_message(message.chat.id, f'Победил игрок {player_one_name}! Поздравляем!')
    else:
        bot.send_message(message.chat.id, f'Победил игрок {player_two_name}! Поздравляем!')


def check_take(message):
    global current_take
    global can_take_candy
    if candy_count < can_take_candy:
        can_take_candy = candy_count
    if player_turn == 'Искусственный-недоинтеллект':
        current_take = randint(1, can_take_candy)
    else:
        current_take = int(message.text)
    if can_take_candy < current_take:
        bot.send_message(message.chat.id, 'Ошибка, вы ввели неверное количество конфет, попробуйте снова!')
        bot.send_message(message.chat.id, f'Введите количество конфет от 1 до {can_take_candy}: ')
        bot.register_next_step_handler(message, check_take)
    elif current_take > candy_count:
        bot.send_message(message.chat.id, 'Ошибка, нельзя взять конфет больше, чем в банке, попробуйте снова!')
        bot.send_message(message.chat.id, f'Введите количество конфет от 1 до {can_take_candy}: ')
        bot.register_next_step_handler(message, check_take)
    else:
        return current_take


bot.polling(none_stop=True, interval=0)
