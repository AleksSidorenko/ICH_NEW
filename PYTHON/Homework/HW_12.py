# 1. Напишите программу, которая запрашивает у пользователя число N
# и выводит на экран таблицу умножения от 1 до N.
# Используйте вложенный цикл for для создания таблицы умножения.
# Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите число N: 5
# Таблица умножения:
# Option 1
# n = int(input("Введите число n: "))
# l_n = len(str(n * n))
# t = "Таблица умножения:"
# l_t = len(t)
# print(t)
# for i in range(1, n+1):
#     print(end = " " * l_t)
#     for j in range(1, n+1):
#         print(f"{(i * j):>{l_n}}", end = "  ")
#         # print(f"{(i * j):2d}", end="  ")
#     print("\n")

# Option 2
# N = int(input("Введите число n: "))
# L=len(str(N*N))+2
# s = "Таблица умножения:"
# print(s)
# for i in range(1, N + 1):
#     for j in range(1,N+1):
#         print(f"{i*j:{L}d}",end="")
#     print("\n")

# my_list = [1, 2, 3, 4, 5]
# for c, value in enumerate(my_list, 1):
#     print(c, value) # , end='')

# 2. Напишите программу, которая принимает два списка одинаковой длины и создает новый список,
# содержащий пары элементов из исходных списков. Используйте функцию zip() для создания пар элементов.
# Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите элементы первого списка, разделенные пробелом: 1 2 3 4 5
# Введите элементы второго списка, разделенные пробелом: A B C D E
# Список пар элементов: [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]
# Option 1
# l = input('Введите элементы первого списка, разделенные пробелом: ').split()
# l1 = input('Введите элементы второго списка, разделенные пробелом: ').split()
# print("Список пар элементов: ", list(zip(map(int, l),l1))) # map(int...) чтобы выводилось без кавычек, согласно примеру вывода
# # Option 2
# l = map(int, input('Введите элементы первого списка, разделенные пробелом: ').split())
# l1 = input('Введите элементы второго списка, разделенные пробелом: ').split()
# print("Список пар элементов: ", list(zip(l,l1)))