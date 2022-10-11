# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

fst_str, snd_str = input("Введите первую строку:"), input("Введите вторую строку:")
if fst_str in snd_str or snd_str in fst_str:
    print(f"Строка {fst_str} входит в строку {snd_str} - {snd_str.count(fst_str)} раз")
    print(f"Строка {snd_str} входит в строку {fst_str} - {fst_str.count(snd_str)} раз")