# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
from task4_def import generate_expr, create_expr
import ast

k = int(input("Введите степень многочлена: "))
for i in range(1, 3):
    with open(f'task5_{i}.txt', 'w', encoding='utf-8') as f:
        f.write(generate_expr(k, 't5'))

exp_1 = ast.literal_eval(open('task5_1.txt', 'r').read())
exp_2 = ast.literal_eval(open('task5_2.txt', 'r').read())
fst, snd = [], []
result = []
for i in range(len(exp_1)):
    result += (exp_1[i][0] + exp_2[i][0], exp_1[i][1])
for i in range(len(exp_1)):
    fst.append(exp_1[i][0])
    fst.append(exp_1[i][1])
    snd.append(exp_2[i][0])
    snd.append(exp_2[i][1])
print(f'Первый многочлен: {create_expr(fst)}\n'
      f'Второй многочлен: {create_expr(snd)}\n'
      f'Сумма многочленов: {create_expr(result)}')
