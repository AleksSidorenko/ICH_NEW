# 1. Напишите программу, которая запрашивает у пользователя строку и определяет, является ли она панграммой.
# Панграмма - это фраза, содержащая все буквы алфавита.
# Программа должна игнорировать регистр букв и пробелы при проверке панграммы.
# Выведите соответствующее сообщение на экран с помощью команды print.
# Решить задачу для латиницы.
#
# Пример вывода:
# Введите строку: The quick brown fox jumps over the lazy dog
# Строка является панграммой.

# string = input("Enter a string: ")
# decimal_str_up = 65                # 65 - 90 ASCII для заглавных латинских букв 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# decimal_str_down = 97              # 97 - 122 ASCII для прописных латинских букв ''
# pant = ''
# while chr(decimal_str_up) in string or chr(decimal_str_down) in string:
#         pant = pant + chr(decimal_str_up) if decimal_str_up < 91 else chr(decimal_str_down)
#         decimal_str_up += 1
#         decimal_str_down += 1
# if len(pant) == 26:
#     print(f"{string} is Pangram")
# else:
#     print(f"{string} is not Pangram")

# 2. Напишите программу, которая запрашивает у пользователя строку и выводит на экран количество гласных
# и согласных букв в ней. Используйте функцию len() для подсчета количества букв.
# Выведите результат на экран с помощью команды print.
# Решить задачу для латиницы.

# Вариант 1
# str = input("Enter a string: ")
# str_len = len(str)
# i = 0
# save_str = ''
# a_up = "AEIJOUY"
# a_down = "aeijouy"
# vow_let = 0
# while i < str_len:
#     save_str = save_str + str[i] if str[i] != " " else save_str
#     vow_let = (vow_let + 1) if (str[i] in a_up or str[i] in a_down) else vow_let
#     i += 1
# cons_let = len(save_str)-vow_let
# print(str_len)
# print(len(save_str))
# print(save_str)
# print(f'Количество \033[31m гласных\033[0m букв в строке {str}: \033[31m{vow_let}\033[0m')
# print(f'Количество \033[34m согласных\033[0m букв в строке {str}: \033[34m{cons_let}\033[0m')

# Вариант 2
# s = input("Enter a string: ")
# l = len(s)
# luck = 0
# i = 0
# a_up = "AEIJOUY"
# a_down = "aeijouy"
# g = 0
# while i < l:
#     if s[i] == ' ':
#         luck += 1
#     elif s[i] in a_up or s[i] in a_down:
#           g += 1
#     i = i + 1
# print(f'Количество \033[31m гласных\033[0m букв в строке {s}: \033[31m{g}\033[0m')
# print(f'Количество \033[34m согласных\033[0m букв в строке {s}: \033[34m{l-luck-g}\033[0m')


# s = input("Enter a string: ")
# l = len(s)
# i = 0
# s_s = ''
# while i < l:
#     s_s = s_s + s[i]
#     print(s_s)
#     i = i + 1

