# 1. Написать программу, вычисляющую факториал числа.
# Решить задачу с помощью рекурсии.
# def factorial(n):
#     return n * factorial(n - 1) if n > 1 else n
#
# num = int(input("Введите положительное число: "))
# print(f"Факториал исла: {num} = {'Введено отрицательное число' if num < 0 else 1 if num in (0, 1) else factorial(num)}")

# 2. Напишите программу, которая использует рекурсию для вычисления суммы цифр числа.
# Создайте функцию sum_digits, которая принимает один аргумент - число,
# для которого нужно вычислить сумму цифр.
# Используйте условие выхода из рекурсии, когда число состоит из одной цифры.
# Выведите результат на экран.
# Пример вывода:
# Введите число: 12345
# Сумма цифр числа 12345 равна 15

# def sum_digits(number):
#     return number if number < 10 else number % 10 + sum_digits(number // 10)
#
# num = int(input("Введите число: "))
# print(f"Сумма цифр числа: {num} = {sum_digits(num)}")

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)

# your_number = [1, 2, 3, 4, 5]
# # your_number = input("Введите числа через пробел: ")
# # your_number = [int(x) for x in your_number.split()]
# calculate_sum = lambda *your_number: sum(your_number)
#
# print("Сумма чисел:",calculate_sum(*your_number))