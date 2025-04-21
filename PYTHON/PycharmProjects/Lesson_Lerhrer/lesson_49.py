# 1) Напишите функцию, которая принимает список строк и возвращает наибольшую строку из
# списка.
# Функция должна быть аннотирована с помощью аннотаций типов.

# 2) Напишите функцию, которая принимает список словарей и ключ, по которому нужно
# отсортировать список словарей.
# Функция должна быть аннотирована с помощью аннотаций типов.

# from typing import Any
# from operator import itemgetter
#
# def sort_dict(users_data: list[dict[str, Any]], key_fact: str) -> list[dict[str, Any]]:
#     return sorted(users_data, key=itemgetter(key_fact))
#
#
# data = [
# {'name': 'Alice', 'age': 25},
# {'name': 'Bob', 'age': 30},
# {'name': 'Charlie', 'age': 20}
# ]
# print(sort_dict(data, 'age'))

# 3. Напишите функцию, которая принимает список строк и возвращает словарь,
# где ключи — строки, а значения — длина этих строк.
# Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.

# def convert_str_to_dict(strings_list: list[str]) -> dict[str, int]:
#     return {element: len(element) for element in strings_list}
#
# print(convert_str_to_dict(["apple", "banana", "cherry"]))

# 4. Напишите функцию, которая принимает имя пользователя и необязательный список его достижений.
# Если список пуст, возвращается сообщение "Нет достижений".
# Если список не пуст, возвращается строка с перечислением достижений.
# Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения



# 5. Напишите генератор, который принимает на вход поток элементов и выдает только уникальные
# элементы, сохраняя их порядок встречаемости (для уже повторяющихся элементов генератор
# не выдает ничего)

def generate_unique_elements():
    temp=[]
    digit = yield
    while True:
        if digit not in temp:
            temp.append(digit)
            digit = yield digit
        else:
            digit = yield None

gen = generate_unique_elements()
next(gen)
for i in range(3):
    user_input = int(input("enter a num: "))
    print(gen.send(user_input))
gen.close()

from typing import Iterable
# def generate_unique_elements():  # -> Iterable[int | None]:
#     try:
#         temp=[]
#         digit = yield
#         while True:
#             if digit not in temp:
#                 temp.append(digit)
#                 digit = yield digit
#             else:
#                 digit = yield None
#     except GeneratorExit:
#         print(temp)
#
# gen = generate_unique_elements()
# next(gen)
# for i in range(3):
#     user_input = int(input("enter a num: "))
#     print(gen.send(user_input))
# gen.close()


def generate_unique_elements():
    temp = []
    digit = yield
    while True:
        if digit not in temp:
            temp.append(digit)
            digit = yield digit * 2
            print("-----")
        else:
            digit = yield None
            print("+++++")

gen = generate_unique_elements()
next(gen)
for i in range(3):
    user_input = int(input("enter a num: "))
    print(gen.send(user_input))









