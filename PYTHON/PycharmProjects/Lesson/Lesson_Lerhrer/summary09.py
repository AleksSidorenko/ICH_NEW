# from copy import deepcopy
#
# original_list = [[1, 2, [3]], [4, 5, 6], [7, 8, 9], 10]
# new_list = deepcopy(original_list)
# print(original_list is new_list)
# new_list[0].append(99)
# print(new_list)
# print(original_list)


# original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 10]
# new_list = original_list.copy()
# # [link1, link2, link3, 10]
new_list = [i for i in original_list]
# print(original_list)
# print(new_list)
# # new_list2 = original_list
# print(original_list == new_list)
# print(original_list is new_list)
# # print(original_list is new_list2)
# # print(id(original_list))
# # print(id(new_list))
# new_list[0].append(99)
# # new_list.append("Hi")
# print(new_list)
# print(original_list)
# #
# new_list2 = [i for i in original_list]

# # Алгоритм глубокого копирования списка с вложенными списками
# def deep_copy(lst):
#     # Создаем новый список, в который будем копировать элементы
#     new_lst = []
#
#     for item in lst:
#         # Если элемент является списком, копируем его рекурсивно
#         if isinstance(item, list):
#             new_lst.append(deep_copy(item))
#         else:
#             # Если элемент не является списком, просто добавляем его
#             new_lst.append(item)
#
#     return new_lst
