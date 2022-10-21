# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Не обращайте на это внимания)
# from random import randint, choice
#
# degree = int(input("Введите степень: "))
# with open('task4.txt', 'w', encoding='utf-8') as f:
#     f.write(f'Список многочленов со степенью {degree}\n')
#     for _ in range(randint(1, 10)):
#         sample = [f'{randint(0, 100)}*(x**{degree}) + {randint(0, 100)}*x + {randint(0, 100)} = 0\n',
#                   f'x**{degree} + {randint(0, 100)} = 0\n',
#                   f'{randint(0, 100)}*(x**{degree}) = 0\n']
#         f.write(choice(sample))
from task4_def import generate_expr

power = int(input("Введите степень: "))
res = generate_expr(power, 't4')
with open('task4.txt', 'w', encoding='utf-8') as f:
    f.write(res)
print(res)
