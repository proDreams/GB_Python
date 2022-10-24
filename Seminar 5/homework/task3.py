# Создайте программу для игры в "Крестики-нолики".
from random import choice


def create_board(size):
    board_matrix = [['.' for _ in range(size + 1)] for _ in range(size + 1)]
    board_matrix[0][0] = ''
    board_matrix[0][1:] = [str(i) for i in range(1, size + 1)]
    for i in range(1, size + 1):
        board_matrix[i][0] = chr(64 + i)
    return board_matrix


def fill_turn(player_turn, game_board):


def print_board(board_matrix):
    for i in board_matrix:
        for j in i:
            print(j.ljust(5), end='')
        print()


def start_game(mode, game_board, size):
    player_one_name = input('Введите имя первого игрока: ')
    if mode == 2:
        player_two_name = input('Введите имя второго игрока: ')
    else:
        player_two_name = 'Искусственный-недоинтеллект'
    coin = choice(['Орёл', 'Решка'])
    if coin == 'Орёл':
        print(f'Выпал Орёл, первым ходит {player_one_name}')
        turn = 1
    else:
        print(f'Выпала Решка, первым ходит {player_two_name}')
        turn = 2
    play_process(player_one_name, player_two_name, turn, game_board, size)


def get_turn(player_name, size)
    while True:
        player_turn = input(f'Ход игрока {player_name}\n'
                            f'Введите координату хода в виде, например a2\n'
                            f'Где буква = строка, а цифра = столбец: ').split()
        if player_turn[0].isalpha() and player_turn[1].isdigit():
            if ord(player_turn[0]) - 64 > size or player_turn[1] > size:
                print('Ошибка! Введена неверная координата!')
            else:
                return player_turn
        else:
            print('Ошибка! Введена неверная координата!')


def play_process(player_one_name, player_two_name, turn, game_board):
    print_board(game_board)
    while True:
        if turn == 1:
            player_turn = get_turn(player_one_name, size)
            fill_turn(player_turn, game_board)


while True:
    board_size = int(input("Введите размер доски (3, 5, 7): "))
    if board_size != 3 or board_size != 5 or board_size != 7:
        print('Ошибка, неверный размер доски!\n')
    else:
        break
game_mode = int(input("1. Игра против бота\n"
                      "2. Игра для двух человек\n"
                      "Выберите режим игры: "))
board = create_board(board_size)
start_game(game_mode, board, board_size)
