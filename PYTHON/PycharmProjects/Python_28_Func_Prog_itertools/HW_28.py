# 1. Напишите программу, которая принимает список слов от пользователя
# и использует генераторное выражение (comprehension) для создания нового списка,
# содержащего только те слова, которые начинаются с гласной буквы.
# Затем программа должна использовать функцию map, чтобы преобразовать каждое слово в верхний регистр.
# В результате программа должна вывести новый список,
# содержащий только слова, начинающиеся с гласной буквы и записанные в верхнем регистре.

# def new_list_vowels_letters(list_words):
#     vowels_letters = "AEIJOUYaeijouy"
#     comprehension = (word for word in list_words if word[0] in vowels_letters)
#     return list(map(lambda word: word.upper(), comprehension))
#
#
# l_words = ['apple', 'banana', 'kiwi', 'apricot', 'cherry', 'grape', 'orange', 'mango']
# print(new_list_vowels_letters(l_words))


# 2. Напишите программу, которая принимает список чисел от пользователя
# и использует функцию reduce из модуля functools, чтобы найти произведение всех чисел в списке.
# Затем программа должна использовать функцию itertools.accumulate для накопления произведений чисел в новом списке.
# В результате программа должна вывести список, содержащий накопленные произведения.

# from functools import reduce
# from itertools import accumulate
#
# def accumulated_products(num):
#     products = reduce(lambda x, y: x * y, num)
#     return list(accumulate(num, lambda x, y: x * y))
#     # return list(accumulate(num, operator.mul))
#
#
# # numbers = list(accumulate([1, 2, 3, 4, 5]))
# # print(numbers)
# numbers = [1, 2, 3, 4, 5]
# print("Накопленные произведения:", accumulated_products(numbers))

# ---------------------------- map() -------------
# from functools import reduce
# from itertools import  accumulate
# from operator import mul
#
# numbers = [int(x) for x in input("Введите список чисел:").split()]
# product_red = reduce(lambda x,y: x*y, numbers)
# print(product_red)
# product_acc = accumulate(numbers, mul)
# print(list(product_acc))

# name_lengths = map(len, ['Маша', 'Петя', 'Вася'])
# print(list(name_lengths))

# squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
# print(list(squares))

# import random
#
# names = ['Маша', 'Петя', 'Вася']
# code_names = ['Шпунтик', 'Винтик', 'Фунтик']
# for i in range(len(names)):
#     names[i] = random.choice(code_names)
# print(names)

# import random

# names = ['Маша', 'Петя', 'Вася']
# secret_names = map(lambda x: random.choice(['Шпунтик', 'Винтик', 'Фунтик']), names)
# print(list(secret_names))


# names = ['Маша', 'Петя', 'Вася']
# for i in range(len(names)):
#     names[i] = hash(names[i])
# print(list(names))
# oder:
# secret_names = map(lambda i: hash(names[i]), range(len(names)))
# print(list(secret_names))
# oder:
# names = ['Маша', 'Петя', 'Вася']
# secret_names = map(hash, names)
# print(list(secret_names))

# ------------ reduce() ---------------
from functools import reduce

# summa = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
# print(summa)

# sentences = ['капитан джек воробей',
#              'капитан дальнего плавания',
#              'ваша лодка готова, капитан']
# cap_count = reduce(lambda a, x: a + x.count('капитан'), sentences,0)
# print(cap_count)

# people = [{'имя': 'Маша', 'рост': 160},
#           {'рост ': 'Саша', 'рост': 80},
#           {'name': 'Паша'}]
# heights = list(map(lambda x: x['рост'],
#           filter(lambda x: 'рост' in x, people)))
# if len(heights) > 0:
#     from operator import add
#     average_height = reduce(add, heights) / len(heights)
# print(average_height)

# from random import random
#
# def move_cars(car_positions):
#     return map(lambda x: x + 1 if random() > 0.3 else x,
#                car_positions)
#
# def output_car(car_position):
#     return '-' * car_position
#
# def run_step_of_race(state):
#     return {'time': state['time'] - 1,
#             'car_positions': move_cars(state['car_positions'])}
#
# def draw(state):
#     print('')
#     print('\n'.join(map(output_car, state['car_positions'])))
#
# def race(state):
#     draw(state)
#     if state['time']:
#         race(run_step_of_race(state))
#
# race({'time': 5,
#       'car_positions': [1, 1, 1]})

# reduce(lambda res, x: [x]+res, [1, 2, 3, 4], [])
# print(reduce(lambda res, x: [x] + res, [1, 2, 3, 4], []))