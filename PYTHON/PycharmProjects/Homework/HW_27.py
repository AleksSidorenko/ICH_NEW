# 1. Напишите функцию, которая принимает на вход список чисел
# и возвращает сумму квадратов только четных чисел из списка,
# используя функциональные подходы (например, map, filter и reduce).
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72

# def sum_squares(n):
#     # f = filter(lambda x: x % 2 == 0, n)
#     # sq = map(lambda x: x ** 2, f)
#     # return sum(sq)
#     return sum(map(lambda x: x ** 2, filter(lambda i: i % 2 == 0, n)))
#
# numbers = [4, 6, 3, 4, 2, 3, 9, 0, 7]
# print(f'Сумма квадратов четных чисел: {sum_squares(numbers)}')


# oder:
# from functools import reduce
#
# def sum_squares(n):
#     f = filter(lambda x: x % 2 == 0, n)
#     sq = map(lambda x: x ** 2, f)
#     return reduce(lambda x, y: x + y, sq)
#
# numbers = [4, 6, 3, 4, 2, 3, 9, 0, 7]
# print(f'Сумма квадратов четных чисел: {sum_squares(numbers)}')

# 2. Напишите функцию, которая принимает на вход список функций и значение,
# а затем применяет композицию этих функций к значению, возвращая конечный результат.
# Пример использования:
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]
# compose_functions(functions, 5) должно вывести 9

# from functools import reduce

# def compose_functions(functions, number):
#     for function in functions:
#         number = function(number)
#     return number
#     # return reduce(lambda x, y: y(x), functions, number)
#
#
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]
# print(f'Результат композиции функций: {compose_functions(functions, 5)}')

