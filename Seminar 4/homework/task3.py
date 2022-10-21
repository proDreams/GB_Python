# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.

# Первое решение.
numbers_list = list(map(int, input('Введите последовательность чисел: ').split()))
unique_list = []
numbers_list.sort()
current = 0
while current < len(numbers_list):
    check = numbers_list.count(numbers_list[current])
    if check > 1:
        for i in range(check):
            numbers_list.remove(numbers_list[current])
    else:
        unique_list.append(numbers_list[current])
        numbers_list.remove(numbers_list[current])
print(unique_list)

# Моя реализация идеи Наташи с другого потока. Привет Дарье Лютовой ;)
numbers_list = list(map(int, input('Введите последовательность чисел: ').split()))
numbers_list.sort()
unique_dict = {i: numbers_list.count(i) for i in numbers_list}
unique_list = [i for i in unique_dict.keys() if unique_dict[i] == 1]
print(unique_list)

# Самое простое
numbers_list = list(map(int, input('Введите последовательность чисел: ').split()))
unique_list = [i for i in numbers_list if numbers_list.count(i) == 1]
print(unique_list)