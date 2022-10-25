# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Распаковщик
import os.path

with open('task4_zip_input.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()[0]
print(f'Исходная строка: {input_data}\n'
      f'Размер файла {os.path.getsize("task4_zip_input.txt")} байт')