# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

lst = [2, 5, 2, 3, 4, 6, 1, 7]
while lst[0] + 1 not in lst:
    lst.remove(lst[0])
result = [lst[0]]
for i in lst:
    if i > result[-1]:
        result.append(i)
print(result)
