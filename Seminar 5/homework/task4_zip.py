# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Запаковщик
import os.path

with open('task4_zip_input.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()[0]
print(f'Исходная строка: {input_data}\n'
      f'Размер файла {os.path.getsize("task4_zip_input.txt")} байт')

'vvvvvvvvvvsssssssssbbbbb'
with open('task4_output.txt', 'w', encoding='utf-8') as output_file:
    result = ''
    count = 0
    while True:
        for i in range(len(input_data)):
            if input_data[0] == input_data[i]:
                count += 1
            else:
                break
        while count > 0:
            result += f'{9 if count > 9 else count}{input_data[0]}'
            count -= 9
        input_data = input_data[count:]
        count = 0
        if len(input_data) == 0:
            break
    output_file.write(result)
print(f'Сжатая строка: {result}\n'
      f'Размер файла {os.path.getsize("task4_output.txt")} байт')
