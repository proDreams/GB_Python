# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform

num = int(input("Введите количество элементов: "))
num_list = [round(uniform(1, num), 2) for _ in range(num)]
max_num, min_num = round(num_list[0] % 1, 2), round(num_list[0] % 1, 2)
for i in range(num):
    if max_num < round(num_list[i] % 1, 2):
        max_num = round(num_list[i] % 1, 2)
    elif min_num > round(num_list[i] % 1, 2):
        min_num = round(num_list[i] % 1, 2)
print(f'Исходный список: {num_list}\n'
      f'Максимальное дробное число: {max_num}\n'
      f'Минимальное дробное число: {min_num}\n'
      f'Разница между максимальным и минимальным: {round(max_num - min_num, 2)}')
