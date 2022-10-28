# Напишите программу, удаляющую из текста все слова, содержащие "абв".


ref = [i for i in input('Введите строку с символами: ')]


def check_word(word, letters):
    for letter in letters:
        if letter not in word:
            return ''
    else:
        return word


# Вариант когда слова построчно
with open('task1_input.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()
with open('task1_output.txt', 'w', encoding='utf-8') as output_file:
    a = list(map(check_word(input_data, ref), input_data))
    print(a)

exit()
# for data in input_data:
#     for letter in ref:
#         if letter not in data:
#             output_file.write(data)
#             break

# Вариант когда слова одной строкой
with open('task1_input2.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()
with open('task1_output2.txt', 'w', encoding='utf-8') as output_file:
    for data in input_data:
        for word in data.split():
            for letter in ref:
                if letter not in word:
                    output_file.write(f'{word} ')
                    break
        output_file.write('\n')
