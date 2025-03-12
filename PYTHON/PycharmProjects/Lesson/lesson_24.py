# file_path = input("Введите полный путь к файлу: ") # 'C:\Documents\Files\Hello.txt'
# with open(file_path, 'r', encoding='cp1251') as file:
#     content = file.read()
#     print(content)
###########################################
# with open('example.txt', 'a+', encoding='cp1251') as file:
#     file.write("\nAppending new text.")
#     file.seek(0)
#     content = file.read()
#     print(content)
###########################################
def greeting():
    print("Hello, world!")


# greeting()
###########################################
def sendmail():
    text = "Please, explain how the function works?"
    print(text)


# sendmail()
###########################################
def sendmail(from_name, age): # параметры функции
    text = "Please, explain how the function works?"
    print(f'My name is: {from_name}, \n My age is: {age} \n {text}')


# sendmail(from_name='Alex', age=24) # аргументы функции
###########################################
def send_mail():
    text = "Hello World"
    return text


# print(send_mail())
###########################################
def get_sq(number):
    result = number ** 2
    return result


# a = get_sq(5)
# print(a)
# print(get_sq(int(input("Enter a number: "))))
###########################################
# def a():
#     print("Start of function a")
#     b()
#     print("End of function a")
#
#
# def b():
#     print("Start of function b")
#     c()
#     print("End of function b")
#
#
# def c():
#     print("Start of function c")
#     print("End of function c")
#
#
# a()
###########################################
# def function_a():
#     print("Inside function A")
#     function_b()
#
# def function_b():
#     print("Inside function B")
#
#
# function_a()
#
# Как это работает:
# Когда вызывается function_a(), она помещается в стек вызовов.
# Внутри function_a происходит вызов function_b(), поэтому она тоже добавляется в стек вызовов.
# Когда function_b() завершает выполнение, она удаляется из стека.
# Управление возвращается в function_a, и она также завершает выполнение, после чего удаляется из стека.
# Стек вызовов в данном случае выглядит так:
#
# Когда запускается function_a(), стек:
# [function_a()]
# После вызова function_b() внутри function_a, стек:
# [function_a(), function_b()]
# После завершения function_b(), стек:
# [function_a()]
# После завершения function_a(), стек пуст.
###########################################
# def add(x, y):
#     result = x + y  # 'result' — локальная переменная
#     print(f"Result: {result}")
#     return result
#
#
# def main():
#     d = 100
#     be = 209
#     add(d, be)
#
#
# main()
# # Объяснение:
# #
# # При вызове main() создаётся фрейм для функции main.
# # В этом фрейме хранятся локальные переменные a и b.
# # При вызове add(a, b) создаётся новый фрейм для функции add.
# # В этом фрейме хранятся локальные переменные x, y и result.
# # После завершения add, её фрейм удаляется из стека, и result исчезает.
# # После завершения main, её фрейм тоже удаляется.
###########################################
# global_var = 10
#
#
# def example_function():
#     # Локальная переменная
#     local_var = 5
#     print("Локальная переменная:", local_var)  # Доступ к локальной переменной
#     print("Глобальная переменная:", global_var)  # Доступ к глобальной переменной
#
#
# def modify_global():
#     global global_var  # Указываем, что будем изменять глобальную переменную
#     global_var = 20
#     print("Глобальная переменная изменена на:", global_var)


# Основной код
# print("Глобальная переменная до вызова функций:", global_var)
# example_function()  # Вызов функции с локальной переменной
# modify_global()  # Изменение глобальной переменной
# print("Глобальная переменная после вызова функций:", global_var)
###########################################
# Python использует правило LEGB (Local, Enclosing, Global, Built-in) для поиска имени:
# Local (локальное): Поиск имени сначала происходит в локальном пространстве имён.
# Enclosing (замыкающее): Если локальное пространство отсутствует, поиск продолжается в замыкающем пространстве (например, в функции, которая содержит текущую функцию).
# Global (глобальное): Если имя не найдено в локальном и замыкающем пространстве, поиск продолжается в глобальном.
# Built-in (встроенное): Если имя отсутствует во всех вышеуказанных пространствах, Python проверяет встроенное пространство имён.
###########################################
# x = "global"
#
#
# def outer_function():
#     x = "enclosing"
#
#     def inner_function():
#         x = "local"
#         print(x)  # Вывод: local
#
#     inner_function()
#
#
# outer_function()
###########################################
# Перепишите решение следующей задачи с использованием функции.
# У нас есть две логические переменные: isWeekday, isVacation (выходной день и каникулы).
# Они могут принимать разные значения,
# всего 4 комбинации: true - true, true - false, false - false, false - true.
# Есть правило: мы можем поспать, если день не рабочий или мы на каникулах.
# Напишите программу, которая в зависимости от значений двух переменных печатает, можем ли мы поспать или нет.
# То есть для значений isWeekday = False и isVacation = False программа должна печатать “можете поспать”.
# def Weekdaying(isWeekday, isVacation):
#     '''Определяет, можем ли мы поспать.
#     Если день не рабочий (is_weekday == False) или мы на каникулах (is_vacation == True),
#     возвращает 'можете поспать', иначе 'не можете поспать'. """'''
#     if not isWeekday or isVacation:
#         return 'You can sleep'
#     else:
#         return 'You can work'
# day_weekday = input("Print the day: ").strip().lower() == 'true'
# vacation_weekday = input("Print the vacation: ").strip().lower() =='true'
#
#
# result = Weekdaying(day_weekday, vacation_weekday)
# print(result)
###########################################
# Написать функция для определения большего числа
# def comparison_number(number1, number2):
#     if number1 < number2:
#         return f'{number1} is less than {number2}'
#     elif number1 > number2:
#         return f'{number1} is greater than {number2}'
#     else:
#         return f'{number1} is equal to {number2}'
#
#
# input_number1 = int(input('Print an integer Number1: '))
# input_number2 = int(input('Print an integer Number2: '))
#
# print(comparison_number(input_number1, input_number2))
###########################################
# Даны два целых числа A и B (при этом A ≤ B).
# Напишите функцию, которая печатает все числа от A до B включительно.
# def print_numbers(a, b):
#     for i in range(int(a), int(b) + 1):
#         print(i)
#
# a, b = input("Введите 2 числа через пробел: ").split()
# # a, b = int(a), int(b) # без указания int выдаёт ошибку
# print_numbers(a, b)
#
# Option 2
# print(list(range(int(a), int(b) + 1)))

# Напишите функцию, которая возвращает факториал заданного числа.
# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
# По данному натуральному n вычислите значение n!.
# Пользоваться математической библиотекой math в этой задаче запрещено.
# Во всех задачах считывайте входные данные через input() и выводите ответ через print().

