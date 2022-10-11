# 1 – Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Подробный вариант через map()
num_str = input("Введите число: ")
if '.' in num_str:
    num_str = num_str.replace('.', '')
elif ',' in num_str:
    num_str = num_str.replace(',', '')
num_list = map(int, num_str)
num_sum = sum(num_list)
print(num_sum)

# Подробный вариант через цикл
num_str = input("Введите число: ")
if '.' in num_str:
    num_str = num_str.replace('.', '')
elif ',' in num_str:
    num_str = num_str.replace(',', '')
num_sum = 0
for i in num_str:
    num_sum += int(i)
print(num_sum)

# Однострочный вариант через map()
print(sum(map(int, input("Введите число: ").replace('.', '').replace(',', ''))))

# Однострочный вариант через цикл
print(sum([int(i) for i in input("Введите число: ").replace('.', '').replace(',', '')]))
