# Дана строка с именем, например, “Иван”.
# Написать программу, которая печатает
# приветствие, например, “Привет, Иван!”.
# n = input("Enter your name: ")
# print(f'\033[32m Hello, {n}\033[0m') # Подсветка вывода строки:
# Красный: \033[31m
# Зеленый: \033[32m
# Желтый: \033[33m
# Синий: \033[34m
# Фиолетовый: \033[35m
# Голубой: \033[36m
# Пример:
# print("\033[1;32;40mЖирный
# зелёный текст на чёрном фоне\033[0m")
import string

#  Веб-страницы состоят из строк типа "<i>Yay</i>" - выводит текст Yay курсивом.
#  В этом примере, строка-тег “i” означает <i> и </i>, которые окружают слово Yay.
#  Нам дана строка-тэг и текст.
#  Написать программу, которая выводит тег вокруг данного текста, например,  "<i>Yay</i>".
#  Например, ('i', 'Hello') → '<i>Hello</i>'.
# text = input("Enter a string: ")
# mod_str = "<i>" + text + "</i>"
# print(mod_str)

# Дана строка. Написать программу, которая создает строку из трех копий последних двух символов данной строки.
# Данная строка должна быть длиной минимум 2. (('Hello') → 'lololo'), ('ab') → 'ababab'.
# text = input("Enter a string: ")
# if text > 2:
#     a = text[-2:] * 3
#     print(a)
# else:
#     print("text must be at least 2 symbols")

# Дана строка, написать программу, которая печатает строку без первого и последнего
# символа от данной строки, например, “Иван” - “ва”. “Python” -> “ytho”.
# text = input("Enter a string: ")
# print(text[1:-1])

# Даны две строки разной длины (одна может быть пустой).
# Написать программу, которая печатает строку вида короткая+длинная+короткая,
# где короткая строка снаружи длинной. Например, 'Hello', 'hi' → 'hiHellohi'.
# sep - задаем любой разделитель по - умолчанию
# string_1 = input("String: ")
# string_2 = input("String: ")
# if len(string_1) > len(string_2):
#     print(f'{string_1}{string_2}{string_1}')
# else:
#     print(string_2, string_1, string_2, sep='***')

# Написать программу, которая печатает True, если слова “cat” и “dog”
# встречаются в строке одинаковое количество раз (и напечатать false - если разное количество раз).
# 'catdog' → True, 'catcat' → False, '1cat1cadodog' → True
# string_1 = input("Enter a string: ")
# cat_int = string_1.count('cat')
# dog_int = string_1.count('dog')
# if cat_int == dog_int: # вывод
#     print('True')
# else:
#     print('False')
# print(cat_int == dog_int) # другой вывод
# print(string_1)
# print(cat_int)
# print(dog_int)

# Варианt №2
# string_1 = input("Enter a string: ")
# cat_int = 0
# dog_int = 0
# i = 0
# while i <= len(string_1) - 3:
#     if string_1[i:i + 3] == 'cat':      # cat_int in string_1:
#         cat_int += 1
#     else:
#         string_1[i:i + 3] == 'dog'
#         dog_int += 1
#     i += 1
# print(string_1)
# print(cat_int)
# print(dog_int)

# Написать программу, которая печатает количество вхождений данной подстроки в строку.
# Например, для подстроки hi, 'abc hi ho' → 1, для подстроки “well”,  'ABCwell well') → 2.
# string = input("Enter a string: \n")
# word = 'Hello'
# i = 0
# n = 0
# while i + len(word) <= len(string):
#     if string[i:i + len(word)] == word:
#         n += 1
#     i += 1
# print(n)







