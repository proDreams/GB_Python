# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

result_list = []
for x in range(2):
    for y in range(2):
        for z in range(2):
            result_list.append(not(x or y or z) == (not x) and (not y) and (not z))
for i in result_list:
    if result_list[0] != i:
        print("Утверждение не верно")
        break
else:
    print("Утверждение верно")
