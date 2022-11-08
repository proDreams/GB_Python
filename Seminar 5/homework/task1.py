# Напишите программу, удаляющую из текста все слова, содержащие "абв".
input_data = ['абв', 'обеспАбвечивать', 'приносить', 'западный', 'испытАнибве', 'уезжать', 'абвреформа', 'придумать',
              'присутствовать', 'иабвюнабвь', 'подлинный']
ref = set(i for i in input('Введите строку с символами: ').lower())
print(input_data, [data for data in input_data if not ref <= set(data.lower())], sep='\n')

# Вариант когда слова построчно
# with open('task1_input.txt', 'r', encoding='utf-8') as input_file:
#     input_data = input_file.readlines()
# with open('task1_output.txt', 'w', encoding='utf-8') as output_file:
#     # for data in input_data:
#     #     if not ref < set(data.lower()):
#     #         output_file.write(f'{data}')
#     output_file.writelines([data for data in input_data if not ref < set(data.lower())])


exit()
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
