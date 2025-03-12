# 1. Напишите функцию merge_dicts,
# которая принимает произвольное количество словарей в качестве аргументов
# и возвращает новый словарь, объединяющий все входные словари.
# Если ключи повторяются, значения должны быть объединены в список.
# Функция должна использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.
# Пример ввода:
# {'a': 1, 'b': 2}
# {'b': 3, 'c': 4}
# {'c': 5, 'd': 6}
# Пример вывода:
# {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}

# def merge_dicts(*c):
#     k = {}
#     for i in c:
#         for key, value in i.items():
#             if key in k:
#                 k[key].append(value)
#             else:
#                 k[key] = [value]
#     return k

# def merge_dicts(*kwargs):
#     new_dict = {}
#     for para in kwargs:
#         for key, value in para.items():
#             if new_dict.get(key) is None:
#                 new_dict[key] = [value]
#             else:
#                 new_dict[key].append(value)
#     return new_dict
#
# Не
# def merge_dicts(*kwargs):
#     new_dict = {}
#     # d = { new_dict.update(para) for para in kwargs }
#     for para in kwargs:
#         for key, value in para.items():
#             if key not in new_dict:
#                 # para.update({key: value})
#                 new_dict.update(para)
#             else:
#                 if type([value]):
#                     new_dict[key].extend(value)
#                     # new_dict[key] = [value]
#                 else:
#                     new_dict[key].append(value)
#                     # para.update({key: value})
#                     # new_dict[key].extend(value)
#
#     return new_dict


# dic1 = {'a': 1, 'b': 2}
# dic2 = {'b': 3, 'c': 4}
# dic3 = {'c': 5, 'd': 6}
# print(merge_dicts(dic1, dic2, dic3))

# 2. Напишите программу, которая принимает строку от пользователя
# и подсчитывает количество уникальных символов в этой строке.
# Создайте функцию count_unique_chars,
# которая принимает строку и возвращает количество уникальных символов.
# Выведите результат на экран.
# Пример вывода:
# Введите строку: hello
# Количество уникальных символов: 4

# def count_unique_chars(string):
#     return len(set(s.replace(' ', '').replace(',', '').replace('.', '')))
#
#
# s = "hello world"
# print(count_unique_chars(s))

# 3. Напишите программу, которая создает словарь,
# содержащий информацию о студентах и их оценках.
# Ключами словаря являются имена студентов,
# а значениями - списки оценок.
# Создайте функцию calculate_average_grade,
# которая принимает словарь с оценками студентов
# и вычисляет средний балл для каждого студента.
# Функция должна возвращать новый словарь,
# в котором ключами являются имена студентов, а значениями - их средний балл.
# Выведите результат на экран.
# Пример словаря с оценками
# grades = {
#     'Alice': [85, 90, 92],
#     'Bob': [78, 80, 84],
#     'Carol': [92, 88, 95]
# }
# Пример вывода:
# {'Alice': 89.0, 'Bob': 80.66666666666667, 'Carol': 91.66666666666667}

# def calculate_average_grade(x):
#     k = {}
#     for key, value in x.items():
#         k[key] = sum(value) / len(value)
#     return k
#
# grades = {'Alice': [85, 90, 92], 'Bob': [78, 80,84], 'Carol': [92, 88, 95]}
# print(calculate_average_grade(grades))

# def calculate_average_grade(dict_note):
#     return { key: round(sum(value) / len(dict_note), 2) for key, value in dict_note.items() }
#
#
# grades = {'Alice': [85, 90, 92],
#           'Bob': [78, 80, 84],
#           'Carol': [92, 88, 95]}
# print(calculate_average_grade(grades))