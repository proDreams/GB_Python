def input_coord(n):
    try:
        return int(input(f'Input {n} coordinate.. \n'))
    except:
        print('Wrong input')


def define_quarter(x2, y2):
    if y2 == 0:
        if x2 == 0:
            print('Center')
        else:
            print('Axis')

    elif x2 == 0:
        print('Axis Y')

    elif x2 > 0:
        if y2 > 0:
            print('Quarter 1')
        elif y2 < 0:
            print('Quarter 4')

    elif x2 < 0:
        if y2 > 0:
            print('Quarter 2')
        elif y2 < 0:
            print('Quarter 3')


print('This program will indicate # of quarter based on coordinates.')
define_quarter(input_coord('1st'), input_coord('2nd'))
