# Задача 4 в обратном порядке.

from random import randint

nums = open('task4.txt', 'r')
num_list = [int(i) for i in nums]
num = int(input("Введите число: "))
indexes = [randint(-num, num) for i in range(num)]
prod_num = 1
for i in indexes:
    if i < len(num_list):
        prod_num *= num_list[i]
print(indexes, prod_num, sep='\n')
nums.close()
