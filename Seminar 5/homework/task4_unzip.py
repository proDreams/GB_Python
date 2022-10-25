# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Распаковщик
import os.path

with open('task4_output.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()[0]


with open('task4_unzip_output.txt', 'w', encoding='utf-8') as output_file:
    result = ''
    for i in range(0, len(input_data), 2):
        result += input_data[i + 1] * int(input_data[i])
    output_file.write(result)

print(f'Сжатая строка: {input_data}\n'
      f'Размер файла {os.path.getsize("task4_output.txt")} байт\n'
      f'Восстановленная строка: {result}\n'
      f'Размер файла {os.path.getsize("task4_unzip_output.txt")} байт')
with open('task4_zip_input.txt', 'r', encoding='utf-8') as original_file:
    original_data = original_file.readlines()[0]
    print(f'Исходная строка: {original_data}\n'
      f'Размер файла {os.path.getsize("task4_zip_input.txt")} байт')