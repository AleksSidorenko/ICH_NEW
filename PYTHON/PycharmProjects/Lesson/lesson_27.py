# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14 × 10 в
# соответствии с образцом. Для вывода прямоугольника используйте цикл for.
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********
# def draw_box():
#     w = 10
#     h = 14
#     for i in range(h):
#         if i == 0 or i == h-1:
#             print('*' * w)
#         else:
#             print('*' + ' ' * (w -2) + '*')
#
#
# draw_box()
#########################
# Напишите программу, выводящую следующий список:
# ;['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Option 1
# def generet_list():
#     result = []
#     i = 0
#     while i < 26:
#         result.append(chr(ord('a') + i) * (i + 1))
#         i += 1
#     return result
#
#
# print(generet_list())
# letter = chr(ord('a') + i)  # Получаем букву, начиная с 'a'

# Option 2
# def generate_list():
#     result = []
#     for i in range (26):
#         result.append(chr(ord('a') + i) * (i + 1))
#     return result
#
# print(generate_list())
###########################
# Напишите программу, которая принимает два числа и возвращает их сумму и произведение
# в виде кортежа (sum, product). Используйте функцию для вычисления суммы и
# произведения. Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите первое число: 3
# Введите второе число: 4
# Сумма и произведение чисел: (7, 12)
# def sumAndProduct(a, b):
#     summ = a + b
#     prod = a * b
#     return summ, prod
#
# result = sumAndProduct(3, 5)
# print(f"Сумма и произведение чисел: {result}")
# Option 2
# def sumAndProduct(a, b):
#     summ = a + b
#     prod = a * b
#     return summ, prod
#
# result = sumAndProduct(3, 5)
# print(f"Сумма и произведение чисел: ({result[0]}, {result[1]})")
# Option 3
# def sumAndProduct(numbers) :
#     sum_result = sum(numbers)
#     p = 1
#     for nam in numbers :
#         p = p*nam
#     return sum_result,p
#
#
# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# result = sumAndProduct(numbers)
# n1,n2,n3 = map(int,input('Введите 2 числа через пробел ').split())
# result = sumAndProduct([n1,n2,n3])
# print(result)
#####################













