# class Money:
#     def __init__(self, amount, currency):
#         self.amount = amount
#         self.currency = currency
#
#     # def __add__(self, other):
#     #     if self.currency == other.currency:
#     #         return Money(self.amount + other.amount, self.currency)
#
#     def __add__(self, other):
#         if self.currency == other.currency:
#             self.amount += other.amount
#         return self
#
#     def __str__(self):
#         return f"{self.amount} {self.currency}"
#
#
# m1 = Money(100, "eur")
# m2 = Money(230, "eur")
# m3 = m1 + m2
# print(m3)
# print(id(m1))
# print(id(m2))
# print(id(m3))


# from functools import total_ordering
# # import functools
#
# @total_ordering
# # @functools.total_ordering
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __eq__(self, other):
#         return self.price == other.price  # and self.name.lower() == other.name.lower()
#
#     # def __ne__(self, other):
#     #     return self.price != other.price
#
#     # def __lt__(self, other):
#     #     return self.price < other.price
#
#     def __gt__(self, other):
#         return self.price > other.price
#
#     # def __le__(self, other):
#     #     return self.price <= other.price
#
#     # def __ge__(self, other):
#     #     return self.price >= other.price
#
#     def __bool__(self):
#         return bool(self.price)
#
#     def __hash__(self):
#         return hash((self.name, self.price))  # Используем кортеж
#
# p1 = Product("Apple", 2)
# p2 = Product("Banana", 0)
#
# print(p1 < p2)
# print(p1 <= p2)
# print(p1 > p2)
# print(p1 >= p2)
# print(p1 == p2)
# print(p1 != p2)
# print()
# print(bool(p1))
# print(bool(p2))
#
# # Если в классе определен __eq__, а __hash__ не переопределен, то Python автоматически делает __hash__ = None.
# s = {p1, p2}
# print(s)
#
#
# l = [1, 2, 3]
# print(len(l))
# print(l.__len__())


#
#
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
#     def __str__(self):
#         return str(self.data)
#
# ml = MyList([10, 20, 30])
# print(ml)
# print(ml[1])  # Вызывает __getitem__ → Получаем 20
# ml[1] = 99  # Вызывает __setitem__ → Меняем на 99
# print(ml)  # [10, 99, 30]
# ml[1] = -5  # Вызывает __setitem__
# print(ml.data)  # [10, 99, 30]


# class MyCallable:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, greeting):
#         print(f"{greeting}, {self.name}!")
#
# # Создаем экземпляр класса
# obj = MyCallable("Alice")
# print(obj)
#
# # Вызываем объект как функцию
# obj("Hello")
# # obj.__call__("Hello")
#
# class Test:
#
#     def __call__(self):
#         print("Hello World")
#
# test = Test()
# test()


# class MyIterator:
#     def __init__(self):
#         self.i=0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i<100:
#             self.i+=10
#             return self.i
#         else:
#             raise StopIteration
#
# obj = MyIterator()
# for item in obj:
#     print(item)
#
#
# class MyClass:
#     def __init__(self):
#         self.x = 1
#         self.y = 2
# obj = MyClass()
# print(obj.__dict__) # {'x': 1, 'y': 2}


class Factorial:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n in self.cache:
            return self.cache[n]
        if n == 0:
            self.cache[n] = 1
        else:
            self.cache[n] = n * self(n - 1)
            print("-----")
        return self.cache[n]

fact = Factorial()
print(fact(5))  # 120
print(fact(6))  # 720 (использует кеш)