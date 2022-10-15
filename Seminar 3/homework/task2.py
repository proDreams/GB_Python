# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
from random import randint

num = int(input("Введите количество элементов: "))
num_list = [randint(-num, num) for _ in range(num)]
prod_list = [num_list[i] * num_list[-i - 1] for i in range((num + 1) // 2)]
# if num % 2 != 0:
#     prod_list.append(num_list[num // 2] ** 2)
print(f"Исходный список: {num_list}\n"
      f"Список пар чисел: {prod_list}")
