# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# -n, n
num = int(input("Введите число: "))
num_list = [i for i in range(-num, num + 1)]
indexes = open('task4.txt', 'r')
prod_num = 1
for i in indexes:
    if int(i) < len(num_list):
        prod_num *= num_list[int(i)]
print(num_list, prod_num, sep='\n')
indexes.close()

# random
from random import randint

num = int(input("Введите число: "))
num_list = [randint(-num, num) for i in range(num)]
indexes = open('task4.txt', 'r')
prod_num = 1
for i in indexes:
    if int(i) < num:
        prod_num *= num_list[int(i)]
print(num_list, prod_num, sep='\n')
indexes.close()
