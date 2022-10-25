from random import randrange


def write_polynomial(list_02):
    string_02 = ""
    sup_02 = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    if all(item_02 == 0 for item_02 in list_02):
        string_02 += "0"
    else:
        k_02 = len(list_02) - 1
        for i_02 in range(0, len(list_02)):
            if list_02[i_02] == 0:
                k_02 -= 1
                continue
            if i_02 == 0:
                if list_02[i_02] > 1 or list_02[i_02] < 0:
                    string_02 += str(list_02[i_02])
            elif list_02[i_02] < 0:
                string_02 += str(list_02[i_02])
            elif list_02[i_02] > 0:
                if string_02 != "":
                    string_02 += "+ "
                if list_02[i_02] != 1 or i_02 == len(list_02) - 1:
                    string_02 += str(list_02[i_02])
            if i_02 == len(list_02) - 2:
                string_02 += "x "
            elif i_02 == len(list_02) - 1:
                string_02 += " "
            else:
                string_02 += "x" + str(k_02).translate(sup_02) + " "
            k_02 -= 1
        string_02 += "= 0"
    return string_02


def random_list(num1, min1, max1):
    try:
        num1 = int(num1)
        min1 = int(min1)
        max1 = int(max1)
    except:
        print('Your input was incorrect.')
        exit()
    list_1 = [randrange(min1, max1 + 1) for i1 in range(0, num1)]
    return (list_1)


list_1 = random_list(25, 0, 10)
print(list_1)
string_01 = write_polynomial(list_1)
print(string_01)
file01 = open("polynomial.txt", 'a', encoding='utf8')
file01.write(string_01)
