# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
num_a, num_b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
lcm = max(num_a, num_b)
while True:
    if lcm % num_a == 0 and lcm % num_b == 0:
        print(lcm)
        break
    lcm += 1

# num_a, num_b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
# prime_a = [i for i in range(2, num_a + 1) if num_a % i == 0]
# prime_b = [i for i in range(2, num_b + 1) if num_b % i == 0]
# print(prime_a, prime_b, sep='\n')
#
#
# # ...
# def calculate_lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
#
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("The L.C.M. of", num1, "and", num2, "is", calculate_lcm(num1, num2))
