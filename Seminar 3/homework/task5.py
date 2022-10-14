# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

# Вариант вычисления двух веток и соединение их
def fibonacci(fib, start, pos):
    result = start
    if fib == 0 or fib == 1:
        return 0
    if pos == '+':
        for i in range(2, fib):
            result.append(result[i - 2] + result[i - 1])
    elif pos == '-':
        for i in range(2, fib):
            result.append(result[i - 2] - result[i - 1])
    return result


fib_num = int(input("Введите число: "))
fib_list = [0]
fib_list = fibonacci(fib_num, [1, -1], '-')[::-1] + fib_list
fib_list = fib_list + fibonacci(fib_num, [1, 1], '+')
print(fib_list)


# Вариант с вычислением почти-что на лету
def fibonacci(fib, start):
    result1 = start
    result2 = result1.copy()[:0:-1]
    for i in range(2, fib):
        if i % 2 == 0:
            result1.append(result1[i - 2] + result1[i - 1])
            result2.insert(0, -result1[i])
        else:
            result1.append(result1[i - 2] + result1[i - 1])
            result2.insert(0, result1[i])
    return result2 + result1


fib_num = int(input("Введите число: "))
fib_list = [0, 1]
fib_list = fibonacci(fib_num, fib_list)
print(fib_list)
