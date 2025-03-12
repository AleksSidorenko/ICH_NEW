# Для заданного целого числа N подсчитать количество четных чисел, меньше или равных N.
# Вариант 1
# N=int(input('Enter the number: '))
# count = 0
# i = 1
#№ str_even = ''
# while i <= N:
#     if i % 2 == 0:
#         count += 1
#         str_even += str(i) + ' '  # i целое число и этой строкой мы переводим его в строку
#     i += 1
# print(count)
# print(str_even)
# Вариант 2
# n = int(input("enter a number"))
# counter = 0
# while n > 0:
#     if n % 2 == 0:
#         counter += 1
#     n -= 1
# print(counter)

# Вычислите n-е число ряда Фибоначчи с помощью цикла while. Что такое числа Фибоначчи?
# x = int(input("Enter a number: "))
# fib1 = 0
# fib2 = 1
# count = 1
# while count < x:
#     # print(fib1, end=' ')
#     fib1, fib2 = (fib2, fib1 + fib2)
#     count += 1
# print(f'\nNumber {x} Fibonacci number: {fib1}')

# По данному натуральному числу N найдите наибольшую целую степень двойки,
# не превосходящую N. Выведите показатель степени и саму степень.
# n = int(input("Enter a number: "))
# count = 0 # степень = 0
# i = 1 # 2 ** 0 = 1
# while i <= n:
#     count += 1
#     i = 2 ** count
# print(f'Показатель степени: {count-1}')
# print(f'степень двойки, не превосходящую N: {2**(count-1)}')

# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.




