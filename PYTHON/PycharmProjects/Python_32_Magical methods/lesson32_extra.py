# from functools import total_ordering
import functools

# @total_ordering
@functools.total_ordering
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price  # and self.name.lower() == other.name.lower()

    # def __ne__(self, other):
    #     return self.price != other.price

    # def __lt__(self, other):
    #     return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    # def __le__(self, other):
    #     return self.price <= other.price

    # def __ge__(self, other):
    #     return self.price >= other.price

    # def __bool__(self):
    #     return bool(self.price)

    # def __hash__(self):
    #     return hash((self.name, self.price))  # Используем кортеж

p1 = Product("Apple", 0)
p2 = Product("Banana", 2)

print(p1 < p2)
print(p1 <= p2)
print(p1 > p2)
print(p1 >= p2)
print(p1 == p2)
print(p1 != p2)
print()
print(bool(p1))
print(bool(p2))

# Если в классе определен __eq__, а __hash__ не переопределен, то Python автоматически делает __hash__ = None.
# s = {p1, p2}
# print(s)

# class MyList:
#     def __init__(self, data):
#         self.data = data  # Внутренний список
#
#     def __getitem__(self, index):
#         print(f"Получаем элемент {index}")
#         return self.data[index]  # Просто берем из списка
#
#     def __setitem__(self, index, value):
#         if value >= 0:
#             print(f"Устанавливаем {value} в позицию {index}")
#             self.data[index] = value  # Изменяем список
#         else:
#             print("Значение не может быть отрицательным")
#
#
# ml = MyList([10, 20, 30])
# print(ml[1])  # Вызывает __getitem__ → Получаем 20
# ml[1] = 99  # Вызывает __setitem__ → Меняем на 99
# print(ml.data)  # [10, 99, 30]
# ml[1] = -5  # Вызывает __setitem__
# print(ml.data)  # [10, 99, 30]


#
# class MyDict:
#     def __init__(self):
#         self.data = {}
#
#     def __getitem__(self, key):
#         return self.data[key]
#
#     def __setitem__(self, key, value):
#         self.data[key] = value
#
#     def __delitem__(self, key):
#         del self.data[key]
#
# from collections import ChainMap
#
# # Создаем объект MyDict
# my_dict = MyDict()
#
# # Добавляем элементы
# my_dict['name'] = 'John'
# my_dict['age'] = 25
#
# print(my_dict['age'])
#
# # Удаляем элемент по ключу
# del my_dict['name']
#
# # Проверяем результат
# print(my_dict.data)


# class MyCallable:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, greeting):
#         print(f"{greeting}, {self.name}!")
#
# # Создаем экземпляр класса
# obj = MyCallable("Alice")
#
# # Вызываем объект как функцию
# obj("Hello")

# class Test:
#     pass
#     def __call__(self):
#         print("Hello World")
#
# test = Test()
# test()
#

# class Factorial:
#     def __init__(self):
#         self.cache = {}
#
#     def __call__(self, n):
#         if n in self.cache:
#             return self.cache[n]
#         if n == 0:
#             self.cache[n] = 1
#         else:
#             self.cache[n] = n * self(n - 1)
#             print("-----")
#         return self.cache[n]
#
# fact = Factorial()
# print(fact(5))  # 120
# print(fact(6))  # 720 (использует кеш)



