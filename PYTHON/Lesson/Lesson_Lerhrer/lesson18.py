# def add(num1, num2):
#     pass

# def add(num1, num2, num3):
#     pass
#
# def add(num1, num2):
#     def validate(num1, num2):
#         pass

# index = int(input("Enter index"))
# words = ["sfdsf", "fdhghjthj", "sds"]
# #          "s"       "f"        "s"
# # words.sort(key=lambda word: word[0])
# # words.sort(key=lambda word: word[index])
# words.sort(key=lambda word: (word[index], len(word)))
# print(words)
# # "sfdsf"[0] = "s"
# # "fdhghjthj"[0] = "f"


#
# from functools import partial
# # # Создание новой функции, которая всегда будет использовать аргумент x = 2
# # multiply_by_two = partial(lambda x, y: x + y, y='!')
# # print(multiply_by_two)
# # result = multiply_by_two('5')
# # print(result)
#
# print(1, 2, 3, 4, 5, sep='---', end='!\n')
# print(4, 5, sep='---', end='!\n')
# print('hello', 'world', sep='---', end='!\n')
#
# custom_print = partial(print, sep='---', end='!\n')
# custom_print(1, 2, 3, 4, 5)
# custom_print(1, 2)
# custom_print('hello', 'world')
#
# custom_print2 = partial(print, 'Values: ', sep='---')
# custom_print2(1, 2, 3, 4, 5)
#
#
# def say(a, b, c='!'):
#     print(a, b, c)
# say('Bye', 'Mike')
# say('Hello', 'world', c='.')
# new_say = partial(say, 'Hello', b='Jack')
# new_say()


# def countdown(n):
#     if n <= 0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n - 1)
# countdown(5)

# # бесконечно
# def countdown(n):
#     print(n)
#     countdown(n - 1)
# countdown(5)
#
# def countdown(n):
#     while n > 0:
#         print(n)
#         n -= 1
#     print("Done")
# countdown(5)


# def message():
#     print('Это рекурсивная функция')
#     message()
# message()
#
# def message(times):
#     if times > 0:
#         print('Это рекурсивная функция')
#         message(times - 1)
# message(5)

# def message(times):
#     if times > 0:
#         print('Это рекурсивная функция.')
#         message(times - 1)
#         print(times)
# message(5)


def fibonacci_recursive_index(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive_index(n - 1) + fibonacci_recursive_index(n - 2)

# 0 1 1 2 3 5
print(fibonacci_recursive_index(5))

def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 0 1 1 2 3
print(fibonacci_recursive(5))

# Написать программу, вычисляющую факториал числа.
# Решить задачу с помощью рекурсии.
# 5! = 1 * 2 * 3 * 4 * 5 = 120

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         pass
#
# print(factorial(5))

