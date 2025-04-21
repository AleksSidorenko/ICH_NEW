# l = [1, 2, 3]
# r = reversed(l)
# print(r)
# print(list(r))
#
# s = sorted(l, reverse=True)
# print(s)
#
# words = ["asd", "qwer", "tra"]
#
# # w_sort = sorted(words, key=len)
# w_sort = sorted(words, key=lambda w: w[-1])
# print(w_sort)


#
# from time import time
#
# numbers = [n for n in range(1_000_000)]
#
# # print(filter(lambda x: x % 2 == 0, numbers), map(lambda x: x ** 2, numbers))
#
# start = time()
# # result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
# result = filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers))
# end = time() - start
# print(result, end)
#
# start = time()
# result = (x for x in result if x % 2 == 0)
# result = (x ** 2 for x in numbers)
# end = time() - start
# print(result, end)
#
# start = time()
# result = [x for x in result if x % 2 == 0]
# result = [x ** 2 for x in numbers]
# end = time() - start
# print(end)


# 6.198883056640625e-06
# 0.000006198883056640625
# 0.09259486198425293

#
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
# result2 = reduce(lambda x, y: x + y, numbers)
# print(result)
# print(result2, "----------")
# first = map(lambda x: x * 2, numbers)
# print(first)
# second = filter(lambda x: x % 2 == 0, first)
# print(second)
# third = reduce(lambda x, y: x + y, second)
# print(third)


# first = filter(lambda x: x % 2 == 0, numbers)
# print(first)
# second = map(lambda x: x * 2, first)
# print(second)
# third = reduce(lambda x, y: x + y, second)
# print(third)

# import itertools
# import operator
# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
#
# result2 = reduce(operator.mul, numbers)
# print(result2)
#
# result = itertools.accumulate(numbers, operator.mul, initial=1)
# # result = itertools.accumulate(numbers, operator.mul)
# print(result)
# print(list(result))


# import itertools
# letters = ['a', 'b', 'c']
# numbers = [1, 2, 3]
#
# combinations = list(itertools.combinations(letters, 2))
# print(combinations)
# combinations = list(itertools.combinations(letters, 3))
# print(combinations, "\n")
#
# permutations = list(itertools.permutations(numbers))
# print(permutations)
# permutations = list(itertools.permutations(numbers, 2))
# print(permutations, "\n")
#
# product = list(itertools.product(letters, numbers))
# print(product)


import itertools
letters = ['a', 'b', 'c']
numbers = [1, 2]
# zipped = list(itertools.zip_longest(letters, numbers, fillvalue='-'))
zipped = list(itertools.zip_longest(letters, numbers, [0]))
print(zipped)

