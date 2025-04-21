

# nums = [1, 2, 3, 4, 5]
# # nums.__next__()
# it = nums.__iter__()
# print(it)
# print(type(it))
# print(it.__next__())
# print(it.__next__())
# print("-----------")
# print(it.__next__())
# nums[3] = 0
# print(nums)
# print(list(it))
# new = []
# for i in it:
#     print(i)
    # print(it.__next__())
# print(new)

# file = open("numbers.txt")
# print(file.__next__())
# print(file.__next__())
# print(file)
# print(type(file))

# import sys
#
# numbers = iter(range(1, 1000001))
# print(sys.getsizeof(numbers))
# numbers = range(1, 1000001)
# print(sys.getsizeof(numbers))
# numbers = list(range(1, 1000001))
# print(sys.getsizeof(numbers))
#
# my_list = [1, 2, 3]
# for i in my_list:
#     print(i)
# it = my_list.__iter__()
# print(it)
# it = iter(my_list)
# print(it)
# print(it.__next__())
# print(next(it))
# print(next(it))
# print(next(it, None))
# print(next(it, None))
# print(next(it, None))
# # for item in my_list:
# #     print(item)
#
# iterator = iter(my_list)
# while True:
#     # print(next(iterator))
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break

# -----------------------------------------------

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
# gen = my_generator()
# gen1 = my_generator()
# print(gen)
# print(type(gen))
#
# print(next(gen))
# print(next(gen1))
# print(next(gen))
# print(next(gen))

# # return в генераторе
# def my_generator():
#     yield 1
#     yield 2
#     return "End"
#
# gen = my_generator()
# print(next(gen))  # 1
# print(next(gen))  # 2
# try:
#     print(next(gen))  # StopIteration: End
# except StopIteration as e:
#     print(e.value)  # End


# # return в генераторе
# def process_data(data):
#     for i in data:
#         if i == "STOP":
#             return "Processing stopped"  # Завершает генератор
#         yield i
#
# gen = process_data(["a", "b", "c", "STOP", "d"])
# # for item in gen:
# #     print(item)
#
# for item in gen:
#     try:
#         print(item)  # StopIteration: End
#     except StopIteration as e:
#         print(e.value)  # End

#
# my_generator = (x ** x for x in range(10))
# print(my_generator)
# for item in my_generator:
#     print(item)


# def show_letters(some_str):
#     for symbol in some_str:
#         if symbol.isalpha():
#             yield symbol

# def show_letters(some_str):
#     # yield from (letter for letter in some_str if letter.isalpha())
#      yield (letter for letter in some_str if letter.isalpha())
#
# for i in show_letters("kf23r89h2i"):
#     print(i)

# ------------------------------

# import itertools
# my_list = [1, 2, 3, 4, 5]
# my_iterator = itertools.islice(my_list, 1, 4)
# for item in my_iterator:
#     print(item) # Выводит 2, 3, 4

# import itertools
# colors = ['red', 'green', 'blue']
# sizes = ['S', 'M', 'L']
# # for color, size in zip(colors, sizes):
# #     print(color, size)
# for color, size in itertools.product(colors, sizes):
#     print(color, size)
#
# import itertools
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# for item in itertools.chain(list1, list2):
#     print(item)


def my_range(start, stop=None, step=1):
    if stop is None:  # Если указан только один аргумент, то это "stop"
        stop = start
        start = 0
    while start < stop:
        yield start
        start += step

# for i in my_range(3):
#     print(i)
for i in my_range(1, 11, 2):
    print(i)

print()