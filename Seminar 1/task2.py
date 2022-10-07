# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

num_a = int(input("Введите первое число: "))
num_b = int(input("Введите второе число: "))
num_c = int(input("Введите третье число: "))
num_d = int(input("Введите четвёртое число: "))
num_e = int(input("Введите пятое число: "))

maximum = num_a

if num_b > maximum:
    maximum = num_b
    if num_c > maximum:
        maximum = num_c
        if num_d > maximum:
            maximum = num_d
            if num_e > maximum:
                maximum = num_e
if num_c > maximum:
    maximum = num_c
    if num_d > maximum:
        maximum = num_d
        if num_e > maximum:
            maximum = num_e
if num_d > maximum:
    maximum = num_d
    if num_e > maximum:
        maximum = num_e
if num_e > maximum:
    maximum = num_e

print(f"Число {maximum} больше всех")
