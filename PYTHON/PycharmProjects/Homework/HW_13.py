# 1. Напишите программу, которая принимает два числа и возвращает их сумму и
# произведение в виде кортежа (sum, product).
# Используйте функцию для вычисления суммы и произведения.
# Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите первое число: 3
# Введите второе число: 4
# Сумма и произведение чисел: (7, 12)
# def f_sum(x, y):      # или можно записать в одну строку: def f_sum(x, y): return x + y
#     return x + y
#
# def f_product(x, y):  # или можно записать в одну строку: def f_product(x, y): return x * y
#     return x * y
#
#
# n1 = int(input("Введите первое число: "))
# n2 = int(input("Введите второе число: "))
# print("Сумма и произведение чисел: ", (f_sum(n1, n2), f_product(n1, n2)))
##################################################
# 2. Напишите программу, которая принимает список чисел и возвращает сумму,
# минимальное и максимальное значение из списка.
# Используйте функцию для обработки списка чисел и возврата трех значений.
# Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите числа:  3, 7, 2, 9, 1, 5
# Сумма чисел: 27
# Минимальное значение: 1
# Максимальное значение: 9
# def f_proc(l_num):
#     p = print(f'Сумма чисел: {sum(l_num)} \nМинимальное значение: {min(l_num)} \nМаксимальное значение: {max(l_num)}')
#     return p
#
#
# list_numbers = list(map(int, input("Введите числа через запятую: ").split(",")))
# f_proc(list_numbers)
###################
# Функция также может принимать переменное количество позиционных аргументов, тогда перед именем ставится *:
# def func(*args): # args - это кортеж из всех переданных аргументов функции, и с переменной можно работать также, как и с кортежем.
#     return args
#
# print(func(9, 11, 'abc'))
#############
# Функция может принимать и произвольное число именованных аргументов, тогда перед именем ставится **:
# def func(**kwargs): # В переменной kwargs у нас хранится словарь, с которым мы, опять-таки, можем делать все, что нам заблагорассудится.
#     return kwargs
#
# print(func(a=1, b=2, c=3)) # {'a': 1, 'b': 2, 'c': 3}
# print(func(a='python'))    # {'a': 'python'}
#############
# Функция может и не заканчиваться инструкцией return, при этом функция вернет значение None:
# def func():
#     pass
#
# print(func())  # None
#####################
# Функция может быть любой сложности и возвращать любые объекты (списки, кортежи, и даже функции!):
# def newfunc(n):
#     def myfunc(x):
#         return x + n
#     return myfunc
#
# new = newfunc(100)  # new - это функция
# new(200) # 300
################
# Анонимные функции могут содержать лишь одно выражение, но и выполняются они быстрее.
# Анонимные функции создаются с помощью инструкции lambda. Кроме этого,
# их не обязательно присваивать переменной, как делали мы инструкцией def func():
# func = lambda x, y: x + y
# print(func(1, 2)) # 3
#
# print(func('a', 'b')) # 'ab'
# print((lambda x, y: x + y)(1, 2)) # 3
# print((lambda x, y: x + y)('a', 'b')) # 'ab'
#
# # lambda функции, в отличие от обычной, не требуется инструкция return,
# # а в остальном, ведет себя точно так же:
# func = lambda *args: args
# print(func(1, 2, 3, 4)) # (1, 2, 3, 4)
#####################
# Функцию можно записать в одну строку, если блок инструкций представляет собой простое выражение:
#
# def sum(a, b): return a + b
# Функции могут быть вложенными:
#
# def func1(a, b):
#
#     def inner_func(x):
#         return x*x*x
#
#     return inner_func(a) + inner_func(b)
# Функции — это объекты, поэтому их можно присваивать переменным.
##################
# def stats(data):
#     """данные должны быть списком"""
#     _sum = sum(data) # обратите внимание на подчеркивание, чтобы избежать переименования встроенной функции sum
#     mean = _sum / float(len(data)) # обратите внимание на использование функции float, чтобы избежать деления на целое число
#     variance = sum([(x-mean)**2/len(data) for x in data])
#     return mean,variance   # возвращаем x,y — кортеж!
#
# m, v = stats([1, 2, 1])



