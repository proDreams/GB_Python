# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
from random import choice, randint


def check_take(count, max_take, player):
    while True:
        if player == 'Искусственный-недоинтеллект':
            num = randint(1, max_take)
        else:
            num = int(input(f'Введите количество конфет от 1 до {max_take}: '))
        if max_take < num:
            print('Ошибка, вы ввели неверное количество конфет, попробуйте снова!')
        elif num > count:
            print('Ошибка, нельзя взять конфет больше, чем в банке, попробуйте снова!')
        else:
            return num


def play_process(count, max_take, player_one, player_two):
    turn = 1
    print(f'В банке с конфетами: {count}')
    while count > 0:
        if turn == 1:
            player_take = check_take(count, max_take, player_one)
            print(f'Игрок {player_one} забирает из банки {player_take}')
            count -= player_take
            print(f'В банке осталось конфет: {count}')
            turn = 2
        else:
            player_take = check_take(count, max_take, player_two)
            print(f'Игрок {player_two} забирает из банки {player_take}')
            count -= player_take
            print(f'В банке осталось конфет: {count}')
            turn = 1
        print()
    return turn


def play(count, max_take, players):
    player_one_name = input('Введите имя первого игрока: ')
    if players == 2:
        player_two_name = input('Введите имя второго игрока: ')
    else:
        player_two_name = 'Искусственный-недоинтеллект'
    coin = choice(['Орёл', 'Решка'])
    if coin == 'Орёл':
        print(f'Выпал Орёл, первым ходит {player_one_name}')
    else:
        player_one_name, player_two_name = player_two_name, player_one_name
        print(f'Выпала Решка, первым ходит {player_one_name}')
    if play_process(count, max_take, player_one_name, player_two_name) == 2:
        print(f'Победил игрок \033[1m{player_one_name}\033[0m! Поздравляем!')
    else:
        print(f'Победил игрок \033[1m{player_two_name}\033[0m! Поздравляем!')


print('''
\033[1mДобро пожаловать в игру с конфетами!\033[0m
\033[4mПравила игры:\033[0m
На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
''')
candy_count = int(input('Введите количество конфет: '))
can_take_candy = int(input('Введите максимальное количество конфет за ход: '))
players = int(input('Выберете режим игры:\n'
                    '1. С Искусственным-недоинтеллектом\n'
                    '2. Два игрока\n'))
play(candy_count, can_take_candy, players)
