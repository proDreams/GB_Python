# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import time

def check_prime(number, lst):
    if number in lst:
        return True
    for j in range(2, number // 2):
        if number % j == 0:
            return False
    else:
        if number not in lst:
            lst.append(number)
        return True



numb = int(input("Введите число: "))
start = time.time()
prime_set = []
div = 2
num = numb
while num != 1:
    if num % div == 0:
        if check_prime(div, prime_set):
            num //= div
        else:
            div += 1
    else:
        div += 1
print(f"Число {numb} имеет следующие простые множители: {prime_set}")
end = time.time() 
print(end - start)