# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Вариант когда слова построчно
with open('task1_input.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()
with open('task1_output.txt', 'w', encoding='utf-8') as output_file:
    for data in input_data:
        if 'абв' not in data.rstrip():
            output_file.write(data)

# Вариант когда слова одной строкой
with open('task1_input2.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()
with open('task1_output2.txt', 'w', encoding='utf-8') as output_file:
    for data in input_data:
        for word in data.split():
            if 'абв' not in word:
                output_file.write(f'{word} ')
        output_file.write('\n')
