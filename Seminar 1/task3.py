# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# Первый вариант
num = int(input("Введите число: "))
for i in range(-num, num + 1):
    print(i, end=" ")
print()

# Упрощаем
num = int(input("Введите число: "))
print(*[i for i in range(-num, num + 1)])

# Ещё упрощаем
num = int(input("Введите число: "))
print(*range(-num, num + 1))

# Применяем "моржовый оператор"
print(*range(-(n := int(input("Введите число: "))), n + 1))
