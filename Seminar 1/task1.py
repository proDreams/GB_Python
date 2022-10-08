# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры: *
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8, 9 -> нет

num_a = int(input("Введите первое число: "))
num_b = int(input("Введите второе число: "))
if num_a == num_b * num_b or num_b == num_a * num_a:
    print(f"Число {max((num_a, num_b))} является квадратом {min(num_a, num_b)}")
else:
    print(f"Число {max((num_a, num_b))} не является квадратом {min(num_a, num_b)}")
