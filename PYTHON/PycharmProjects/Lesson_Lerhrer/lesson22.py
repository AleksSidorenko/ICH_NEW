# x = 10 / 0
# print(x)

# try:
#     x = 10 / 0
#     print(x)
# except ZeroDivisionError:
#     print("Ошибка деления на ноль")

# print("--------")

# try:
#     x = int("abc")
#
# except ValueError:
#     print("Ошибка преобразования строки в число")
#     try:
#         [1, 2][5]
#     except IndexError:
#         print("IndexError")
# except IndexError:
#     print("Ошибка типа данных")
#
# print("Hi")


# try:
#     x = int("abc")
#     # 10 / 0
# except Exception:
#     print("Какая-то ошибка")
# except IndexError:
#     print("Ошибка преобразования строки в число")

# file = None
# try:
#    file = open("data.txt", "r")
#    file.read()
# except:
#    print("Запись не удалась")
# finally:
#    if file:
#       file.close()


# try:                                         # ERROR!
#     file = open("datsdfsfa.txt", "r")
#     file.read()
# except:
#     print("Запись не удалась.")
# finally:
#     file.close()
#

# print("-------")
# try:
#    x = 10 / 0
# except ZeroDivisionError:
#    print("Ошибка деления на ноль")
# else:
#    print("Результат:", x) # Выводит "Результат: 5.0"
#

# def func():
#    try:
#        10 / 0
#    except ZeroDivisionError:
#        print("Error")
#        return
#    finally:
#        print("finally")
#        print("End")
#
# func()
# print("----")
#
#
# def divide(x, y):
#    if y < 0:
#       raise ValueError("Не работаем с отрицательными")
#    return x / y
#
# print(divide(6, -3))


# file = None
# try:
#    file = open("file1.txt")
# except FileNotFoundError as e:
#    print(e)
# else:
#    data = file.readlines()
#    try:
#       for el in data:
#          int(el[3])
#    except ValueError as e:
#       print(e)
# finally:
#    if file:
#       file.close()
