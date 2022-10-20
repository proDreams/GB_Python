from random import randint, choice


def generate_expr(k, t):
    result = ''
    result2 = []
    while k >= 0:
        rand = randint(0, 100)
        if k == 1:
            k_op = 'x'
        else:
            k_op = f'x^{k}'
        if rand > 1 and k != 0:
            result += f'{rand}{k_op}' + ' + '
        elif rand == 1 and k != 0:
            result += f'{k_op}' + ' + '
        result2.append((rand, k))
        k -= 1
    if t == 't4':
        return result + f'{randint(0, 100)} = 0'
    else:
        return f'{result2}'


def create_expr(coeff):
    result = ''
    for i in range(0, len(coeff), 2):
        k = coeff[i + 1]
        coef = coeff[i]
        if k == 1:
            k_op = 'x'
        elif k == 0:
            k_op = ''
        else:
            k_op = f'x^{k}'
        if coef > 1 and k != 0:
            result += f'{coef}{k_op}' + ' + '
        elif coef == 1:
            result += f'{coef}' + ' + '
        else:
            result += f'{coef} = 0'
    return result
