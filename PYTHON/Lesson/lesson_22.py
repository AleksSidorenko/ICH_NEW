# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов.
# Option 1
# s = input("Enter a string: ").split()
# print(len(s))
# Option 2
# s = input("Enter a string: ")
# print(s.count(" "))
# print(s.count(" ")+1)

# Напишите программу,
# которая считает вхождение заданной подстроки в заданную строку.
# Например, для подстроки “ab” и строки “Abrakadabra” программа напечатает 2.
# s = input("Enter a string: ").lower()
# text = input("Enter a text: ").lower()
# print(s.count(text))

# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.
# При решении этой задачи не стоит пользоваться циклами и инструкцией if.
# OPtion 1
# s = input("Enter a string: ").split()
# print(s[1] + " " + s[0])
# Option 2
# s1 = s[:]
# s2 = s1[::-1]
# print(s2)

# For variable in iterable object:
#       operator 1
#       operator 2
#       .....
#       operator n
# 1
# list1 = [1, 2, 3, 4, 5]
# for item in list1:
#     print(item)
# 2
# text = 'python'
# for item in text:
#     print(item)
# while i < len(text): # вариант с while
#     print(text[i])
#     i = i + 1
# 3
# for char in 'Python':
#     print(char.upper())
# 4
# for i in range(1, 11):
#     print(i)
# 5
# list1 = [1, 2, 3, 4, 5]
# for item in list1:
#    print(item * 2)
    # a = item * 2
    # print(a)
# list1 = [1, 2, 3, 4, 5]
# for item in [0,1,2,3,4]:
#     list1[item] = 0
#     print(list1)
# 6
# for i in range(2, 501, 50): # range(start, stop, step)
#     print(i)
# 7
# s = 'Hello World'
# for letter in s:
#     print(letter, end=' ') # end=' ' - печать по горизонтали
# for letter in range(len(s)):
#    print(s[letter], end = ' ')
#    print(letter * 2)
# 8
# s = 'Hello World'
# for i, d in enumerate(s):
#     print(i, d)
# for d, i in enumerate(s): # при перемене мест переменных for меняет местами вывод
#     print(i, d)










