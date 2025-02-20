# Дан массив целых чисел длины 1 и более. Написать функцию,
# которая возвращает массив длины 2, состоящих из первого и последнего элемента
# входного массива.
# {1, 2, 3} -> {1, 3}, {7, 4, 6, 2} -> {7, 2}
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def f_mas(numbers):
#     # return (numbers[0], numbers[-1])
#     return [numbers[0], numbers[-1]]
# print(f_mas(numbers))
##############
# Дан список покупок. Найдите какой по счету (начиная с единицы) товар с
# названием "Milk". Если товара нет, выведите сообщение об отсутствии.
# products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
# # print(products.index("Milk") + 1)
# product = "Milk"
# if product in products:
#     print(f"{product} is in {products.index(product) + 1}")
# else:
#     print(f"{product} is not in {products.index(product) + 1}")
#################
# **Задача:**
# Дан текст. Программа должна:
# 1. Разбить текст на слова.
# 2. Создать список уникальных слов в алфавитном порядке (не учитывая регистр).
# 3. Вывести количество уникальных слов.
#
# **Данные:**
# ```python
# text = "Python is a great programming language. Python is popular and powerful."
# ```
#
# **Пример вывода:**
# ```
# Количество уникальных слов: 9
# Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming', 'python']
# ```
# def count_unique(text):
#     # pass
#     split_text = text.replace('.', '').replace(',', '').lower().split()
#     print(split_text)
#     list_unique = []
#     for word in split_text:
#         # if list_unique.count(word) == 0:          # 1-st Variant
#         if word not in list_unique:                 # 2-nd Variant
#             list_unique.append(word)
#     print(list_unique)
#
# count_unique('Python is a great programming language. Python is popular and powerful.')