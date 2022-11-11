# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;
# Очевиднейший вариант.
# print(eval(input('Введите выражение: ')))
#################################################################################
from decimal import Decimal


def create_lists(text):
    num = ''
    op = ''
    for i in text:
        if i.isdigit() or i == '.':
            num += i
        elif i == ' ':
            continue
        else:
            num += ' '
            op += i
    return list(map(Decimal, num.split())), list(op)


def calc(num, op):
    while len(num) > 1:
        temp = 0
        prod_div = min(op.index('*') if '*' in op else len(op),
                       op.index('/') if '/' in op else len(op))
        add_sub = min(op.index('-') if '-' in op else len(op),
                      op.index('+') if '+' in op else len(op))
        if prod_div != len(op):
            if op[prod_div] == '*':
                temp = num[prod_div] * num[prod_div + 1]
            elif op[prod_div] == '/':
                temp = num[prod_div] / num[prod_div + 1]
            del num[prod_div]
            num[prod_div] = temp
            del op[prod_div]
        elif add_sub != len(op):
            if op[add_sub] == '+':
                temp = num[add_sub] + num[add_sub + 1]
            elif op[add_sub] == '-':
                temp = num[add_sub] - num[add_sub + 1]
            del num[add_sub]
            num[add_sub] = temp
            del op[add_sub]
    return num


input_text = input('Введите выражение для вычисления: ')
while ')' in input_text:
    right = input_text.find(')')
    left = input_text[:right].rfind('(')
    temp_n, temp_o = create_lists(input_text[left + 1:right])
    temp_n = str(*calc(temp_n, temp_o))
    input_text = input_text[:left] + temp_n + input_text[right + 1:]
numbers, operators = create_lists(input_text)
calc(numbers, operators)
print(numbers[0].normalize())
