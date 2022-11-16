from random import randint

# lst = [randint(1, 10) for _ in range(10)]
lst = [1, 2, 3, 5, 1, 5, 3, 10]

####################
# Вариант первый.
print(f'Сгенерированный список: {lst}\n'
      f'Уникальные элементы: {list(filter(lambda x: lst.count(x) < 2, set(lst)))}\n'
      f'Дубликаты: {list(filter(lambda x: lst.count(x) > 1, set(lst)))}\n'
      f'Список без дубликатов: {list(set(lst))}')


####################
# Вариант второй.
lst2, lst3 = [], []
for i in set(lst):
    if lst.count(i) > 1:
        lst3.append(i)
    else:
        lst2.append(i)
print(f'Сгенерированный список: {lst}\n'
      f'Уникальные элементы: {lst2}\n'
      f'Дубликаты: {lst3}\n'
      f'Список без дубликатов: {list(set(lst))}')


####################
# Вариант третий.
lst2 = [i for i in set(lst) if lst.count(i) < 2]
lst3 = [i for i in set(lst) if lst.count(i) > 1]
print(f'Сгенерированный список: {lst}\n'
      f'Уникальные элементы: {lst2}\n'
      f'Дубликаты: {lst3}\n'
      f'Список без дубликатов: {list(set(lst))}')
