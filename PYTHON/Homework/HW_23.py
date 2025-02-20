# 1. Напишите программу, которая генерирует и выводит квадраты чисел от 1 до N
# с использованием генераторного выражения. Реализуйте функцию generate_squares,
# которая принимает число N в качестве аргумента и использует генераторное выражение
# для генерации квадратов чисел. Затем выведите квадраты чисел на экран.
# Пример работы программы:
# 1
# 4
# 9
# 16
# 25

# def generate_squares(number):
#     squares = ( x ** 2 for x in range(1, number + 1) )
#     return squares
#
# num = int(input("Введите число: "))
# g_squares = generate_squares(num)
# for i in g_squares:
#     print(i, end=" ")

# 2. Напишите генератор, который будет генерировать бесконечную последовательность Фибоначчи.
# Каждый раз, когда генератор вызывается, он должен возвращать следующее число последовательности.
# Напишите программу, которая будет использовать этот генератор для вывода первых N чисел Фибоначчи.
# Пример вывода:
# Введите количество чисел Фибоначчи: 10
# Первые 10 чисел Фибоначчи:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# def generator_fibonacci(number):
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# num = int(input("Введите число: "))
# g_f = generator_fibonacci(num)
# print(f"Первые {num} чисел Фибоначчи:")
# for i in range(num):
#     print(next(g_f), end=" ")


# def generator_fibonacci(number):
#     a, b = 0, 1
#     for _ in range(number):
#         yield a
#         a, b = b, a + b
#
# num = int(input("Введите число: "))
# g_f = generator_fibonacci(num)
# print(f"Первые {num} чисел Фибоначчи:")
# for i in range(num):
#     print(next(g_f), end=" ")
