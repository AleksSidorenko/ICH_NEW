# 1. Напишите функцию find_longest_word, которая будет принимать список слов и
# возвращать самое длинное слово из списка.
# Аннотируйте типы аргументов и возвращаемого значения функции.
# Пример вызова функции и ожидаемого вывода:
# words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
# print(result)  # Ожидаемый вывод: "dragonfruit"
#
# from typing import List
#
# def find_longest_word(l_words: list) -> list:
#     words = []
#     for word in list_words:
#         if len(word) > len(words):
#             words = word
#     return words
#
# list_words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(list_words)
# print(result)

# Option
# from typing import Iterable
#
# def find_longest_word(l_words: list) -> Iterable[list]:
#     words = []
#     for word in list_words:
#         if len(word) > len(words):
#             words = word
#     yield words
#
# list_words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(list_words)
# print(next(result))

# Option
# from typing import List
#
# def find_longest_word(w: List[str]) -> str:
#    return max(w, key = len)
#
# words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
# print(result)

# Option

# from typing import List
#
# def find_longest_word(words: List[str]) -> str:
#     return next((word for word in sorted(words, key=len, reverse=True)), "")
#
# # Пример использования
# words_list = ["apple", "banana", "cherry", "blueberry"]
# print(find_longest_word(words_list))


# 2. Напишите программу, которая будет считывать данные о продуктах из файла и
# использовать аннотации типов для аргументов и возвращаемых значений функций.
# Создайте текстовый файл "products.txt",
# в котором каждая строка будет содержать информацию о продукте
# в формате "название, цена, количество". Например:
# Apple, 1.50, 10
# Banana, 0.75, 15
# В программе определите функцию calculate_total_price,
# которая будет принимать список продуктов и возвращать общую стоимость.
# Продумайте, какая аннотация должна быть у аргумента!
# Считайте данные из файла, разделите строки на составляющие и создайте список продуктов.
# Затем вызовите функцию calculate_total_price с этим списком и выведите результат.
# Начиная с этого дз мы потихоньку отказываемся от формата ожидаемого ввода-вывода.
# Потому что в реальных задачах обычно этого нет.
# Нужно самому придумывать даже самые простые тестовые данные,
# содержимое тестовых файлов и т.п. В случае с классами (будут чуть позже) особенно.

# from typing import List, Any
#
# def calculate_total_price(text: List[Any]) -> float:
#     return float(text[1]) * float(text[2])
#
# with open('products.txt', 'w+') as file:
#     lines = ["Apple, 1.50, 10", "Banana, 0.75, 15"]
#     summa = 0
#     for line in lines:
#         file.write(line)
#         file.readlines()
#         pr = calculate_total_price(line.split(', '))
#         file.write('\n')
#         summa = summa + pr
#     print(summa)

# from typing import List, Tuple
#
# def calculate_total_price(product_list: List[Tuple[str, float, int]]) -> float:
#     sum_price = 0
#     for _, price_prod, quantity_prod in product_list:
#         price_prod = price_prod * quantity_prod
#         sum_price += price_prod
#     return sum_price
#
#
# with open('products.txt', 'w+') as file:
#     lines = ["Apple, 1.50, 10", "Banana, 0.75, 15"]
#     products = []
#     for line in lines:
#         file.write(line)
#         file.readlines()
#         name, price, quantity = line.split(", ")
#         products.append((name, float(price), int(quantity)))
#         file.write('\n')
#     print(f"Общая стоимость всех товаров: {calculate_total_price(products)} EUR")


# Option
#
# from typing import List,Tuple
#
# def calculate_total_price(c: List[Tuple[str,float,int]]) -> float:
#     total=0
#     for i in c:
#         total+=i[1]*i[2]
#     return total
#
#
# f = [ x.split(", ") for x in open("products.txt","r").readlines() ]
# s = [ (y[0],float(y[1]),int(y[2])) for y in f ]
# print(calculate_total_price(s))


# Option

# from typing import List, Tuple
#
# # Определяем тип данных для продукта: (название, цена, количество)
# Product = Tuple[str, float, int]
# def read_products_from_file(filename: str) -> List[Product]:
#     """Считывает продукты из файла и возвращает список кортежей (название, цена, количество)."""
#     products = []
#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             for line in file:
#                 name, price, quantity = line.strip().split(", ")
#                 products.append((name, float(price), int(quantity)))
#     except FileNotFoundError:
#         print(f"Ошибка: Файл '{filename}' не найден.")
#     except ValueError:
#         print("Ошибка: Некорректные данные в файле.")
#     return products
#
# def calculate_total_price(products: List[Product]) -> float:
#     """Вычисляет общую стоимость всех продуктов."""
#     return sum(price * quantity for _, price, quantity in products)
#
# # Основная логика программы
# file_name = "products.txt"
# product_list = read_products_from_file(file_name)
# if product_list:
#     total_price = calculate_total_price(product_list)
#     print(f"Общая стоимость всех товаров: {total_price:.2f} EUR")



