# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#  Пример:
# Для N = 5: 1, -3, 9, -27, 81

num = int(input("Введите число: "))
res_list = [1]
for i in range(1, num):
    if i % 2 == 0:
        res_list.append(abs(res_list[i - 1]) * 3)
    else:
        res_list.append(-(abs(res_list[i - 1]) * 3))
print(*res_list)


