# d = {1: [1, 2,3], 2:None, 3: ""}
# l = [1,2,3]
# print(l)
# print(d)
#
# if 4 in d:
#     print(d[4])


# my_dict = {"apple": 5, "banana": 2, "orange": 8}
# print(my_dict.get("apple")) # Выводит 5
# print(my_dict.get("grape")) # Выводит None
# print(my_dict.get("grape", 0)) # Выводит 0, так как клĀча "grape" нет в словаре
# print(my_dict.get("apple", 15))
# print(my_dict)


# my_dict = {"apple": 5, "banana": 2, "orange": 8}
# print(my_dict.setdefault("apple", 10))
# print(my_dict.setdefault("grape", 15))
# print(my_dict.setdefault("kiw"))
# print(my_dict.setdefault("kwi"))
# print(my_dict.setdefault("kiwwi"))
# print(my_dict)

# courses = {}
# students = [('Math', 'Alice'), ('Math', 'Bob'), ('Physics', 'Charlie')]
#
# for course, student in students:
#     courses.setdefault(course, []).append(student)
#
# print(courses)  # {'Math': ['Alice', 'Bob'], 'Physics': ['Charlie']}
# print(courses.popitem())
# print(courses)  # {'Math': ['Alice', 'Bob'], 'Physics': ['Charlie']}
#
# from collections import OrderedDict
#
# ordered_dict = OrderedDict()
# ordered_dict["apple"] = 5
# ordered_dict["banana"] = 2
# ordered_dict["orange"] = 8
# print(ordered_dict)
#
# # print(ordered_dict.pop("apple"))
# # print(ordered_dict)
# # print(ordered_dict.popitem(last=False))
# # print(ordered_dict)
# print(ordered_dict.move_to_end("banana"))
# print(ordered_dict)
# print(ordered_dict.move_to_end("banana", last=False))
# print(ordered_dict)



# from collections import OrderedDict
#
# def lru_cache(capacity, cache, key, value):
#     if key in cache:
#         cache.pop(key)
#     elif len(cache) >= capacity:
#         cache.popitem(last=False)
#     cache[key] = value
# capacity = 3
# cache = OrderedDict()
#
# lru_cache(capacity, cache, "key1", "value1")
# lru_cache(capacity, cache, "key2", "value2")
# lru_cache(capacity, cache, "key3", "value3")
# print(cache) # Выводит OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
#
# lru_cache(capacity, cache, "key2", "new_value2") # Обновлāем значение "key2"
# print(cache) # Выводит OrderedDict([('key1', 'value1'), ('key3', 'value3'), ('key2', 'new_value2')])
# lru_cache(capacity, cache, "key4", "value4") # Кÿш переполнен, удалāем "key1"
# print(cache) # Выводит OrderedDict([('key3', 'value3'), ('key2', 'new_value2'), ('key4', 'value4')])
#
# def calculate(nums):
#     pass


from collections import defaultdict

# d = dict()
# my_dict = defaultdict(int)
# print(my_dict)
# my_dict["apple"] = 5
# print(my_dict)
# print(my_dict["banana"])
# print(my_dict)
#
# my_dict = defaultdict(list)
# print(my_dict)
# my_dict["apple"] = [1, 2, 3, 4, 5]
# print(my_dict)
# print(my_dict["banana"])
# print(my_dict)
# print(my_dict["kiwi"].append(1))
# print(my_dict)


# from collections import defaultdict
#
# fish_inventory = [
#     ("Sammy", "shark", "tank-a"),
#     ("Jamie", "cuttlefish", "tank-b"),
#     ("Mary", "squid", "tank-a"),
# ]
#
# tanks = defaultdict(list)
# for name, fish, tank in fish_inventory:
#     tanks[tank].append((name, fish))
# print(tanks)


# from collections import Counter
# my_list = [1, 2, 3, 1, 2, 3, 1, 2, 4, 5, 4, 3, "hello", "a", "b", "a", "a", "a"]
# print(list("hello"))
# my_counter = Counter(my_list)
# print(my_counter)
# print(my_counter.most_common(3))
# print(list(my_counter.elements()))
#
# print(Counter("hello"))


# from collections import namedtuple
# # Создаем именованный кортеж с именами полей 'name' и 'age'
# Person = namedtuple('Person', ['name', 'age'])
# # person1 = ('Alice', 30)
# # person1 = Person(name='Alice', age=30)
# person1 = Person('Alice', 30)
# person2 = Person('Bob', 35)
# # print(person1[0])
# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)


# from collections import namedtuple
# Person = namedtuple("Person", ["name", "age", "city"])
# Person = namedtuple("Person", "name age city")
# person1 = Person("Alice", 30, "New York")
# person2 = Person("Bob", 25, "San Francisco")
# name, age, city = person1
# print(name, age, city)

import json
# Сериализациā Python-объекта в JSON-строку
data = {"name": "John",
        "age": 25,
        "city": "New York",
        "hobby": ("hiking", "swimming"),
        "country": None,
        "is_active": True}
print(data)
json_str = json.dumps(data)
print(type(json_str))
print(json_str) # Выводит '{"name": "John", "age": 25, "city": "New York"}'
# # Десериализациā JSON-строки в Python-объект
# json_str = '{"name": "John", "age": 25, "city": "New York"}'
data = json.loads(json_str)
print(type(data))
print(data)
# print(data["name"]) # Выводит 'John'