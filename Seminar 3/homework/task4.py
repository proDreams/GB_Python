# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# Решал такую задачу на степике, вроде неплохо получилось)
def bin_octa(num, prod):
    result = []
    while num > 0:
        result.append(num % prod)
        num //= prod
    return result


def hexa(num):
    result = []
    alp = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while num > 0:
        if num % 16 > 9:
            result.append(alp[num % 16])
        else:
            result.append(num % 16)
        num //= 16
    return result


while True:
    d = int(input('Выберите систему счисления от 2 до 12 или 16\n'
                  'Или 0 для выхода: '))
    n = int(input('Введите число: '))

    if 1 < d < 13:
        print(*bin_octa(n, d)[::-1], sep='')
    elif d == 16:
        print(*hexa(n)[::-1], sep='')
    elif d == 0:
        break
    else:
        print('Такой системы нет в списке. Доступны от 2 до 12 или 16 и 0 для выхода')
