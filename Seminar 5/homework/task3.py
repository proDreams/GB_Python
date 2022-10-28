# Создайте программу для игры в "Крестики-нолики".
from random import choice


def create_board(size):
    board_matrix = [['.' for _ in range(size + 1)] for _ in range(size + 1)]
    board_matrix[0][0] = ''
    board_matrix[0][1:] = [str(i) for i in range(1, size + 1)]
    for i in range(1, size + 1):
        board_matrix[i][0] = chr(64 + i)
    return board_matrix


def fill_turn(player_turn, game_board, turn):
    if turn == 1:
        game_board[player_turn[0]][player_turn[1]] = 'X'
    else:
        game_board[player_turn[0]][player_turn[1]] = 'O'


def print_board(board_matrix):
    for i in board_matrix:
        for j in i:
            print(j.ljust(5), end='')
        print()


def start_game(game_board, size):
    player_one_name = input('Введите имя первого игрока: ')
    player_two_name = input('Введите имя второго игрока: ')
    coin = choice(['Орёл', 'Решка'])
    if coin == 'Орёл':
        print(f'Выпал Орёл, первым ходит {player_one_name}')
        turn = 1
    else:
        print(f'Выпала Решка, первым ходит {player_two_name}')
        turn = 2
    play_process(player_one_name, player_two_name, turn, game_board, size)


def get_turn(player_name, size, game_board):
    while True:
        player_turn = input(f'Ход игрока {player_name}\n'
                            f'Введите координату хода в виде, например A2\n'
                            f'Где буква = строка, а цифра = столбец: ')
        if player_turn[0].isalpha() and player_turn[1].isdigit():
            if ord(player_turn[0]) - 64 > size or int(player_turn[1]) > size:
                print('Ошибка! Введена неверная координата!')
            else:
                if game_board[ord(player_turn[0]) - 64][int(player_turn[1])] == 'X' or \
                        game_board[ord(player_turn[0]) - 64][int(player_turn[1])] == 'O':
                    print('Ошибка! Координата уже введена!')
                else:
                    return ord(player_turn[0]) - 64, int(player_turn[1])
        else:
            print('Ошибка! Введена неверная координата!')


def check_win(player_one_turns, player_two_turns, size, game_board):
    flag = 'AAA'
    if len(player_one_turns) + len(player_two_turns) >= size:
        for i in player_one_turns, player_two_turns:
            for j in i:
                if game_board[j[0]][j[1]] == (game_board[j[0] - 1][j[1]]) == (
                        game_board[j[0] + 1][j[1]] if j[0] + 1 <= size else False):
                    return game_board[j[0]][j[1]]
                elif game_board[j[0]][j[1]] == (game_board[j[0]][j[1] - 1]) == (
                        game_board[j[0]][j[1] + 1]):
                    return game_board[j[0]][j[1]]
                elif game_board[j[0]][j[1]] == (game_board[j[0] - 1][j[1] - 1]) == (
                        game_board[j[0] + 1][j[1] + 1] if j[1] + 1 <= size else False):
                    return game_board[j[0]][j[1]]
                elif game_board[j[0]][j[1]] == (game_board[j[0] + 1][j[1] - 1]) == (
                        game_board[j[0] - 1][j[1] + 1] if j[1] + 1 <= size else False):
                    return game_board[j[0]][j[1]]
    return flag


def play_process(player_one_name, player_two_name, turn, game_board, size):
    print_board(game_board)
    player_one_turns = []
    player_two_turns = []
    while True:
        if turn == 1:
            player_turn = get_turn(player_one_name, size, game_board)
            player_one_turns.append(player_turn)
            fill_turn(player_turn, game_board, turn)
            turn = 2
        elif turn == 2:
            player_turn = get_turn(player_two_name, size, game_board)
            player_two_turns.append(player_turn)
            fill_turn(player_turn, game_board, turn)
            turn = 1
        print_board(board)
        winner = check_win(player_one_turns, player_two_turns, size, game_board)
        if winner == 'X':
            print(f'Победил игрок {player_one_name}')
            break
        elif winner == 'O':
            print(f'Победил игрок {player_two_name}')
            break


print('''
\033[1mДобро пожаловать в игру крестики-нолики!\033[0m
''')
board_size = 7
board = create_board(board_size)
print_board(board)
start_game(board, board_size)
