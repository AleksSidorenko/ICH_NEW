# set1 = {'5'}
# set2 = {'1', '2', '1', '4'}
# set3 = {1, 2, 3, 5}
# set3 = {5}
# print(set1.union(set2, set3))
# print(set1.union(set2))
# print(set1 | set2)
#
# print(set1.intersection(set2))
# print(set1 & set2)
# #
# print(set1.difference(set2))
# print(set1 - set2)
#
# print(set2 - set1)
# #
# print(set1.symmetric_difference(set2))
# print(set1 ^ set2)
#
# s = set1.issubset(set2)
# print(set1)
# if s is True:
#     print('T')
# else:
#     print('F')
# print(set1 <= set2)
#
# print(set1.issuperset(set2))
# print(set1 >= set2)

# Дан массив.
# Дать ответ на вопрос есть ли в нём два элемента с суммой ноль.
# ● Решить с двумя вложенными циклами
# ● Решить с помощью множеств

# l = [1, -8, -5, 4, 7, 3, -4, -1, 9]
# def check_pair_sumnull(mas):
#     new_mas = set()
#     for i in mas:
#         if -i in new_mas:
#             return True
#             new_mas.add(i)
#         return False
#
# result = (check_pair_sumnull(l))
# print(result)

# Напишите программу, которая принимает два списка и возвращает список, содержащий только
# уникальные элементы из обоих списков.
# Создайте функцию unique_elements, которая принимает два списка в качестве аргументов и
# возвращает список уникальных элементов. Используйте множества для фильтрации
# дубликатов. Выведите результат на экран.
# Примеры списков:
# {1, 2, 3, 4, 5}
# {4, 5, 6, 7, 8}
# Пример вывода:
# Уникальные элементы: {1, 2, 3, 4, 5, 6, 7, 8}

# list1 = ['3, 4, 5']
# list2 = ['4, 5, 6']
#
#
# print(set(list1 + list2))
# def get_uniq_elements(list1, list2):
#     return sorted(list(set(list1 + list2)))
#
#
# result = get_uniq_elements(list1, list2)
# print("Uniq data:", result)


# def deep_copy(list1):
#     res = []
#     for i in list1:
#         if isinstance(i, list):
#             res.append(deep_copy(i))
#         else:
#             res.append(i)
#
#     return res
# # Оригинальный список с вложенными списками
# original_list = [[1, 2, 3], 'Hi', 10, [4, 5, 6], [7, 8, 9]]
#
#
# # Глубокая копия списка с использованием нашей функции
# deep_copied_list = original_list.copy()
# deep_copied_list = deep_copy(original_list)
#
# # Изменим элемент в оригинальном списке
# original_list[0][0] = 99
#
# # Выводим результаты
# print("Оригинальный список:", original_list)
# print("Глубокая копия:", deep_copied_list)
#

my_set = {'a', 'b', 'c'}
for item in my_set:
    print(item, end=' ')
