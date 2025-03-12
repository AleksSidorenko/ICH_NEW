# courses = {}
# students = [('Math', 'Alice'), ('Math', 'Bob'), ('Physics', 'Charlie')]
#
# for course, student in students:
#     courses.setdefault(course, []).append(student)
#
# print(courses)  # {'Math': ['Alice', 'Bob'], 'Physics': ['Charlie']}

# Дана строка.
# Посчитайте в ней частоту встречаемости всех букв. Считаем, что в строке могут быть
# пробельные символы.

# from collections import Counter
# def count_words(text):
#     x = Counter(text)
#     for w in list(x.keys()):
#         if not (w.isspace() or w.isalpha()):
#             x.pop(w)
#
#     return x
#
# s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est."
# print(count_words(s))

# Реализуйте функцию, которая принимает словарь задач с категориями и группирует задачи по их категориям.
# {
# 'работа': ['task1', 'task4'],
# 'учёба': ['task2', 'task5'],
# 'развлечения': ['task3']
# }
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

# def group_tasks(tasks):
#     groups = defaultdict(list)
#     for key, value in tasks.items():
#         groups[value].append(key)
#
#     return groups
#
#
# tasks = {
# "task1": "работа",
# "task2": "учёба",
# "task3": "развлечения",
# "task4": "работа",
# "task5": "учёба"
# }
# print(group_tasks(tasks))

# Дан текст.
# Необходимо посчитать сколько раз встретилось каждое слово и вывести в топ слов,
# упорядоченный сначала по убыванию встречаемости, а при равенстве частот в соответствии с
# упорядочиванием в лексикографическом порядке.
# Решить задачу с помощью использования изученных классов.

# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.'
#
# clean_text = text.replace(',', '').replace('.', '').lower().split()
# #print(clean_text)
# my_counter = Counter(clean_text)
# #print(my_counter)
#
# sorted_counter = sorted(my_counter.items(), key=lambda x: (-x[1], x[0]))
# print(sorted_counter)
