## Чтение JSON-файла с товарами и расчет общей стоимости**
# Задача:
#
# Запросить у пользователя имя JSON-файла с товарами.
# Прочитать данные, обработать ошибки (FileNotFoundError, PermissionError, JSONDecodeError).
# Посчитать общую стоимость всех товаров (цена × количество). Обработать ошибки валидности данных

# [
# {"name": "яблоко", "price": 50, "quantity": 3},
# {"name": "банан", "price": 30, "quantity": 2},
# {"name": "апельсин", "price": 40, "quantity": 4}
# ]
# import json
# from json import JSONDecodeError
#
# try:
#     with open("products.json", encoding= "utf-8") as my_file:
#         data_products = json.load(my_file)
# except FileNotFoundError:
#     print("вашего файла не существует. возможно я его не вижу, ты не видишь, а он есть")
# except PermissionError:
#     print("у меня прав нет, дай админку")
# except JSONDecodeError:
#     print("Json шалит")
# else:
#     sum = 0
#     for product in data_products:
#         try:
#             sum += product['price']
#         except KeyError:
#             print("продукт не корректен - ", product)
#         except TypeError:
#             print("цена не корректна - ", product)
#     print(sum)