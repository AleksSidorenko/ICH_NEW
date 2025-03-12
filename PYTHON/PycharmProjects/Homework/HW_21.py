# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте
# и выводит на экран наиболее часто встречающиеся слова.
# Для решения задачи используйте класс Counter из модуля collections.
# Создайте функцию count_words, которая принимает текст в качестве аргумента
# и возвращает словарь с количеством вхождений каждого слова.
# Выведите наиболее часто встречающиеся слова и их количество.
# Пример вывода:
# Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1

# from collections import Counter

# def count_words(text):
#     t = text.lower().replace(",", "").replace(".", "").split()
#     return Counter(t).items()
# s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est." # input("Введите текст: ")
# c = sorted(count_words(s), key=lambda x: x[1], reverse=True)
# for i in c[:2]:
#     print(f"{i[0]}: {i[1]}")

# def count_words(text):
#     clear_words = Counter(text.lower().split())
#     cnt_words = []
#     for word, count in sorted(clear_words.items(), key=lambda i: i[1], reverse=True):
#         if count > 1:
#             cnt_words.append(f'{word}: {count}')
#         else:
#             if len(cnt_words) == 1:
#                 cnt_words.append(f'\n{word}: {count}')
#
#     return print(*cnt_words)
#
# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est."
# count_words(text)

# 2. Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке,
# включающий поля name, age и city.
# Создайте список объектов Person и выведите информацию о каждом человеке на экран.
# Пример вывода:
# Name: Alice, Age: 25, City: New York
# Name: Bob, Age: 30, City: London
# Name: Carol, Age: 35, City: Paris

# from collections import namedtuple
#
# Person = namedtuple('Person', 'name age city')
# pers = [Person("Alice", 25, "New York"),
#         Person("Bob", 30, "London"),
#         Person("Carol", 35, "Paris")]
#
# p = { print(f'Name: {name}, Age: {age}, City: {city}') for name, age, city in pers }

# 3. Напишите программу, которая принимает словарь от пользователя и ключ,
# и возвращает значение для указанного ключа с использованием метода get или setdefault.
# Создайте функцию get_value_from_dict, которая принимает словарь и ключ в качестве аргументов,
# и возвращает значение для указанного ключа,
# используя метод get или setdefault в зависимости от выбранного варианта.
# Выведите полученное значение на экран.
# Пример словаря:
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
# Пример вывода:
# Введите ключ для поиска: banana
# Использовать метод get (y/n)? y
# Значение для ключа 'banana': 6

# def get_value_from_dict(dict, key, method):
#     return dict.get(key, 0) if method == 'y' else dict.setdefault(key, 10)
#
#
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
# key, method = map(str, (input("Введите ключ товара: "), input("и метод поиска (get - y / set - n):  ")))
# print(f"Остаток {key} на складе: {get_value_from_dict(my_dict, key, method)} тонн")
# print(f'Ассортимент всего товара на складе: {my_dict}')

# key = input("Введите ключ для поиска товара: ")
# method = True if input("Использовать метод get (y/n)? ").lower() == "y" else False