# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# ...

numbers_string = input("Введите числа через пробел: ")
numbers_list = [int(i) for i in numbers_string.split()]
maxn = numbers_list[0]
minn = numbers_list[1]
for i in numbers_list:
    if maxn < i:
        maxn = i
    elif minn > i:
        minn = i
print(f'Исходная строка: {numbers_string}\n'
      f'Максимальное число: {maxn}\n'
      f'Минимальное число: {minn}\n')

# ... 
numbers_string = [int(i) for i in input().split()]
maxn = max(numbers_string)
minn = min(numbers_string)
print(f'Исходный список: {numbers_string}\n'
      f'Максимальное число: {maxn}\n'
      f'Минимальное число: {minn}\n')