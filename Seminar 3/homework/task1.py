# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# from random import randint
#
# num = int(input("Введите количество элементов: "))
# num_list = [randint(-num, num) for _ in range(num)]
# sum_list = [num_list[i] for i in range(1, num, 2)]
# num_sum = sum(sum_list)
# print(f"Исходный список: {num_list}\n"
#       f"Элементы на нечётных позициях: {sum_list}\n"
#       f"Их сумма: {num_sum}")

from random import randint

num = int(input("Введите количество элементов: "))
num_list = [randint(-num, num) for _ in range(num)]
num_sum = sum(num_list[1::2])
print(f"Исходный список: {num_list}\n"
      f"Элементы на нечётных позициях: {num_list[1::2]}\n"
      f"Их сумма: {num_sum}")