# Aufgabe 1. Grundlegende Sammlungen. Listen
# Schreiben Sie ein Programm, das eine Liste von Zahlen vom Benutzer annimmt
# und dann Folgendes ausgibt:
# 1. Eine Liste aller einzigartigen Zahlen in der Reihenfolge ihres Auftretens.
# 2. Die Anzahl der Elemente in der ursprünglichen Liste und die Anzahl der einzigartigen Elemente.

# def unique_numbers():
#     numbers = input("Geben Sie eine Liste von Zahlen ein (getrennt durch Leerzeichen): ").split()
#     numbers = list(map(int, numbers))  # Преобразуем в список чисел
#
#     unique_list = []  # Список для уникальных чисел
#     for num in numbers:
#         if num not in unique_list:
#             unique_list.append(num)
#
#     print("Einzigartige Zahlen in Reihenfolge des Auftretens:", unique_list)
#     print("Anzahl der Elemente in der ursprünglichen Liste:", len(numbers))
#     print("Anzahl der einzigartigen Elemente:", len(unique_list))
#
# unique_numbers()

# Объяснение:
# Получаем ввод, разделяем по пробелам и конвертируем в int.
# Создаём unique_list, добавляя в неё только новые элементы.
# Выводим уникальные числа, размер исходного списка и количество уникальных элементов.

# Aufgabe 2. Listenmethoden, Tupel
# Schreiben Sie ein Programm, das fünf Zahlen vom Benutzer annimmt, sie zu einer Liste hinzufügt
# und anschließend ein Tupel mit den einzigartigen Werten aus der Liste erstellt und das Tupel ausgibt.

# def list_to_tuple():
#     numbers = []
#     for _ in range(5):
#         num = int(input("Geben Sie eine Zahl ein: "))
#         numbers.append(num)
#     unique_tuple = tuple(set(numbers))  # Преобразуем список в множество, затем в кортеж
#     print("Einzigartige Werte als Tupel:", unique_tuple)
#
# list_to_tuple()

# Объяснение:
# Запрашиваем 5 чисел у пользователя и сохраняем их в список.
# Преобразуем список в множество (убираем дубликаты) и затем в кортеж.
# Выводим кортеж уникальных значений.

# Aufgabe 3. Listenverständnis
# Erstellen Sie eine Liste von Zahlen von 1 bis 20 mithilfe eines Listen-Komprehensionsausdrucks
# und geben Sie eine neue Liste aus,
# die nur die geraden Zahlen aus dieser Liste enthält, wobei diese im Quadrat dargestellt werden.

# numbers = [i for i in range(1, 21)]  # Список чисел от 1 до 20
# even_squares = [i**2 for i in numbers if i % 2 == 0]  # Квадраты чётных чисел
#
# print("Quadrate der geraden Zahlen:", even_squares)

# Объяснение:
# numbers = [i for i in range(1, 21)] создаёт список от 1 до 20.
# even_squares = [i**2 for i in numbers if i % 2 == 0] формирует новый список,
# оставляя только чётные числа и возводя их в квадрат.
# Выводим список квадратов чётных чисел.


# Aufgabe 4. Verschachtelte Funktionen. Lambda-Funktionen
# Schreiben Sie eine Funktion, die eine Liste von zweistelligen Zahlen entgegennimmt
# und eine neue Liste zurückgibt, die nach der zweiten Ziffer sortiert ist.
# Verwenden Sie eine Lambda-Funktion innerhalb der Hauptfunktion, um diese Aufgabe auszuführen.

# def sort_by_second_digit(numbers):
#     return sorted(numbers, key=lambda x: x % 10)  # Сортировка по последней цифре числа
#
# # Пример использования
# numbers = [23, 87, 45, 91, 32, 67]
# sorted_numbers = sort_by_second_digit(numbers)
# print("Sortierte Liste:", sorted_numbers)

# Объяснение:
# Используем sorted() с lambda x: x % 10, чтобы сортировать по последней цифре.
# x % 10 даёт вторую цифру числа (например, для 23 — это 3).
# Функция возвращает отсортированный список.

# Aufgabe 5. Rekursion
# Implementieren Sie eine rekursive Funktion zur Berechnung der Summe aller Zahlen in einer Liste.
# Das Programm sollte Zahlen vom Benutzer abfragen, eine Liste erstellen
# und die Summe der Elemente unter Verwendung der Rekursion ausgeben.

# def recursive_sum(numbers):
#     if not numbers:
#         return 0  # Базовый случай: если список пуст, сумма = 0
#     return numbers[0] + recursive_sum(numbers[1:])  # Рекурсивно складываем элементы
#
# # Ввод данных
# user_input = input("Geben Sie eine Liste von Zahlen ein (getrennt durch Leerzeichen): ")
# numbers = list(map(int, user_input.split()))  # Преобразуем ввод в список чисел
#
# # Вычисление и вывод суммы
# print("Summe der Zahlen:", recursive_sum(numbers))

# Объяснение:
# Базовый случай: если список пуст, возвращаем 0.
# В противном случае берём первый элемент и рекурсивно суммируем остальные.
# Пользователь вводит числа, программа разбивает строку и конвертирует элементы в int.

# Aufgabe 6. Mengen
#  Erstellen Sie ein Programm, das zwei Listen von Zahlen vom Benutzer entgegennimmt,
#  Mengen daraus bildet und die Schnittmenge, die Vereinigung
#  und die Differenz der Elemente dieser Mengen in beide Richtungen ausgibt.

# def set_operations():
#     set1 = set(map(int, input("Geben Sie die erste Liste von Zahlen ein: ").split()))
#     set2 = set(map(int, input("Geben Sie die zweite Liste von Zahlen ein: ").split()))
#
#     print("Schnittmenge (Intersection):", set1 & set2)
#     print("Vereinigung (Union):", set1 | set2)
#     print("Differenz (Set1 - Set2):", set1 - set2)
#     print("Differenz (Set2 - Set1):", set2 - set1)

# set_operations()

# Объяснение:
# set(map(int, input().split())) превращает ввод пользователя в множество чисел.
# set1 & set2 — пересечение (общие элементы).
# set1 | set2 — объединение (все уникальные элементы).
# set1 - set2 — разность (элементы set1, которых нет в set2).
# set2 - set1 — разность (элементы set2, которых нет в set1).