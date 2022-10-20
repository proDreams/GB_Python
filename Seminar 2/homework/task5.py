# 5 – Реализуйте алгоритм перемешивания списка.

# Через цикл и функцию randint
from random import randint

num_list = [i for i in range(10)]
print(f"Оригинальный список: {num_list}")
for i in range(len(num_list)):
    rand = randint(0, 9)
    num_list[i], num_list[rand] = num_list[rand], num_list[i]
print(f"Перемешанный список: {num_list}")

# Через функцию shuffle
from random import shuffle

num_list1 = [i for i in range(10)]
print(f"Оригинальный список: {num_list1}")
shuffle(num_list1)
print(f"Перемешанный список: {num_list1}")
