# 1. Напишите декоратор validate_args,
# который будет проверять типы аргументов функции и выводить сообщение об ошибке,
# если переданы аргументы неправильного типа.
# Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.
# Пример использования:
# @validate_args(int, str)
# def greet(age, name):
#     print(f"Привет, {name}! Тебе {age} лет.")
#
# greet(25, "Анна")  # Все аргументы имеют правильные типы
# greet("25", "Анна")  # Возникнет исключение TypeError
# Ожидаемый вывод:
# Привет, Анна! Тебе 25 лет.
# TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.

# print("😊🔥💻")  # 😊🔥💻
# print("Привет, мир! 🚀")
# print( "👍", '😄')


# def validate_args(*typenames):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             cnt = 0
#             for i, c_type in zip(args, typenames):
#                 try:
#                     if not isinstance(i, c_type):
#                         cnt += 1
#                         raise TypeError(f'Аргумент {i} имеет неправильный тип \033[31m{type(i)}\033[0m.'
#                                         f'Ожидается \033[34m{c_type}\033[0m.')
#                 except TypeError as e:
#                         print(e)
#             if cnt == 0:
#                 return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @validate_args(int, str, str, int, float)
# def greet(age, name, city, height, weight):
#     print(f"Привет, {name}!\n"
#           f"Тебе {age} лет.\n"
#           f"Ты из города: {city}.\n"
#           f"Твой рост: {height} см.\n"
#           f"Твой вес: {weight} кг.\n"
#           f"Ты в хорошей форме!😊")
#
# greet(25, "Анна", "London", 170, 63.5)
# print('-----------------')
# greet('25', "Анна", 23, 120, 100)

# 2. Напишите декоратор log_args,
# который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>,
# Результат: <результат>". Используйте модуль logging для записи в лог-файл.
# Пример использования:
# @log_args
# def add(a, b):
#     return a + b
#
# add(2, 3)
# add(5, 7)
# Ожидаемый вывод в файле log.txt:
# Аргументы: 2, 3, Результат: 5
# Аргументы: 5, 7, Результат: 12
# Убедитесь, что перед запуском кода у вас создан файл log.txt в той же директории,
# где находится скрипт Python.

# def log_args(func):
#     def wrapper(*args, **kwargs):
#         with open("log.txt", 'w') as f:
#             result = func(*args, **kwargs)
#             f.write(f"Аргументы: {args}, {kwargs} Результат: {result}")
#         with open(f"log.txt", 'r') as f:
#             print(f.read())
#     return wrapper
#
# @log_args
# def add(a, b):
#     return a + b
#
# add(2, 3)
# add(a=5, b=7)

# GPT
# import logging
# # import functools
#
# # Настройка логгера
# logging.basicConfig(
#     filename="log.txt",      # Файл, куда будут записываться логи
#     level=logging.INFO,      # Уровень логирования (INFO – только важная информация)
#     format="%(asctime)s - %(message)s",  # Формат записи (включает дату и сообщение)
#     encoding="utf-8"         # Кодировка файла (чтобы не было проблем с русскими символами)
# )
# def log_args(func):
#     # @functools.wraps(func)  # Сохраняем имя и документацию оригинальной функции
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)  # Вызываем оригинальную функцию
#         args_str = ", ".join(map(str, args)) if args else "нет"
#         kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else "нет"
#         log_message = f"Аргументы: {args_str}, kwargs: {kwargs_str}, Результат: {result}"
#         logging.info(log_message)
#         return result
#     return wrapper
#
#
# @log_args
# def add(a, b):
#     return a + b
#
# # Тестовые вызовы
# add(2, 3)
# add(a=5, b=7)