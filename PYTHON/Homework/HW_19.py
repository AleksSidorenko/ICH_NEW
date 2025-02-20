# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
# Используйте множества и сортировку букв в слове для проверки на анаграмму.
# Выведите результат на экран.
# Пример переданного списка слов: ['cat', 'dog', 'tac', 'god', 'act']
# Пример вывода: Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']

# def anagrams(l_words):
#     l_words = list(set(l_words))
#     anagram_list = []
#     while l_words:
#         anagram_list1 = []
#         anagram_list2 = []
#         anagram_list1.append(l_words.pop())
#         anagram_list2.append(*anagram_list1)
#         for word in l_words:
#             if sorted(word) == sorted(*anagram_list2):
#                 anagram_list1.append(word)
#                 l_words = set(l_words) - set(anagram_list1)
#         if len(anagram_list1) > 1:
#             anagram_list.append(anagram_list1)
#
#     return anagram_list
#
# list_words = ['spd', 'afd', 'cat', 'qwa', 'eva', 'dog', 'cat', 'rot', 'tac', 'ave', 'ogd', 'kot', 'god', 'ura', 'act', 'opa']
# # list_words = ['vea', 'spd', 'cat',  'afd', 'okt', 'cat', 'qwa', 'tok', 'dog', 'eva', 'dog', 'act', 'cat', 'rot', 'tac', 'ave', 'ogd', 'kot', 'god', 'ura', 'act', 'opa']
# res = anagrams(list_words)
# print(*res, sep = ", ")

# Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет,
# является ли set1 подмножеством set2.
# Функция должна возвращать True, если все элементы из set1 содержатся в set2, и False в противном случае.
# Функция должна быть реализована без использования встроенных методов issubset или <=.
# Пример множеств
# {1, 2, 3}
# {1, 2, 3, 4, 5}
# Пример вывода:
# True
# Option 1
# def is_subset(s1, s2):
#     for i in s1:
#         if i not in s2:
#             return False
#     return True
#
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# print(is_subset(set1, set2))

# Option 2
# def is_subset(s1, s2):
#     return False if { False for i in s1 if i not in s2 } == {False} else True
#
#
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# print(is_subset(set1, set2))