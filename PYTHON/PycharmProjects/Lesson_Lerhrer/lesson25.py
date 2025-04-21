# x = 5
# x: str = 5
# print(x)
# print(type(x))


# def mult(a: int, b: str) -> int:
#     return a * b
#
# print(mult(5, "!"))
# # print(add(5, "6"))



from typing import Optional, Union, Any
from typing import List, Dict, Tuple
import typing
#
# def word_multiply(t: str, amount: int) -> str:
#     if t:
#         return t * amount
#     else:
#         return None
#
# text = 'python'
# print(word_multiply(text, 2)) # => python
# print(word_multiply(text, 0)) # =>
#
# def greet(name: Optional[str]) -> str:
#     if name is None:
#         return "Hello, anonymous"
#     else:
#         return f"Hello, {name}"



# from typing import List, Tuple, Set, Dict, Union
#
# def process_data(data: list[str]) -> tuple[int, set[str]]:
#     # Обработка данных
#     return len(data), set(data)
#
# def get_person_details(person: Dict[str, Union[str, int]]) -> str:
#     # Получение информации о человеке
#     return f"{person['name']}, {person['age']} years old"


# from operator import add, sub, mul, truediv
# result = add(5, 3) # Результат: 8
# print(result)
# result = sub(10, 2) # Результат: 8
# print(result)
# result = mul(2, 4) # Результат: 8
# result = truediv(16, 2) # Результат: 8.0
#
# from operator import itemgetter
# data = [
#  {'name': 'Alice', 'age': 25},  # 25
#  {'name': 'Bob', 'age': 30},  # 30
#  {'name': 'Charlie', 'age': 20}  # 20
# ]
# sorted_data = sorted(data, key=itemgetter('age'), reverse=True)
# print(sorted_data)
#
# # [1, 2, 6, 8, 11, 16]



# from bisect import bisect_left, bisect_right

# # data1 = [1, 3, 5, 7, 9]
# # data2 = [1, 3, 6, 7, 9]
# data2 = [1, 3, 6, 6, 6, 6, 7, 9]
# # index = bisect_left(data1, 6) # Результат: 3
# # index = bisect_right(data1, 6) # Результат: 3
# index = bisect_left(data2, 6)
# print(index)
# index = bisect_right(data2, 6)
# print(index)
# index = bisect_right(data2, 2)
# print(index)
# index = bisect_left(data2, 2)
# print(index)


# from bisect import bisect_left, bisect_right
#
# #                                F    D   C   B    A
# def grade_right(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect_right(breakpoints, score)
#     return grades[i]
# #                                F    D   C   B    A
# def grade_left(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect_left(breakpoints, score)
#     return grades[i]
#
# print([grade_right(score) for score in [33, 99, 77, 70, 89, 90, 100]])
# print([grade_left(score) for score in [33, 99, 77, 70, 89, 90, 100]])
#

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


