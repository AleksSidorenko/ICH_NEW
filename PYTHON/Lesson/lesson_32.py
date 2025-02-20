# numbers = [1, 2]
# new_numbers = numbers
# new_numbers.append(3)
# print(numbers)
# print(new_numbers)

# def power(exponent):
# def raise_to_power(base):
# return base ** exponent
# return raise_to_power
#
# square = power(2)
# print(square)
# cube = power(3)
# print(cube)
#
# print(square(4)) # Выведет: 16 (4^2)
# print(cube(4)) # Выведет: 64 (4^3)


#  Дано предложение из слов, разделенных пробелами.
# Написать функцию transform(), которая принимает такое предложение и возвращает аналогичное,
# но где все слова длины 3 в этом предложении - заглавными буквами.
# Пример: “The quick brown fox jumps over the lazy dog” -> “THE quick brown FOX jumps over THE lazy
# DOG”.

# def transform(text):
#     words = text.split()
#     working_list = []
#     for word in words:
#         if len(word) == 3:
#             working_list.append(word.upper())
#         else:
#             working_list.append(word)
#     # print(type(str(working_list)))
#     return " ".join(working_list)
#
# print(transform("The quick brown fox jumps over the lazy dog"))

# def transform(text):
#     words = text.split()
#     new_words = [word.upper() if len(word) == 3 else word for word in words]
#
#     # new_words = []
#     # for word in words:
#     #     if len(word) == 3:
#     #         new_words.append(word.upper())
#     #     else:
#     #         new_words.append(word)
#     return " ".join(new_words)
# print(transform("The quick brown fox jumps over the lazy dog"))

# Изменим условие 1 задачи: нужно, чтобы функция из примера 1 могла также менять слова
# длины 4 на написанные маленькими буквами.
# В общем виде, нужно, чтобы функции можно было дать условие, которому соответствует
# указанное действие.
# Например, все слова длины 4 хотим заменить на звездочки. А слова длины 2 - на черточки.
# Каждое выполнение функции - одно условие и одно действие.

# def transform(text, word_len):
#     words = text.split()
#     new_words = [word.upper() if len(word) == word_len else word for word in words]
#     return " ".join(new_words)
#
# print(transform("The quick brown fox jumps over the lazy dog", 3))
# print(transform("The quick brown fox jumps over the lazy dog", 4))

# def transform(text, condition):
#     words = text.lower().split()
#     new_words = [word.upper() if condition(word) else word for word in words]
#     return " ".join(new_words)
#
# print(transform("The quick brown fox jumps over the lazy dog", lambda word: len(word) == 3))
# print(transform("The quick brown fox jumps over the lazy dog", lambda word: len(word) == 5))
# print(transform("The quick brown fox jumps over the lazy dog", lambda word: word[0] == "t"))

# def square(x):
#     return x ** 2
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x ** 2, numbers)
# print(squared_numbers)
