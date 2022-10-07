# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

numbers = [int(input("Введите число: ")) for _ in range(5)]
maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i

print(f"Число {maximum} больше всех")
