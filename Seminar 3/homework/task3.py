# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform

num = int(input("Введите количество элементов: "))
roun = int(input("Введите точность: "))
num_list = [round(uniform(1, num), roun) for _ in range(num)]
max_num, min_num = round(num_list[0] % 1, roun), round(num_list[1] % 1, roun)
for i in num_list:
    temp = round(i % 1, roun)
    if max_num < temp:
        max_num = temp
    elif min_num > temp:
        min_num = temp
print(f'Исходный список: {num_list}\n'
      f'Максимальное дробное число: {round(max_num, roun)}\n'
      f'Минимальное дробное число: {round(min_num, roun)}\n'
      f'Разница между максимальным и минимальным: {round(max_num - min_num, roun)}')
