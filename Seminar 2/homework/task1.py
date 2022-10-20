# # 1 – Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # 6782 -> 23
# # 0,56 -> 11
#
# # Подробный вариант через map()
# num_str = input("Введите число: ")
# if '.' in num_str:
#     num_str = num_str.replace('.', '')
# elif ',' in num_str:
#     num_str = num_str.replace(',', '')
# num_list = map(int, num_str)
# num_sum = sum(num_list)
# print(num_sum)
#
# # Подробный вариант через цикл
# num_str = input("Введите число: ")
# if '.' in num_str:
#     num_str = num_str.replace('.', '')
# elif ',' in num_str:
#     num_str = num_str.replace(',', '')
# num_sum = 0
# for i in num_str:
#     num_sum += int(i)
# print(num_sum)
#
# # Однострочный вариант через map()
# print(sum(map(int, input("Введите число: ").replace('.', '').replace(',', ''))))
#
# # Однострочный вариант через цикл
# print(sum([int(i) for i in input("Введите число: ").replace('.', '').replace(',', '')]))

# Стырил со стаковерфло)
num_str = input("Введите число: ").translate(str.maketrans({',': '', '.': '', '-': ''}))
print(sum(map(int, num_str)))

# Не совсем понял как работает фильтр и совсем не знаком с лямбдой. С этим помог одногруппник)
num_str = input("Введите число: ")
num_list = [*filter(lambda c: c not in ['.', ','], num_str)]
num_sum = 0
for i in num_list:
    num_sum += int(i)
print(num_sum)

# Увеличиваем вещественное до целого и целое в цикле складываем.
# Тут пришлось гуглить, как узнать сколько символов после запятой
num = float(input("Введите число: "))
after_com = abs(str(num).find('.') - len(str(num)))
num = int(num * (10 ** after_com))
num_sum = 0
while num != 0:
    num_sum += num % 10
    num //= 10
print(num_sum)

# Вариант через Decimal
from decimal import *

num = Decimal(12.345)
getcontext().prec = 10

while True:
    if num % 10 != 0:
        num *= 10
    else:
        num = int(num // 10)
        break
num_sum = 0
while num != 0:
    num_sum += num % 10
    num //= 10
print(num_sum)
