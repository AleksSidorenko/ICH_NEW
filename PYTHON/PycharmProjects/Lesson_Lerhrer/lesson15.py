# numbers = [1, 2, 3, 4, 5]

# # a = (1,)
# # numbers.append(6)
# # numbers.append(a)
# # numbers.extend(a)
# # numbers.extend(range(5))
#
# # print(numbers[2:])
# to_find = 7
# # if to_find in numbers:
# #     print(numbers.index(to_find, 2))
# # for num in numbers:
# #     if num == to_find
#
# result = numbers.index(4)
# numbers.insert(result, "4")
# print(numbers)
#
# numbers = [1, 2, 3, 4, 5]
#
# # numbers.remove(6)
# # Проверяем есть ли значение, чтобы не вызвать ошибку
# if 6 in numbers:
#     print(numbers.remove(6))
# print(numbers)
#
# def fun():
#     return print([1, 2, 3, 4, 5].remove(3))
# print(fun())
# print(print(1))
#
# my_list = [1, 2, 3, 4, 2, 2, 2]
# # print(my_list.count(2))
#
#
# a = [66.25, 333, 333, 1, 1234.5]
# # a.insert(2, -1)
# # a.remove(333)
# # print(a, a.index(-1), a.count(333))
# # a.clear()
# a = []
# print(a)


#
# my_list = [1, 2, 3, 4]
# my_list2 = my_list
# my_list2.append(5)
# # del my_list[2] # Удаление элемента с индексом 2
# # print(my_list) # [1, 2, 4]
# del my_list # Удаление списка целиком
# # print(my_list)
# print(my_list2)

# my_tuple = (1, 2, 3, 4)
# print(my_tuple)
# print(type(my_tuple))
# print(my_tuple.count(2))
# # my_tuple[0] = "1"
#
# def return_two():
#     my_tuple = (1, 2, 3, 4)
#     a = my_tuple.index(4)
#     b = my_tuple.count(2)
#     return a, b
# print(return_two())
#
# x, y = return_two()
#
#
# my_list = [1, 2, 3]
# print(my_list[0], my_list[1], my_list[2], sep="---")
# print(*my_list, sep="---")
#
# def sum_elements(name, *elements):
#     print(name)
#     print(elements)
#     print(type(elements))
#     print(sum(elements))
#
#
# sum_elements("Anna", 1, 4, 4, 6, 3, 7, 8, 8)
# print(1, 54, 8, "345")

t = 1, 2, 3
print(type(t))

my_list = [1, [2, 4], 3]
for i, item in enumerate(my_list):
    print(i, item)


s = "Hello world!"
print(*tuple(s), sep="_")

print("_".join(tuple(s))) # это тоже подет
