# 1. Реализовать класс Counter, который представляет счетчик.
# Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)
# Пример использования:
# counter = Counter(5)
# counter += 3
# print(counter)  # Вывод: 8
# counter -= 2
# print(int(counter))  # Вывод: 6

# class Counter:
#     def __init__(self, value=0):
#         self.value = value
#
#     def __add__(self, other):
#         if isinstance(other, (int, float)):
#             self.value += other
#         else:
#             raise TypeError()
#         return self.value
#
#     def __sub__(self, other):
#         self.value -= other
#         return self.value
#
#     def __str__(self):
#         return f'{self.value}'
#
#     def __int__(self):
#         return int(self.value)
#
#
# counter = Counter(10)
# try:
#     counter += 5
#     print(counter)
#     counter -= 3
#     print(int(counter))
# except TypeError:
#     print("Операция возможна только с числами (int или float).")

# 2. Реализовать класс Email, представляющий электронное письмо.
# Класс должен поддерживать следующие операции:
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)
# Пример использования:
# email1 = Email("john@example.com", "jane@example.com",
# "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
#
# email2 = Email("jane@example.com", "john@example.com", "Re: Meeting",
# "Sure, let's meet at 2 PM.", "2022-05-10")
#
# email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob,
# how are you?", "2022-05-09")
# print(email1)  # Вывод:
# """
# From: john@example.com
# To: jane@example.com
# Subject: Meeting
# Hi Jane, let's have a meeting tomorrow.
# """
# print(len(email2))  # Вывод: 24
# print(hash(email3))  # Вывод: -920444056
# print(bool(email1))  # Вывод: True
# print(email2 > email3)  # Вывод: True

# from functools import total_ordering
# from datetime import datetime

# class Email:
#     def __init__(self, sender, recipient, subject, text, date):
#         self.sender = sender
#         self.recipient = recipient
#         self.subject = subject
#         self.text = text
#         self.date = datetime.strptime(date, "%Y-%m-%d")
#
#         # self.date = self.parse_date(date)  # Преобразуем строку в объект datetime.date
#
#     # def parse_date(self, date_str):
#     #     """Парсит дату из строки (поддерживает разные разделители)"""
#     #     for fmt in ("%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d"):
#     #         try:
#     #             return datetime.strptime(date_str, fmt).date()
#     #         except ValueError:
#     #             continue
#     #     raise ValueError(f"Неподдерживаемый формат даты: {date_str}")
#
#     def __eq__(self, other):
#         return self.date == other.date
#
#     def __gt__(self, other):
#         return self.date > other.date
#
#     def __str__(self):
#         return (f"\"\"\" \nОт:   \033[1m {self.sender}\033[0m\n"
#                 f"Кому:  \033[1m{self.recipient}\033[0m\n"
#                 f"Тема:  \033[1m{self.subject}\033[0m\n"
#                 f"Текст: \033[1m{self.text}\033[0m\n"
#                 f"Дата:  \033[1m{self.date}\033[0m\n\"\"\"")
#
#     def __len__(self):
#         return len(self.text)
#
#     def __hash__(self):
#         return hash((self.sender, self.recipient, self.subject, self.text, self.date))
#
#     def __bool__(self):
#         return bool(self.text)
#
# email1 = Email("john@example.com", "jane@example.com",
# "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
# email2 = Email("jane@example.com", "john@example.com", "Re: Meeting",
# "Sure, let's meet at 2 PM.", "2022-05-10")
# email3 = Email("alice@example.com", "bob@example.com", "Hello",
# "Hi Bob, how are you?", "2022-05-09")
#
# print(email1)
# print(f'Длина текста письма "email2": {len(email2)}')
# print(f'Xеш-значения письма "email3": {hash(email3)}')
# print(f'Проверка наличия текста в письме "email1": {bool(email1)}')
# print(f'Сравнение писем "email2 и email3" по дате: {email2.date} <  {email3.date}: {email2.date <  email3.date}')
# print(f'Сравнение писем "email2 и email3" по дате: {email2.date} >  {email3.date}: {email2.date >  email3.date}')
# print(f'Сравнение писем "email2 и email3" по дате: {email2.date} <= {email3.date}: {email2.date <= email3.date}')
# print(f'Сравнение писем "email2 и email3" по дате: {email2.date} >= {email3.date}: {email2.date >= email3.date}')
# print(f'Сравнение писем "email2 и email3" по дате: {email2.date} == {email3.date}: {email2.date == email3.date}')
# print(f'Сравнение писем "email2 и email3" по дате: {email2.date} != {email3.date}: {email2.date != email3.date}')

