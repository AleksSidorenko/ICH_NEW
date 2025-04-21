# Не декоратор
# def decorator(func):
#     print("Сейчас выполним функцию")
#     func()
#     print("Функция выполнена")

# def decorator(func):
#     def wrapper():
#         print("Сейчас выполним функцию")
#         func()
#         print("Функция выполнена\n")
#
#     return wrapper
#
#
# @decorator
# def my_function():
#     print("my_function")
#
#
# @decorator
# def my_another_function():
#     print("my_another_function")


# # result = decorator(my_function)
# # print(result)
# # result()
# # my_function = decorator(my_function)  # @decorator
# print(my_function)
# my_function()
# my_function()
#
# my_another_function()


#
# def uppercase_decorator(function):
#     def wrapper(*args, **kwargs):
#         func = function(*args, **kwargs)
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
#
# @uppercase_decorator
# def return_hello():
#     return "hello"
#
# @uppercase_decorator
# def return_person(person):
#     return f"Hello, {person}"
#
# print(return_hello())
# print(return_person("Bob"))


# def ask_name(ask_name):
#     def decorator(func):
#         def wrapper():
#             if ask_name:
#                 name = input("Как вас зовут? ")
#             result = func()
#             if ask_name:
#                 print(f"Ваше имя {name}, ваш возраст - {result}")
#             else:
#                 print(f"Ваш возраст - {result}")
#         return wrapper
#     return decorator
#
#
# # @ask_name(True)
# @ask_name(False)
# def ask_age():
#     age = input("Сколько вам лет? ")
#     if age.isdigit():
#         return age
#     return "неизвестно"
#
#
# # print(ask_age())
# ask_age()
#
#

# import functools
#
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper():
#         print(f"documentation: :")
#         print(func.__doc__)
#         print(f"Сейчас выполним функцию '{func.__name__}':")
#         func()
#         print("Функция выполнена\n")
#
#     return wrapper
#
#
# @decorator
# def my_function():
#     """
#     my_function documentation
#     """
#     print("my_function")
#
# print(my_function)
# my_function()
# print("----------------")
#
# print(f"documentation: :")
# print(my_function.__doc__)
# print(f"Сейчас выполним функцию '{my_function.__name__}':")



def border_decorator(func):
    def wrapper():
        print("*" * 100)  # Верхняя граница
        func()
        print("*" * 100)  # Нижняя граница
    return wrapper

def repeat_decorator(func):
    def wrapper():
        for _ in range(3):  # Повторяем вызов трижды
            func()
    return wrapper

@border_decorator  # Применяется вторым
@repeat_decorator  # Применяется первым
def print_line():
    print("-" * 100)

print_line()

