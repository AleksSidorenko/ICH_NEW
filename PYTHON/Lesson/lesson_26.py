# list_city = ['London', 'Berlin', 'Paris']
# list_numbers1 = [1, 2, 3, 4, 5]
# list_numbers2 = [1, 3, 2.5, 10.2]
# list_numbers3 = [1, 'abc', 3.5, True, list_city]
# print(list_city[0])
# print(list_numbers1[1:4])
# print(list_city[::-1])

# list_city[0] = 'Wien'
# a = []
# b = list()
# print(a, b)
#
# a = list('Berlin')
# print(a)

# print(len(list_numbers1))
# print(max(list_numbers1))
# print(min(list_numbers1))
# print(sum(list_numbers1))
# print(sorted(list_numbers1))
# print(sorted(list_numbers1, reverse=True))
#
# a = ['Berlin']
# print(sorted(a))
#
# a = [] # Пустой список
#
# b = list() # И это пустой список
# print(a)
#
# print(b)
#
# s = list('Berlin')
# print(s) # Итог - список из букв строки ['B', 'e', 'r', 'l', 'i', 'n']
# print(['Berlin']) # Итог ['Berlin']
#
# print(len(list_numbers1)) # 5 = длина списка
# print(max(list_numbers1)) # 9
# print(min(list_numbers1)) # 1
# print(sum(list_numbers1)) # 19
# print(sorted(list_numbers1)) # 19
#
# print(sorted(list_numbers1, reverse=True)) # [9, 9, 4, 3, 2, 1] - сортировка по убыванию
##########
# num = input("Enter a number: ").split()
# num_int =[]
# print(num)
# for i in num:
#     print(i)
#     i = int(i)
#     num_int.append(i)
#     # num_int.append(i**2)
# print(num_int)
###############
# my_list = ["apple", "banana", "cherry"]
# my_list1 = [1, 2, 3]
# my_list1.extend(my_list1)
# print(my_list1)
# result = '*:'.join(my_list)
# print(result)
######################
# a = list('список')
# print(a)
######################
# s = []  # Пустой список
# print(s)
# l = ['s', 'p', ['isok'], 2]
# print(l) # ['s', 'p', ['isok'], 2]
######################
# c = [c * 3 for c in 'list']
# print(c) # ['lll', 'iii', 'sss', 'ttt']
######################
# c = [c * 3 for c in 'list' if c != 'i']
# print(c) # ['lll', 'sss', 'ttt']
# c = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']
# print(c) # ['ls', 'lp', 'lm', 'ss', 'sp', 'sm', 'ts', 'tp', 'tm']
#######################
# l = [1, 2, 3, 5, 7]
# print(l) # [1, 2, 3, 5, 7]
# l = l.sort()
# print(l) # None
######################
# a = [66.25, 333, 333, 1, 1234.5]
# print(a.count(333), a.count(66.25), a.count('x')) # 2 1 0
# a.insert(2, -1)
# a.append(333)
# print(a) # [66.25, 333, -1, 333, 1, 1234.5, 333]
# a.index(333) # 1
# a.remove(333)
# print(a) # [66.25, -1, 333, 1, 1234.5, 333]
# a.reverse()
# print(a) # [333, 1234.5, 1, 333, -1, 66.25]
# a.sort()
# print(a) # [-1, 1, 66.25, 333, 333, 1234.5]
######################
# numbers = [i for i in range(1,6)]
# print(numbers) # [1, 2, 3, 4, 5]
######################
# Операции над списками Python
# x in l — true, если элемент x есть в списке l;
# x not in l — true, если элемент x отсутствует в l;
# l1 + l2 — объединение двух списков;
# l * n , n * l — копирует список n раз;
# len(l) — количество элементов в l;
# min(l) — наименьший элемент;
# max(l) — наибольший элемент;
# sum(l) — сумма чисел списка;
# for i in list() — перебирает элементы слева направо.
###########################
# a = ['a', 2.5, [0,3]]
# for x in list(a): print(x)
############################
# numbers = [1, 5, 9, 6, 1, 2, 1]
# print(numbers.index(1)) # вывод 0: первая найденная единица на позиции 0
#
# numbers = [1, 5, 9, 6, 1, 2, 1]
# print(numbers.count(1)) # вывод 3, потому что единица встречается 3 раза
#
# numbers = [1, 5, 9, 6]
# numbers.append(3) # Добавляет указанное значение в конец:
# print(numbers) # обновлённый список: [1, 5, 9, 6, 3]

# Сортирует список в Пайтоне. По умолчанию от меньшего к большему:
# numbers = [1, 5, 9, 6]
# numbers.sort()
# print(numbers) # обновлённый список: [1, 5, 6, 9]
# Также можно сортировать последовательность элементов от большего к меньшему:
# numbers = [1, 5, 9, 6]
# numbers.sort(reverse = True)
# print(numbers) # обновлённый список: [9, 6, 5, 1]

# Вставляет элемент перед указанным индексом:
# numbers = [1, 5, 9, 6]
# numbers.insert(3, [2, 3])
# print(numbers) # обновлённый список: [1, 5, 9, [2, 3], 6]

# Удаляет первое попавшееся вхождение элемента в списке Python:
# numbers = [1, 5, 9, 6, 1, 2, 1]
# numbers.remove(1)
# print(numbers) # обновлённый список: [5, 9, 6, 1, 2, 1]

# Подобно методу append(), добавляет элементы, но преимущество метода extend() в том,
# что он также позволяет добавлять списки:
# numbers = [1, 5, 9, 6]
# numbers.extend([2, 3])
# print(numbers) # обновлённый список: [1, 5, 9, 6, 2, 3]

# данный метод удаляет элемент в конкретно указанном индексе,
# а также выводит удалённый элемент. Если индекс не указан, метод по умолчанию удалит последний элемент:
# numbers = [1, 5, 9, 6]
# numbers.pop(1)
# print(numbers) # получаем: [1, 9, 6]

# Преобразовывает список в строку. Разделитель элементов пишут в кавычках перед методом,
# а сам список Питона должен состоять из строк:
# mylist = ['сайт', 'типичный', 'программист']
# print(', '.join(mylist)) # вывод 'сайт, типичный, программист'

