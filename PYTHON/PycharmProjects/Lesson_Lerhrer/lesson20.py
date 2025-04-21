# l = [4, 7, 1, 3, 8]
# print(3 in l)
# s = {4, 7, 1, 3, 8}
# print(3 in s)


# # my_set = [1, 2, 3]
# # my_frozen_set = frozenset(my_set)
# my_set = {4, 5, 6}
# print(type(my_set))
# my_frozen_set = frozenset({4, 5, 6})
# print(type(my_frozen_set))
# print(my_set)
# print(my_frozen_set)
# for el in my_frozen_set:
#     print(el)
# # my_frozen_set.add(4) # Добавление ÿлемента в изменāемое множество
# # my_frozen_set.add(7) # Ошибка, нелþзā добавитþ ÿлемент в неизменāемое множество



# my_list = [x for x in range(5)]
# print([x for x in range(5)])
# print(tuple(my_list))
# print(tuple([x for x in range(5)]))
#
# my_set = {x for x in range(5)}
# print(my_set)

# my_t = (x for x in range(5))  # Не кортеж
# print(my_t)

# s = {4, 7, 1, 3, 8}



# lst = [{"name": "John",
#            "age": 25,
#            "city": "New York",
#            1: "text"},
#        {"name": "Bob",
#         "age": 25,
#         "city": "New York",
#         1: "text"}
#        ]

#
# my_dict = {"names": ["John", "Bob"],
#            "age": 25,
#            "city": "New York",
#            1: "text",
#            (1, 2): "text",
#            frozenset({1, 2, 3}): "text"}
#
# print(my_dict)

# s = {4, 7, 1, 3, 8}
# for i in range(len(s)):
#     print(s[i])
# print(s[0])

# d = {}
# print(d)
# print(type(d))
#
# l = [1, 2, 3]
# # lst_tuples = [("name", "Jane", "Bob"), ("age", 30), ("city", "Minsk")]
# lst_tuples = [["name", "Jane-Doy"], ["age", 30], ["city", "Minsk"]]
# print(dict(lst_tuples))


# my_dict = {"name": "John", "age": 25}
# print("name" in my_dict)
# print("city" in my_dict)
# print("John" in my_dict)

# my_dict = {"name": "John", "age": 25}
# my_dict["city"] = "New York"
# my_dict["age"] = 30
# print(my_dict)
# print(my_dict["city"])
# del my_dict["age"]
# print(my_dict)
# print(my_dict.pop("city"))
# print(my_dict)
#



# my_dict = {"name": "John", "age": 25, "city": "New York"}
# print(my_dict.items())
# print(my_dict.keys())
# values = my_dict.values()
# print(values)
# print(type(values))
# my_dict["new"] = "text"
#
# print(values)


# my_dict = {"name": "John", "age": 25, "city": "New York"}
# for el in my_dict:
#     print(el)
#
# t = (1, 2)
# a, b = t
# print(a)
# print(b)
#
# print(my_dict.items())
# for i in my_dict.items():
#     print(i)
# for key, value in my_dict.items():
#     print(key, value)


# def my_function(*args, **kwargs):
#     print(type(args))
#     print(args)
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key, value)
# my_function(1, 2, 3, name="John", age=25, city="Minsk")
#
#
# my_dict = dict()
# print(my_dict)

# stuff = {1: 'ааа', 2: 'ббб', 3: 'ввв'}
# print(stuff[3])
#
# def func(**kwargs):
#     pass
#
# func({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6})
#
