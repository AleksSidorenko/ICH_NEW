# class MyClass:
#     def __init__(self, name):
#         self.name = name  # Публичный атрибут
#
#     def public_method(self):
#         return f"Hello, {self.name}!"  # Публичный метод
#
# obj = MyClass("John")
# print(obj.name)
# print(obj.public_method())


# class MyClass:
#     def __init__(self, protected_name, name):
#         self._protected_variable = protected_name  # Защищенный атрибут
#         self.name = name  # Публичный атрибут
#
#     def _protected_method(self):
#         return f"Hello, {self._protected_variable}!"  # Защищенный метод
#
# class MySubClass(MyClass):
#     pass
#
#
# obj = MyClass("protected", "Alice")
# print(obj.name)
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
#     def start_engine1(self):
#         print(f"Engine of {self._make} {self._model} started")
#
#     def start_engine2(self):
#         print(f"Engine of {self._make} {self._model} started")
#
#     def start_engine3(self):
#         print(f"Engine of {self._make} {self._model} started")
#
#     def start_engine4(self):
#         print(f"Engine of {self._make} {self._model} started")
#
#     def start_engine5(self):
#         print(f"Engine of {self._make} {self._model} started")
#
#     def drive(self):
#         self._start_engine()
#         print(f"{self._make} {self._model} is driving")
#
# my_car = Car("Toyota", "Camry")
# my_car.drive()

#
#
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
#
# print(obj._MyClass__private_variable)
# print(obj._MyClass__private_method())





# class MyClass:
#     def __init__(self, name):
#         self.__name = name  # Приватный атрибут
#
#     def __private_method(self):
#         return f"Hello, {self.__name}!"  # Приватный метод
#
# obj = MyClass("Bob")
# print(obj.__name)      # Это вызовет ошибку
# # print(obj.__private_method())       # Это вызовет ошибку
#
# print(obj._MyClass__name)
# print(obj._MyClass__private_method())


# class MyClass:
#     def __init__(self):
#         self.__private_variable = 42  # Приватный атрибут
#
#     def get_private_variable(self):
#         return self.__private_variable
#
#     def set_private_variable(self, value):
#         self.__private_variable = value
#
# obj = MyClass()
# print(obj.get_private_variable())
# obj.set_private_variable(100)
# print(obj.get_private_variable())

# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, new_age):
#         if new_age > 0:
#             self.__age = new_age
#
# person = Person(18)
# # person.__age
# print(person.get_age())
# person.set_age(19)
# print(person.get_age())



class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    def get_average_grade(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)

    def add_grade(self, grade):
        if grade in range(1, 6):
        # if 1 <= grade <= 5:
            self.__grades.append(grade)

student = Student("Bob", 18)
print(student.get_average_grade())
student.add_grade(-3)
student.add_grade(4)
student.add_grade(5)
print(student.get_average_grade())
# print(list(range(1, 6)))





