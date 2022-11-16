# def candy_game_move(player_num, name_1, name_2, remain_q):
#     if player_num == 1:  # user input
#         move_01 = input(f'\033[36m{remain_q} candies remaining. Make your move, {name_1}\n')
#     else:
#         move_01 = input(f'\033[00m{remain_q} candies remaining. Make your move, {name_2}\n')
#     try:
#         move_01 = int(move_01)
#     except:  # check if not integer input
#         print('Your input was incorrect! Please repeat.')
#         candy_game_move(player_num, name_1, name_2, remain_q)
#     if move_01 < 1 or move_01 > remain_q or move_01 > 28:  # check if not correct number input
#         print('Your input was incorrect! Please repeat.')
#         candy_game_move(player_num, name_1, name_2, remain_q)
#
#     remain_q -= move_01  # main move
#
#     if remain_q == 0:  # check if WIN (end of game)
#         if player_num == 1:
#             print(f'\033[36mPlayer {name_1} has won and gets all 2021 candies. Congratulations, \033[01m{name_1}!')
#             exit()
#         else:
#             print(f'\033[00mPlayer {name_2} has won and gets all 2021 candies. Congratulations, \033[01m{name_2}!')
#             exit()
#     else:
#         if player_num == 1:  # change player section
#             player_num = 2
#         else:
#             player_num = 1
#
#         candy_game_move(player_num, name_1, name_2, remain_q)  # main recursion
#
#
# print('This is 2 player candy game of 2021 candies. Each player takes not more than 28 candies. '
#       'Please note that the player who makes the Last move wins and takes all the candies.')
# name_1 = input('\033[36mInput Name1\n')
# name_2 = input('\033[00mInput Name2\n')
# candy_game_move(1, name_1, name_2, 2021)

################
# count = 0
# for i in range(2, 10):
#     for j in range(2, i // 2 + 1):
#         if i % j == 0:
#             break
#     else:
#         count += 1
# print(count)
##############
#
lst = ['h', 'g', 'd', 'y', 'u']
start = 32
for i in range(len(lst)):
    while True:
        if chr(start) in lst:
            lst[i], lst[lst.index(chr(start))] = lst[lst.index(chr(start))], lst[i]
            start += 1
            break
        else:
            start += 1
print(lst)
#
#################################

# lst = [6, 7, 7, 1, 2, 3, 4, 5]
# for i in range(1, len(lst)):
#     if lst[i] < lst[i - 1]:
#         print(f'Индекс {i - 1}, макс число {lst[i - 1]}')
#         break

# Пример строк которые не должны быть выделены выражением:
#
# "агент007" - содержит цифры
# "стриж" - только строчные буквы
# "ГТО", - более одной заглавной буквы
# "Три богатыря" - содержит пробел, допустимы только буквы

# Состоят только из букв
# Одна и только одна из букв является заглавной
import re

lst = ["Мама", "Я", "гриБ", 'Яблоко', 'apple', 'Apple', 'APle', 'Appl0', 'яблокО']
lst2 = ["Агент007", "стриж", "ГТО", "Три богатыря"]
# a = re.search(r'^\w*?[А-Я]\w*$', lst2[0])
a = re.search(r'^(([а-я]*[А-Я][а-я]*)|([a-z]*[A-Z][a-z]*))$', lst[6])
# a = re.search(r'[а-я]*?[А-Я][а-я]*', lst2[0])
print(a[0])



