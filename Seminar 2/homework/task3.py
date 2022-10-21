# 3 – Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

# Обычный вариант
num = int(input("Введите число: "))
prod_list = [(1 + 1 / n) ** n for n in range(1, num + 1)]
for n in range(num):
    print(sum(prod_list[:n + 1]))

# ...
# print(*[(1 + 1 / n) ** n for n in range(1, int(input("Введите число: ")) + 1)], sep='\n')

# Двухстрочный
prod_list = [(1 + 1 / n) ** n for n in range(1, int(input("Введите число: ")) + 1)]
print(*[sum(prod_list[:i + 1]) for i in range(len(prod_list))], sep='\n')

# Однострочный и ни разу не эффективный
print(*[sum([(1 + 1 / j) ** j for j in range(1, i + 1)][:i]) for i in range(1, int(input("Введите число: ")) + 1)],
      sep='\n')
