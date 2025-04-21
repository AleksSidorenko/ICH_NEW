# Aufgabe 1. Wörterbücher
# Schreiben Sie ein Programm, das eine Zeichenkette vom Benutzer abfragt.
# Das Programm soll die Häufigkeit jedes Zeichens in der Zeichenkette zählen
# und die Ergebnisse in einem Wörterbuch speichern,
# wobei der Schlüssel das Zeichen und der Wert die Häufigkeit seines Vorkommens ist.

# def count_characters(string):
#     char_count = {}  # Создаём пустой словарь для хранения частот символов
#     for char in string:
#         char_count[char] = char_count.get(char, 0) + 1  # Увеличиваем счётчик
#     return char_count
#
# user_input = input("Geben Sie eine Zeichenkette ein: ")
# result = count_characters(user_input)
# print(f"{user_input} :", result)

# Объяснение:
# Создаётся пустой словарь char_count.
# Перебираются символы строки,
# увеличивая их частоту в словаре (используется dict.get() для удобства).
# Выводится словарь с частотой символов.

# Aufgabe 2. Ausnahmen: Fehlerbehandlung
# Erstellen Sie ein Programm, das zwei Zahlen vom Benutzer annimmt
# und eine Division durchführt.
# Wenn der Benutzer Null als Divisor eingibt,
# sollte das Programm eine Fehlermeldung ausgeben
# und um die Eingabe eines anderen Divisors bitten.

# def divide_numbers():
#     while True:
#         try:
#             num1 = float(input("Geben Sie die erste Zahl ein: "))
#             num2 = float(input("Geben Sie die zweite Zahl ein: "))
#             result = num1 / num2
#             print(f"Ergebnis: {result}")
#             break  # Если успешное деление, выходим из цикла
#         except ZeroDivisionError:
#             print("Fehler: Division durch Null ist nicht erlaubt! Bitte eine andere Zahl eingeben.")
#         except ValueError:
#             print("Fehler: Bitte eine gültige Zahl eingeben.")
#
# divide_numbers()

# Объяснение:
# Вход в бесконечный цикл, чтобы запрашивать корректный ввод.
# try-except блок:
# ZeroDivisionError: ловит попытку деления на ноль и запрашивает повторный ввод.
# ValueError: ловит ввод нечисловых значений (например, если введён текст).
# После успешного деления программа выводит результат и выходит из цикла.

# Aufgabe 3. Iteratoren, Iterierbare Objekte und Generatoren
# Schreiben Sie einen Generator, der vom Benutzer Anfangs- und Endwerte annimmt
# und nur gerade Zahlen im angegebenen Bereich generiert.
# Verwenden Sie diesen Generator,
# um alle geraden Zahlen vom Anfangs- bis zum Endwert auszugeben.

# def even_numbers(start, end):
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             yield num  # Генерация чётного числа
#
# # Ввод диапазона
# start = int(input("Geben Sie den Startwert ein: "))
# end = int(input("Geben Sie den Endwert ein: "))
#
# # Использование генератора
# print("Gerade Zahlen im Bereich:")
# for even in even_numbers(start, end):
#     print(even, end=" ")

# Объяснение:
# Создаётся генератор even_numbers(), который использует yield для генерации только чётных чисел.
# Пользователь вводит начальное и конечное значение.
# Генератор вызывается в цикле for, выводя только чётные числа.

# Aufgabe 4. Generatoren
# Erstellen Sie einen Generator zur Berechnung der unendlichen Fibonacci-Folge.
# Das Programm soll die ersten 10 Zahlen dieser Folge mit dem Generator ausgeben.

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a  # Возвращаем текущее число Фибоначчи
#         a, b = b, a + b  # Обновляем значения
#
# # Использование генератора для вывода первых 10 чисел Фибоначчи
# fib_gen = fibonacci()
# print("Erste 10 Fibonacci-Zahlen:")
# for _ in range(10):
#     print(next(fib_gen), end=" ")

# Объяснение:
# Генератор fibonacci() бесконечно вычисляет числа Фибоначчи с yield.
# В for-цикле 10 раз вызываем next(fib_gen), получая первые 10 чисел.


# Aufgabe 5. Arbeit mit dem Dateisystem
# Erstellen Sie ein Programm, das eine Textdatei mit dem Namen und dem Alter des Benutzers,
# die über die Tastatur eingegeben wurden, erstellt.
# Anschließend soll das Programm diese Datei lesen
# und die Daten im Format "Name: Name>, Alter: Alter>" ausgeben.

# def save_user_data():
#     name = input("Geben Sie Ihren Namen ein: ")
#     age = input("Geben Sie Ihr Alter ein: ")
#
#     with open("userdata.txt", "w", encoding="utf-8") as file:
#         file.write(f"{name}\n{age}")
#
# def read_user_data():
#     with open("userdata.txt", "r", encoding="utf-8") as file:
#         lines = file.readlines()
#         name, age = lines[0].strip(), lines[1].strip()
#         print(f"Name: {name}, Alter: {age}")
#
# # Выполняем функции
# save_user_data()
# read_user_data()

# Объяснение:
# save_user_data(): запрашивает имя и возраст, записывает их в файл.
# read_user_data(): читает файл и выводит данные в формате "Name: ..., Alter: ...".
# Файл открывается с encoding="utf-8" для корректной работы с символами.

# Aufgabe 6. Einführung in funktionale Programmierung
# Schreiben Sie eine Funktion, die eine Liste von Zeichenketten entgegennimmt
# und nur diejenigen Zeichenketten zurückgibt, die mehr als 5 Zeichen enthalten.
# Verwenden Sie dafür die Funktion Filter.

# def filter_long_strings(strings):
#     return list(filter(lambda s: len(s) > 5, strings))
#
# # Пример использования
# words = ["Apfel", "Banane", "Kiwi", "Erdbeere", "Traube"]
# filtered_words = filter_long_strings(words)
# print("Gefilterte Wörter:", filtered_words)

# Объяснение:
# Используем filter() с lambda s: len(s) > 5, чтобы оставить строки длиной больше 5.
# Преобразуем filter в список и выводим отфильтрованные слова.

