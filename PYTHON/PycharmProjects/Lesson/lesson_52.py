# Посчитать общую длину слов с помощью любой функции высшего порядка.
# Посчитать общую длину слов с помощью reduce
# colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
#
# colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
# colors_len = map(lambda word: len(word), colour)
# print(sum(colors_len)
#
# colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
# from functools import reduce
#
# # product = reduce(lambda x, y: x * y, numbers, 1000) # 120
#
# # result = len(reduce(lambda x, y: x + y, colour))
# result = reduce(lambda x, y: x + len(y), colour, 0)
# print(result)





import argparse

pars = argparse.ArgumentParser()

pars.add_argument("--input_file", help="path to file with data", required=True)
pars.add_argument("--output_directory", help="path to directory with report", required=True)

args = pars.parse_args()

print(args.input_file, args.output_directory)
