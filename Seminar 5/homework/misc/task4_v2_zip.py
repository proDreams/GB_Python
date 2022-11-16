import os.path

numbers_dict = {i: chr(i + 48) for i in range(1, 74)}
dict_size = len(numbers_dict)

with open('../task4_zip_input.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()[0]
print(f'Исходная строка: {input_data}\n'
      f'Размер файла {os.path.getsize("../task4_zip_input.txt")} байт')

with open('../task4_output.txt', 'w', encoding='utf-8') as output_file:
    result = ''
    count = 0
    while True:
        for i in range(len(input_data)):
            if input_data[0] == input_data[i]:
                count += 1
            else:
                break
        if count > dict_size:
            temp = count
            while temp > 0:
                result += f'{numbers_dict[dict_size] if temp > dict_size else temp}{input_data[0]}'
                temp -= dict_size
        else:
            result += f'{numbers_dict[count]}{input_data[0]}'
        input_data = input_data[count:]
        count = 0
        if len(input_data) == 0:
            break
    output_file.write(result)
print(f'Сжатая строка: {result}\n'
      f'Размер файла {os.path.getsize("../task4_output.txt")} байт')