# 1. Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию,
# а также методы calculate_area() для вычисления площади прямоугольника и
# calculate_perimeter() для вычисления периметра прямоугольника.
# Переопределить методы __str__, __repr__.
# Затем создайте экземпляр класса Rectangle и
# выведите информацию о нем, его площадь и периметр.

# class Rectangle:
#
#     def __init__(self, width=0, height=0):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     def calculate_perimeter(self):
#         return (self.width + self.height) * 2
#
#     def __str__(self):
#         return f'Прямоугольник: ширина={self.width}, высота={self.height}'
#
#     def __repr__(self):
#         return f'Rectangle(width={self.width!r}, height={self.height!r})'
#
# rectangle = Rectangle(5,3)
# print(rectangle)
# print(f'Площадь прямоугольника: {rectangle.calculate_area()}')
# print(f'Периметр прямоугольника: {rectangle.calculate_perimeter()}')
# print(f'Прямоугольник: {rectangle!r}')

# 2. Создайте класс BankAccount для представления банковского счета.
# Класс должен иметь атрибуты account_number (номер счета) и balance (баланс),
# а также методы deposit() для внесения денег на счет и withdraw() для снятия денег со счета.
# Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите часть денег.
# Выведите оставшийся баланс.
# Не забудьте предусмотреть вариант, при котором при снятии баланс может стать меньше нуля.
# В этом случае уходить в минус не будем,
# вместо чего будем возвращать сообщение "Недостаточно средств на счете".

# class BankAccount:
#
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount  > self.balance:
#             print(f'Недостаточно средств на счете: {self.account_number}')
#         else:
#             self.balance -= amount
#
# bankAccount = BankAccount('DE0123456789', 1000)
# bankAccount.deposit(500)
# bankAccount.withdraw(1600)
# print(f'Баланс счета: {bankAccount.account_number} составляет: {bankAccount.balance} Euro')


# emoji = "😊"
# print(f"str: {emoji!s}")   # str: 😊
# print(f"repr: {emoji!r}")  # repr: '😊'
# print(f"ascii: {emoji!a}") # ascii: '\U0001f60a'