# class Figure:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_data(self):
#         print(self.w, self.h)
#
#
# f1 = Figure(3, 5)
# f2 = Figure(5, 6)
# f3 = Figure(2, 8)
# f1.get_data()
#
# class Square:
#     pass
#
# s = Square()
# print(s)


# class MyClass:
#     def __init__(self, name="Anonim"):
#         self.name = name
#
# my_object = MyClass("John")
# my_object2 = MyClass()
# print(my_object.name)
# print(my_object2.name)
# # Результат: "John"


# class Person:
#     def __init__(self):
#         self.name = name
#
#
# bob = Person('Bob')
# print(bob.name) # 'Bob'
# alice = Person('Alice')
# print(alice.name) # 'Alice'

#
# class MyClass:
#     static_field = "class"
#     def greet(self, name=""):
#         if name:
#             print(f"Hello, {name}!")
#         else:
#             print("Hello!")
#
#
# print(MyClass.static_field)
# my_object = MyClass()
# my_object.greet()
# # Результат: "Hello!"
# my_object.greet("John")
# # Результат: "Hello, John!"


# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"MyClass: {self.name}"
#
#     def __repr__(self):
#         return f"MyClass(name='{self.name}')"
#
#
# my_object = MyClass("John")
# print(my_object)
# print(repr(my_object))
# print(my_object.__str__())
# print(my_object.__repr__())

#
# class MyClass:
#     def get_data(self):
#             print("data")
#
# class MySubClass(MyClass):
#     pass
#
# my_object = MyClass()
# my_sub_object = MySubClass()
# my_sub_object.get_data()
# # my_sub_object.get_d()
# print(isinstance(my_object, MyClass))
# print(isinstance(my_sub_object, MyClass))
# print(isinstance(my_object, MySubClass))
# print(isinstance(my_object, object))


# x = 10
# print(isinstance(x, str))
# print(isinstance(x, object))

#
# class MyClass:
#     def __init__(self, protected_name, name):
#         self._protected_variable = protected_name  # Защищенный атрибут
#         self.name = name  # Публичный атрибут
#
#     def _protected_method(self):
#         return f"Hello, {self._protected_variable}!"  # Защищенный метод
#
# obj = MyClass("protected", "Alice")
# print(obj._protected_variable)
# print(obj._protected_method())
#
# class Car:
#     def __init__(self, make, model):
#         self._make = make  # Защищенный атрибут
#         self._model = model  # Защищенный атрибут
#
#     def _start_engine(self):
#         print(f"Engine of {self._make} {self._model} started")
#
#     def drive(self):
#         self._start_engine()
#         print(f"{self._make} {self._model} is driving")
#
# my_car = Car("Toyota", "Camry")
# my_car.drive()

#
# class MyClass:
#     def __init__(self, name):
#         self.__private_variable = name  # Приватный атрибут
#
#     def __private_method(self):
#         return f"Hello, {self.__private_variable}!"  # Приватный метод
#
# obj = MyClass("Bob")
# # print(obj.__private_variable)      # Это вызовет ошибку
# # print(obj.__private_method())       # Это вызовет ошибку
# print(obj._MyClass__private_variable)
# print(obj._MyClass__private_method())


# class MyClass:
#     def __init__(self, val):
#         self.__private_variable = val  # Приватный атрибут
#
#     def get_private_variable(self):
#         return self.__private_variable
#
#     def set_private_variable(self, value):
#         if value > 0:
#             self.__private_variable = value
#
# obj = MyClass(30)
# # print(obj.__private_variable)
# print(obj.get_private_variable())
# obj.set_private_variable(-100)
# print(obj.get_private_variable())

# import time
#
# print(dir(obj))
