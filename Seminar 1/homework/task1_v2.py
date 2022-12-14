# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

n = int(input("Введите номер дня недели: "))
match n:
    case 6 | 7:
        print("Выходной!")
    case n if 1 <= n <= 5:
        print("Будни")
    case _:
        print("Не день недели")
