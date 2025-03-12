# numbers = [1, 2, 3, 4, 5]
# all_true = all(num > 0 for num in numbers) # True
# print(all_true)
# print(all(numbers))
# any_true = any(num < 0 for num in numbers) # False
#
# all_bool = (num > 0 for num in numbers) # True
# print(list(all_bool))
# print(all_bool)
#
# if 2:
#     print("not null")
#
# item_list = [[]]
# print(all(item_list))
#
# def new_all(coll):
#     for i in coll:
#         if not i:
#             return False
#     return True
# print(new_all(item_list))
#
#
# numbers = [3, 1, 4, 2, 5]
# sorted_numbers = sorted(numbers) # [1, 2, 3, 4, 5]
# print(sorted_numbers)
# reversed_numbers = reversed(numbers) # <list_reverseiterator object at 0x7f4b930b3d00>
# print(reversed_numbers)
# print(list(reversed_numbers))
# print(numbers)


# fruits = ['apple', 'banana', 'orange']
# for index, fruit in enumerate(fruits, 1):
#     print(index, fruit)
# print(enumerate(fruits, 1))
# print(list(enumerate(fruits, 1)))

# numbers = [1324, 223, 545, 234]
# letters = ['a', 'b', 'c']
# words = ['sdfsd', 'sdfsd', 'sdf']
# zipped = zip(numbers, letters, words)
# print(list(zipped))
# for num, letter, word in zipped:
#     print(num, letter, word)
# #
# colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
# print(list(enumerate(colour)))
#
# def square(x):
#     return x ** 2

# numbers = [1, 2, 3, 4, 5]
# squar = (i ** 2 for i in numbers)
# print(list(squar))
# squared = map(square, numbers) # [1, 4, 9, 16, 25]
# squared = map(lambda x: x ** 2, numbers)
# print(squared)
# print(list(squared))
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ev = (i for i in numbers if i % 2 == 0)
# print(ev)
# print(list(ev))
# even = filter(lambda x: x % 2 == 0, numbers) # [2, 4]
# print(even)
# print(list(even))

# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers, 1) # 120
# print(product)
#  * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120

# Посчитать общую длину слов с помощью любой функции высшего порядка.
# Посчитать общую длину слов с помощью reduce

# colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
#
# colors_len = map(lambda word: len(word), colour)
# print(colors_len)
# print(list(colors_len))
# print(sum(colors_len))
# s = 0
# for i in colors_len:
#     s += i
# print(s)


# from functools import reduce
#
# colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers, 10) # 120
# print(product)
# product = map(lambda x: x * x, numbers)
# print(list(product))
# # result = len(reduce(lambda x, y: x + y, colour))
# result = reduce(lambda x, y: x + len(y), colour, 0)
# print(result)

# def squ(num):
#     return list((sq**2 for sq in num))

# numbers = [1, 2, 3, 4, 5]
# oder:
# num = (sq**2 for sq in numbers)
# oder:
# num = map(lambda x: x ** 2, numbers)
# print(squ(numbers))

# def s(num):
#     # return list((i for i in num if i % 2 != 0))
#     return list(filter(lambda i: i % 2 != 0, num))
#
# numbers = [1, 2, 3, 4, 5]
# print(s(numbers))

# def to_upper(strings):
#     return list(map(lambda x: x.upper(), strings))
#
# string = ['avd', 'fgjr', 'skim', 'g6t']
# print(to_upper(string))

# def join_words(words):
#     return " ".join(words) + "."
#
# List_words = ['avd', 'fgjr', 'skim', 'g6t']
# print(join_words(List_words))

# def to_len_str(strings):
#     return list(filter(lambda x: len(x)>1, strings))
#
# string = ['avd', 'fgjr', 'skim', 'g6t']
# print(to_len_str(string))

# def prod(num):
    # from functools import reduce
    # return reduce(lambda x, y: x*y, num)

# numbers = [1, 2, 3, 4, 5]
# print(prod(numbers))

#
# import argparse
# import os
#
# pars = argparse.ArgumentParser()
#
# pars.add_argument("--input_file", help="path to file with data", required=True)
# pars.add_argument("--output_directory", help="path to directory with report", required=True)
#
# args = pars.parse_args()
#
# print(args.input_file)
# print(args.output_directory)
#
# print(os.path.isfile(args.input_file))
# os.makedirs(args.output_directory, exist_ok=True)
#
# with open(args.input_file, 'r') as file:
#     data = file.readlines()
#
# print(data)


# import os
#
# # filepath = "../../test.py"
# filepath = "test.py"
#
# os.system(f"python {filepath}")
#
# print("Finished")
