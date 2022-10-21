# 2 –Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Подробный вариант
num = int(input("Введите число: "))
prod_list = []
for i in range(1, num + 1):
    temp = 1
    for j in range(1, i + 1):
        temp *= j
    prod_list.append(temp)
print(prod_list)

# Попроще
num = int(input("Введите число: "))
prod_list = []
current = 1
for i in range(1, num + 1):
    current *= i
    prod_list.append(current)
print(prod_list)

# Ещё проще
prod_list = [1]
for i in range(1, int(input("Введите число: ")) + 1):
    prod_list.append(prod_list[i - 1] * i)
print(prod_list)

# Через библиотеку math и цикл
from math import factorial

for i in range(1, int(input('Введите число: '))):
    print(factorial(i), end=' ')

# Однострочный через библиотеку math и цикл
from math import factorial

print([factorial(i) for i in range(1, int(input("Введите число: ")) + 1)])
