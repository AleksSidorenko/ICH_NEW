# Напишите программу, которая выводит слова «Python is awesome!»
# (без кавычек) 10 раз.
# Программа должна вывести 10 раз текст «Python is awesome!»,
# каждый на отдельной строке.
# text = "Python is awesome!"
# for i in range(10):
#     print(text)

# numbers = [1, 8, 11, 22, 35, 40]
#
# for num in numbers:
#     if num % 5 == 0:
#         print(f"Нашли число, делящееся на 5: {num}")
#         break  # Прерываем цикл после нахождения первого подходящего числа

# numbers = [5, -1, 3, -7, 8]
#
# for num in numbers:
#     if num < 0:
#         continue  # Пропускаем итерацию для отрицательных чисел
#     print(f"Положительное число: {num}")

# numbers = [1, 3, 5, 7]
#
# for num in numbers:
#     if num % 2 == 0:
#         print(f"Нашли четное число: {num}")
#         break
# else:
#     print("Четных чисел нет")

# numbers = [-3, -2, -1, 1, 3, 4, 7]
#
# for num in numbers:
#     if num < 0:
#         continue  # Игнорируем отрицательные числа
#     if num % 2 == 0:
#         print(f"Нашли четное число: {num}")
#         break
# else:
#     print("Четных чисел не найдено")

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
#
# zipped = zip(names, ages)
# print(list(zipped))

# with open('example.txt', 'r', encoding='cp1251') as file:
#     content = file.read()
#     print(content)
#
# with open('example.txt', 'w', encoding='cp1251') as file:
#     file.write("Hello, World!sdfsdfs")
#
# with open('example.txt', 'a', encoding='cp1251') as file:
#     file.write("\nAppending new line.")

# with open("input.txt", "r", encoding="cp1251") as infile:
#     # Считываем все строки из файла
#     lines = infile.readlines()

# Объединяем строки, разделяя их пробелами, чтобы получить весь текст
# full_text = " ".join(lines)

# Разделяем текст на отдельные слова
# words = full_text.split()

# Переворачиваем список слов
# words.reverse()

# Открываем файл output.txt для записи
# with open("output.txt", "w", encoding="cp1251") as outfile:
    # Записываем каждое слово на новой строке
    # for word in words:
    #     outfile.write(word + "\n")

