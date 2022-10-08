# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
# result_list = []
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             result_list.append(not (x or y or z) == (not x and not y and not z))
# for i in result_list:
#     if result_list[0] != i:
#         print("Утверждение не верно")
#         break
# else:
#     print("Утверждение верно")


# print('Утверждение верно' if not (0 or 0 or 0) == (not 0 and not 0 and not 0) else 'Утверждение не верно')

# Второй очень страшный и ни разу не изящный в одну строку
print(*[f'x = {x}, y = {y}, z = {z} = Утверждение верно' if not (x or y or z) ==
        (not x and not y and not z) else 'Утверждение не верно' for z in range(2) for y in range(2) for x in range(2)]
      , sep='\n')
