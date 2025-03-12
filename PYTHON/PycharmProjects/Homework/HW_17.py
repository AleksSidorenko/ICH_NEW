# 1. Напишите программу, которая принимает список чисел от пользователя и
# передает его в функцию modify_list, которая изменяет элементы списка.
# Функция должна умножить нечетные числа на 2, а четные числа разделить на 2.
# Выведите измененный список на экран.
# Объясните, почему изменения происходят только внутри функции:
# (потому что внутри функции над списком выполняются определенные действия, он изменяется
# (т.к. он изменяем по определению) и появляется новый объект с другой ссылкой,
# где переменные l_numbers и numbers это ссылка на один и тот же объект, а
# num это ссылка уже на измененный объект)
# и как работают изменяемые (передаются в функции по ссылке и там значения меняются)
# и неизменяемые параметры (передаются в функции по значению (т.е. создается копия значения параметра).
# Пример вывода:
# Введите список чисел, разделенных пробелами: 1 2 3 4 5
# Измененный список чисел: [2, 1, 6, 2, 10]
# def modify_list(numbers):
#     num = [ round(number / 2) if number % 2 == 0 else number * 2 for number in numbers ]
#     return num
#
#
# l_numbers = list(map(int, input("Введите список чисел, разделенных пробелами: ").split()))
# print(modify_list(l_numbers))
#
# # Вариант 2:
# def modify_list():
#     l_numbers = input('Введите список чисел, разделенных пробелами: ').split()
#     num = [ round(int(num) / 2) if int(num) % 2 == 0 else int(num) * 2 for num in l_numbers ]
#     return num
#
#
# print(modify_list())

# 2. Напишите программу, которая принимает произвольное количество аргументов от пользователя и
# передает их в функцию calculate_sum, которая возвращает сумму всех аргументов.
# Используйте оператор * при передаче аргументов в функцию. Выведите результат на экран.
# Пример вывода:
# Введите числа, разделенные пробелами: 1 2 3 4 5
# Сумма чисел: 15
def calculate_sum(*args):
    i = 0
    for arg in args:
        for a in arg:
            i += int(a)
    return i

l_numbers = input("Введите список чисел, разделенных пробелами: ").split()
print(calculate_sum(l_numbers))

# Option 2
def calculate_sum(*args):
    s = [ a for arg in args for a in arg ]
    return sum(s)

l_numbers = list(map(int, input("Введите список чисел, разделенных пробелами: ").split()))
print(calculate_sum(l_numbers))

# Option 3
def calculate_sum(*args):
    s = [ int(a) for arg in args for a in arg ]
    return sum(s)

l_numbers = calculate_sum(input("Введите список чисел, разделенных пробелами: ").split())
print(l_numbers)

# Option 4
# def input_numb_list():
#     list_user_numbers = input('Enter a list of numbers separated by space: ').split()
#     # print(list_user_numbers)
#     numb_list = [int(x) for x in list_user_numbers]
#     return sum(numb_list)
#
# l1 = input_numb_list()
# print(l1)
# Рекурсия
#factorial(5)
#    factorial(4)
#        factorial(3)
#            factorial(2)
#                factorial(1)
#                    return 1
#                return 2 * 1 = 2
#            return 3 * 2 = 6
#        return 4 * 6 = 24
#    return 5 * 24 = 120