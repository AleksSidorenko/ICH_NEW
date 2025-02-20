# 1. Напишите программу, которая открывает файл, считывает из него два числа
#    и выполняет операцию их деления.
#    Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
#    Обработайте исключение и выведите соответствующее сообщение.

# try:
#     with open("data_HW_22.txt") as file:
#         a, b = map(int, file.readline().split())
#         if a < 0 or b < 0:
#             raise ValueError("Число должно быть положительным")
#         res = a / b
#         print("Результат деления:", res)
# finally:
#     print("Процесс завершен")


# Option через функцию
# def read_and_divide(filename):
#     try:
#         with open(filename, 'r') as file:
#             # Считываем два числа
#             a, b = map(int, file.readline().split())
#
#             # Проверяем на отрицательность
#             if a < 0 or b < 0:
#                 raise ValueError("Число должно быть положительным")
#
#             # Выполняем деление
#             result = a / b
#             print(f"Результат деления: {result}")
#
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#     except ZeroDivisionError:
#         print("Ошибка: Деление на ноль невозможно")
#     except FileNotFoundError:
#         print("Ошибка: Файл не найден")
#     except Exception as e:
#         print(f"Непредвиденная ошибка: {e}")
#
# # Пример вызова функции
# read_and_divide("data_HW_22.txt")


# 2. Напишите программу, которая открывает файл, считывает его содержимое
#    и выполняет операции над числами в файле.
#    Обработайте возможные исключения при открытии файла (FileNotFoundError)
#    и при выполнении операций над числами (ValueError, ZeroDivisionError).
#    Используйте конструкцию try-except-finally для обработки исключений
#    и закрытия файла в блоке finally.

# try:
#     file = open("data_HW_22.txt")
# except FileNotFoundError as e:
#         print(f"Ошибка: Файл не найден {e}")
# else:
#     try:
#         # d = []
#         # for num in file.readline().split():
#         #     d = d + [int(num)]
#         d = [ int(i) for i in file.readline().split() ]
#         print(f"Результат деления: {d[0] / d[1]}")
#     except ValueError as e:
#         print(f"Ошибка: Некорректные данные в файле: {e}")
#     except ZeroDivisionError:
#         print("Делить на ноль нельзя")
#     finally:
#         file.close()
#         print("Процесс завершен")