# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

str_list = ['a1b2c3', 'q11w22e33', 'z123x234c345']
num = input("Введите число для поиска: ")
for i in str_list:
    if num in i:
        print(f"Число {num} присутствует")
        break
else:
    print("Число  не найдено")
