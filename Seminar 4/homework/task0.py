# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Привет Дарье Лютовой ;)
names, hobbies = open('task0_name.txt', 'r', encoding='utf-8'), open('task0_hobby.txt', 'r', encoding='utf-8')
dictionary = {i.rstrip(): j.rstrip() for (i, j) in zip(names, hobbies)}
print(dictionary)
names.close(), hobbies.close()
