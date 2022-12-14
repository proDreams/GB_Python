# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)
####################################################
# Самый простой вариант алгоритма поиска числа pi, не самый точный,
# но если увеличивать степень 10, скорость работы сокращается очень сильно,
# но растёт точность,
# frac = int(input("Введите количество знаков после запятой (от 1 до 10): "))
# num = 0
# count = 1
# for i in range(10 ** 6):
#     if i % 2 == 0:
#         num += 4 / count
#     else:
#         num -= 4 / count
#     count += 2
# print(f"Число π с точностью до {frac} знаков = {round(num, frac)}")
##########################################################

# ..
from decimal import Decimal

num = Decimal(input("Введите вещественное число: "))
num_d = Decimal(input("Введите вещественное число обозначающее точность.\n"
                      "От 10^-1 до 10^-1: "))
num_r = num.quantize(Decimal(f'{1 + num_d}'))
print(f'Введённое число: {num}\n'
      f'Точность: {num_d}\n'
      f'Результат: {num_r}')