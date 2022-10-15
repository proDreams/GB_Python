# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform

num = int(input("Введите количество элементов: "))
num_list = [round(uniform(1, num), 2) for _ in range(num)]
max_num, min_num = num_list[0] % 1, num_list[0] % 1
for i in num_list:
    if max_num < i % 1:
        max_num = i % 1
    elif min_num > i % 1:
        min_num = i % 1
print(f'Исходный список: {num_list}\n'
      f'Максимальное дробное число: {max_num:.2f}\n'
      f'Минимальное дробное число: {min_num:.2f}\n'
      f'Разница между максимальным и минимальным: {max_num - min_num:.2f}')
