# Всё херня!
import os.path

with open('task4_zip_input.txt', 'rb') as input_file:
    input_data = input_file.readlines()[0]
print(f'Исходная строка: {input_data}\n'
      f'Размер файла {os.path.getsize("task4_zip_input.txt")} байт')

with open('task4_output.txt', 'w', encoding='utf-8') as output_file:
    result = [[], []]
    count = 0
    while True:
        for i in range(len(input_data)):
            if input_data[0] == input_data[i]:
                count += 1
            else:
                break
        result[0].append(input_data[0])
        result[1].append(count)
        input_data = input_data[count:]
        count = 0
        if len(input_data) == 0:
            break
    output_file.write(f'{result}')
print(f'Сжатая строка: {result}\n'
      f'Размер файла {os.path.getsize("task4_output.txt")} байт')
