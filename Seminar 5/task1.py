# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
from random import randint

with open('task1.txt', 'r', encoding='utf-8') as f:
    lst = list(map(int, f.read().split()))
print(f'Список в файле: {lst}')
lst.sort()
for i in range(1, len(lst)):
    if lst[i] - 1 != lst[i - 1]:
        print(f'Не хватает {lst[i] - 1}')
        break
