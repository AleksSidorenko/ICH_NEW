# print(hash("hello"))
# print(hash("hello"))
# print(hash(100))


# print(hash(1))
# print(hash(True))
# # 1
# print(hash(1.0))
# # 1
# print(hash('1'))
# # -3723884734378080930
# print(hash('строка'))
# # -295037195106125010
# print(hash((1,2,3)))
# # 2528502973977326415

#
# s = {"hello", "python", "hi", True, 1, 1.0}
# print(s)
#
# #
# # s1 = {1, 5}
# # s2 = {1, 5, 6}
#
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# intersection = set1.intersection(set2)
# union = set1.union(set2)
# difference = set1.difference(set2)
# symmetric_difference = set1.symmetric_difference(set2)
# print(intersection) # Выводит {2, 3}
# print(union) # Выводит {1, 2, 3, 4}
# print(difference) # Выводит {1}
# print(symmetric_difference) # Выводит {1, 4}
#
# text = "python"
# text += "!"
# print(text[0])
# # text[0] = "P"


# set_nums = {2, 3, (1, 2, [6, 7])}
# print(hash((6, 7)))


# set_nums = {2, {3}, 4}
# print(type(set_nums))
# print({3} in set_nums)
#

# my_set = {1, 2, 3}
# empty_set = set()
# print(len(my_set)) # Выводит размер множества
# print(2 in my_set) # Выводит True, так как элемент 2 содержится во множестве


# my_set = {'1', '2', '3'}
# my_set.add(4) # {1, 2, 3, 4}
# print(my_set) # Выводит пустое множество
# # my_set.remove(2) # {1,3,4}
# print(my_set) # Выводит пустое множество
# my_set.discard(5) # ничего не изменится
# print(my_set) # Выводит пустое множество
# my_set.clear()
# print(my_set) # Выводит пустое множество


# set1 = {2, 3, 4, 15}
# set2 = {4, 3, 2, 1}
# print(set1 == set2)
# print(set1 > set2)
# print(set2 < set1)
#
# flag = True
# for i in set2:
#     print(i)
#     if i not in set1:
#         flag = False
#         break
# print(flag)
# print({1, 2}.issubset({1, 2}))




