"""
❗ Übung 1:
1. Verwenden Sie collections.Counter,
um die Anzahl jedes Zeichens in einer Zeichenkette zu zählen.
Schreiben Sie eine Funktion count_characters, die eine Zeichenkette annimmt
und ein Counter-Objekt mit der Anzahl der einzelnen Zeichen zurückgibt.
Geben Sie anschließend die 3 am häufigsten vorkommenden Zeichen aus.
Lösung:
Zeichen zählen mit Counter
Задача: Посчитать количество каждого символа в строке и вывести 3 самых частых.
"""
# from collections import Counter
"""
DE: Wir importieren Counter aus dem Modul collections.
RU: Импортируем Counter из модуля collections.
DE: Counter ist eine spezielle Datenstruktur aus dem Modul collections, 
die automatisch die Häufigkeit von Elementen zählt.
RU: Counter — это специальная структура из модуля collections, 
которая автоматически считает частоту элементов.
Warum benutzen wir Counter? / Почему мы используем Counter?
DE: Counter erleichtert das Zählen von Zeichen oder Wörtern.
Anstatt eine eigene Zähllogik mit Schleifen zu schreiben, genügt ein einfacher Funktionsaufruf.
Die Methode most_common(n) gibt die n häufigsten Elemente direkt zurück.
RU: Counter упрощает подсчёт символов или слов.
Вместо ручного счёта через циклы можно просто передать строку.
Метод most_common(n) сразу выдаёт n самых частых элементов.
Zusammenfassung / Итог:
Counter spart Zeit und Code beim Zählen und ist die ideale Lösung 
für statistische Auswertungen von Zeichen.
"""
# def count_characters(text):
#     counter = Counter(text)
#     return counter
"""
DE: Wir definieren eine Funktion count_characters,
die einen Text (eine Zeichenkette) als Parameter nimmt.
Mit Counter(text) zählen wir, wie oft jedes Zeichen vorkommt.
Das Ergebnis wird zurückgegeben.
RU: Определяем функцию count_characters, принимающую строку.
С помощью Counter(text) считаем количество вхождений каждого символа.
Возвращаем результат.
"""
# text = "collections in python are very useful"
# counter = count_characters(text)
# print("Top 3 häufigste Zeichen:", counter.most_common(3))
"""
DE: Wir rufen die Funktion mit einer Beispielzeichenkette auf.
most_common(3) gibt die 3 häufigsten Zeichen zurück.
Das Ergebnis wird ausgegeben.
RU: Вызываем функцию с примерной строкой.
most_common(3) возвращает 3 самых частых символа.
Печатаем результат.
"""

"""
2. Verwenden Sie collections.deque, um eine Warteschlange mit fester Länge zu erstellen.
Schreiben Sie eine Funktion fixed_queue, die eine Liste von Zahlen
und die maximale Länge der Warteschlange annimmt,
die Elemente der Liste zur Warteschlange hinzufügt
und den endgültigen Zustand der Warteschlange zurückgibt.

** Задание: **
Используйте `collections.deque`, чтобы создать ** очередь фиксированной длины **.
Напишите функцию `fixed_queue`, которая принимает ** список чисел ** и ** максимальную
длину очереди **, добавляет элементы списка в очередь и возвращает ** итоговое
состояние очереди **.
## 🧠 Lösungsmethode 
#### 🇩🇪 Deutsch:
Zur Lösung dieser Aufgabe verwenden wir die Klasse `deque` aus dem Modul `collections`.
Ein `deque`(double - ended queue) erlaubt das ** Hinzufügen und
Entfernen ** von Elementen an beiden Enden — vorne und hinten.
Wenn wir ein `deque` - Objekt mit dem Parameter `maxlen = N ` erstellen,
dann bleibt seine Länge ** automatisch begrenzt auf `N` **.
Wird ein neues Element hinzugefügt, während die maximale Länge erreicht ist,
wird das ** älteste Element(ganz vorne) ** automatisch entfernt.
Wir definieren eine Funktion `fixed_queue(liste, max_len)`,
die alle Elemente aus der Liste `liste` in die Queue einfügt,
und schließlich die aktuelle Queue als Liste zurückgibt.
#### 🇷🇺 Перевод:
Для решения этой задачи мы используем класс deque из модуля collections.
deque (двусторонняя очередь) позволяет добавлять и 
удалять элементы с обеих сторон — с начала и с конца.
Если создать объект deque с параметром maxlen=N,
его длина будет автоматически ограничена N.
Если добавить новый элемент при полной длине,
то самый старый элемент (в начале) будет автоматически удалён.
Мы определим функцию fixed_queue(liste, max_len),
которая поочерёдно добавляет все элементы из списка liste в очередь,
а затем возвращает текущее состояние очереди в виде списка.
## ✅ 
# DE: Wir importieren die Klasse deque aus dem Modul collections
# RU: Импортируем класс deque из модуля collections
from collections import deque


# DE: Wir definieren eine Funktion mit zwei Parametern:
#   1. liste – die Eingangsdaten (Liste von Zahlen)
#   2. max_len – maximale Länge der Warteschlange
# RU: Определяем функцию с двумя параметрами:
#   1. liste – входные данные (список чисел)
#   2. max_len – максимальная длина очереди
def fixed_queue(liste, max_len):
    # DE: Wir erstellen ein deque-Objekt mit fester Länge
    # Klammer auf: Konstruktoraufruf
    # maxlen=max_len – Begrenzung der Länge
    # Klammer zu: Objekt ist erstellt
    # RU: Создаём объект deque с фиксированной длиной
    # Открываем скобку: вызов конструктора
    # maxlen=max_len – ограничение длины
    # Закрываем скобку: объект создан
    queue = deque(maxlen=max_len)

    # DE: Wir fügen alle Elemente der Liste zur Queue hinzu
    # RU: Добавляем все элементы списка в очередь
    for element in liste:
        # DE: Append fügt das Element ans Ende der Queue an
        # Wenn die maximale Länge erreicht ist, wird das vorderste Element entfernt
        # RU: append добавляет элемент в конец очереди
        # Если длина превышена, то первый (самый старый) элемент удаляется
        queue.append(element)

    # DE: Wir geben den endgültigen Zustand der Queue als Liste zurück
    # RU: Возвращаем итоговое состояние очереди как список
    return list(queue)

### 🧪 Пример использования:

zahlen = [1, 2, 3, 4, 5]
maximale_laenge = 3
print(fixed_queue(zahlen, maximale_laenge))

### ✅ Вывод: [3, 4, 5]


"""
"""
3. Verwenden Sie collections.defaultdict, um ein Wörterbuch zu erstellen,
bei dem jeder Schlüssel mehrere Werte haben kann (zum Beispiel eine Liste).
Schreiben Sie eine Funktion group_by_first_letter,
die eine Liste von Wörtern annimmt und sie nach dem ersten Buchstaben gruppiert,
wobei defaultdict verwendet wird.
Lösung:
Wörter gruppieren mit defaultdict
Задача: Группировать слова по первой букве.
"""
# from collections import defaultdict
"""
DE: Wir importieren defaultdict.
RU: Импортируем defaultdict.
DE: defaultdict ist ein Dictionary, das automatisch Standardwerte für neue Schlüssel erzeugt.
RU: defaultdict — это словарь, который автоматически создаёт значение по умолчанию для новых ключей.
Warum benutzen wir defaultdict(list)? / Почему мы используем defaultdict(list)?
DE: Bei normalem dict müssten wir prüfen, ob ein Schlüssel existiert, bevor wir Werte hinzufügen.
Mit defaultdict(list) entfällt diese Prüfung, da beim ersten Zugriff 
auf einen neuen Schlüssel eine leere Liste erstellt wird.
Ideal zum Gruppieren von Elementen (z.B. nach Anfangsbuchstaben).
RU: В обычном словаре нужно проверять, существует ли ключ, прежде чем добавлять значения.
defaultdict(list) создаёт пустой список при первом обращении к новому ключу.
Отлично подходит для группировки по признакам (например, по первой букве).
Zusammenfassung / Итог:
defaultdict ist elegant und effizient für Aufgaben mit Gruppenbildung oder mehrwertigen Schlüsseln.
"""
# def group_by_first_letter(words):
#     grouped = defaultdict(list)
#     for word in words:
#         if word:
#             first_letter = word[0].lower()
#             grouped[first_letter].append(word)
#     return grouped
"""
DE: Funktion erhält eine Liste von Wörtern.
Wir erstellen ein defaultdict, das Listen als Standardwert verwendet.
Für jedes Wort prüfen wir, ob es nicht leer ist.
Der erste Buchstabe (kleingeschrieben) wird als Schlüssel genutzt.
Das Wort wird der passenden Liste hinzugefügt.
Am Ende geben wir das gruppierte Dictionary zurück.
RU: Функция принимает список слов.
Создаём defaultdict, в котором по умолчанию значения — списки.
Для каждого слова (если оно не пустое) берём первую букву.
Приводим её к нижнему регистру и используем как ключ.
Добавляем слово в соответствующий список.
Возвращаем сгруппированный словарь.
"""
# words = ["Apfel", "Banane", "Avocado", "Birne", "Ananas", "Brombeere"]
# grouped_words = group_by_first_letter(words)
# for letter, group in grouped_words.items():
#     print(f"{letter}: {group}")
"""
DE: Wir testen die Funktion mit deutschen Fruchtnamen. Die Ausgabe zeigt Gruppen nach Anfangsbuchstaben.
RU: Тестируем с названиями фруктов. На выходе получаем группы по первой букве.
"""


"""
4. Erstellen Sie ein benanntes Tupel Point mit den Feldern x, y und z.
Schreiben Sie eine Funktion calculate_distance, die zwei PointObjekte annimmt
und den Abstand zwischen ihnen im dreidimensionalen Raum berechnet.
Lösung:
Abstand im Raum mit namedtuple
Задача: Вычислить расстояние между двумя точками в 3D.
"""
# from collections import namedtuple
# from math import sqrt
"""DE: Wir importieren namedtuple für strukturierte Daten und sqrt für die Wurzel.
RU: Импортируем namedtuple и sqrt для вычисления корня.
DE: namedtuple erstellt leichtgewichtige, unveränderliche Objekte mit benannten Feldern – wie Klassen, 
aber kompakter.
RU: namedtuple создаёт легковесные неизменяемые объекты с именованными полями — как классы, но проще.
Warum benutzen wir namedtuple("Point", ["x", "y", "z"])? / Почему мы используем namedtuple("Point", ["x", "y", "z"])?
DE: Wir brauchen strukturierte Daten für Punkte im Raum (x, y, z).
Mit namedtuple können wir auf die Koordinaten leserlich mit punkt.x, punkt.y usw. zugreifen.
Es ist klarer und sicherer als die Verwendung einfacher Tupel (x, y, z).
RU: Для точек в пространстве нужны структурированные данные (x, y, z).
С namedtuple можно обращаться к координатам понятно: punkt.x, punkt.y и т. д.
Это более понятно и безопасно, чем обычные кортежи.
Zusammenfassung / Итог:
namedtuple ist ideal für kleine strukturierte Datentypen wie Koordinaten 
oder Vektoren – leserlich, effizient, pythonisch.
"""
# Point = namedtuple("Point", ["x", "y", "z"])
"""DE: Wir erstellen eine Struktur Point mit 3 Koordinaten: x, y, z.
namedtuple erlaubt uns, lesbaren Code mit Punktnotation zu schreiben.
RU: Создаём структуру Point с координатами x, y, z.
С namedtuple можно обращаться к полям как к атрибутам."""
# def calculate_distance(p1, p2):
#     return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)
"""DE: Die Funktion berechnet den euklidischen Abstand zwischen zwei Punkten.
Die Formel: √[(x₂−x₁)² + (y₂−y₁)² + (z₂−z₁)²]"""
""" RU: Функция считает евклидово расстояние между двумя точками.
Используем стандартную формулу расстояния в 3D."""
# point1 = Point(1, 2, 3)
# point2 = Point(4, 6, 8)
# print("Abstand zwischen den Punkten:", calculate_distance(point1, point2))
""" DE: Wir testen die Funktion mit zwei Punkten. Die Ausgabe ist das berechnete Ergebnis.
RU: Проверяем функцию на двух точках. Печатаем результат — расстояние между ними. """

"""
Übung 2.
1. Schreiben Sie eine Funktion safe_divide, 
die zwei Zahlen annimmt und das Ergebnis ihrer Division zurückgibt. 
Wenn die Division nicht möglich ist (Division durch Null), 
soll die Funktion die Meldung "Cannot divide by zero" zurückgeben, 
ohne die Ausführung des Programms zu unterbrechen.
"""
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
#
# print(safe_divide(1, 2))
# print(safe_divide(1, 0))
"""
DE: Wir definieren die Funktion safe_divide, die zwei Zahlen a und b annimmt.
Im try-Block versuchen wir, a durch b zu teilen.
Falls b = 0, wird eine ZeroDivisionError-Ausnahme ausgelöst.
Diese fangen wir im except-Block ab und geben eine freundliche Fehlermeldung zurück.
RU: Определяем функцию safe_divide, принимающую два числа a и b.
В блоке try пробуем выполнить деление a / b.
Если b = 0, вызывается исключение ZeroDivisionError.
В блоке except перехватываем ошибку и возвращаем сообщение об ошибке.
"""

"""
2. Schreiben Sie eine Funktion read_file, die versucht, eine Textdatei zu öffnen und zu lesen. 
Wenn die Datei nicht existiert, soll die Funktion den Fehler FileNotFoundError behandeln 
und die Meldung "File not found" ausgeben. 
Im Falle anderer Fehler soll die Meldung "An error occurred" ausgegeben werden.
"""
# def read_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         return "File not found"
#     except Exception:
#         return "An error occurred"
#
# f = read_file("test.txt")
# print(f)
"""
DE:
Die Funktion read_file nimmt den Dateinamen als Parameter.
Im try-Block öffnen wir die Datei im Lesemodus ('r').
Wenn die Datei existiert, lesen wir ihren Inhalt mit read() und geben ihn zurück.
Falls die Datei nicht existiert, wird FileNotFoundError ausgelöst – wir geben "File not found" zurück.
Andere unerwartete Fehler (z. B. Berechtigungen, Kodierung) fangen wir mit Exception ab.
RU:
Функция read_file принимает имя файла.
В блоке try открываем файл в режиме чтения ('r').
Если файл существует — читаем его содержимое и возвращаем.
Если файл не найден, возникает FileNotFoundError, возвращаем "File not found".
Все остальные ошибки (например, права доступа) перехватываются через Exception.
"""

"""
3. Schreiben Sie eine Funktion get_integer, die den Benutzer auffordert, eine Zahl einzugeben. 
Wenn der Benutzer keine ganze Zahl eingibt, soll die Funktion die Ausnahme ValueError behandeln 
und die Eingabe erneut abfragen, bis ein gültiger Wert eingegeben wird.
"""
# def get_integer():
#     while True:
#         try:
#             value = int(input("Bitte geben Sie eine ganze Zahl ein: "))
#             return value
#         except ValueError:
#             print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")
#
# get_integer()
"""
DE:
Die Funktion fordert den Benutzer im while True-Block zur Eingabe auf.
Wir versuchen, die Eingabe mit int() in eine ganze Zahl umzuwandeln.
Falls der Benutzer etwas Ungültiges eingibt (z. B. Buchstaben), wird ValueError ausgelöst.
Der Fehler wird abgefangen, und die Schleife wiederholt sich, bis eine gültige Zahl eingegeben wird.
RU:
Функция использует бесконечный цикл while True, чтобы запрашивать ввод.
С помощью int() пробуем преобразовать ввод в целое число.
Если введено что-то недопустимое (например, буквы) — вызывается ValueError.
Перехватываем исключение и продолжаем цикл, пока пользователь не введёт корректное число.
"""

"""
4. Schreiben Sie eine Funktion calculate_square_root, die eine Zahl annimmt 
und deren Quadratwurzel zurückgibt. Wenn die Zahl negativ ist, soll eine Ausnahme
ValueError ausgelöst werden. Behandeln Sie die Ausnahme 
und geben Sie die Meldung "Cannot calculate the square root of a negative number" zurück.
"""
# from math import sqrt
#
# def calculate_square_root(x):
#     try:
#         if x < 0:
#             raise ValueError("Negative Zahl")
#         return sqrt(x)
#     except ValueError:
#         return "Cannot calculate the square root of a negative number"
#
# calculated_square_root = calculate_square_root(-1)
# print(calculated_square_root)
"""
DE:
Wir importieren sqrt aus dem math-Modul für die Quadratwurzel.
Die Funktion calculate_square_root prüft, ob x negativ ist.
Wenn ja, lösen wir manuell ValueError aus.
Die Wurzelberechnung erfolgt nur bei gültigen (nicht-negativen) Zahlen.
Im except-Block behandeln wir negative Eingaben mit einer Fehlermeldung.
RU:
Импортируем sqrt из модуля math для вычисления корня.
Функция проверяет, не является ли x отрицательным.
Если число отрицательное — вручную вызываем ValueError.
Корень вычисляется только для неотрицательных чисел.
В блоке except возвращаем сообщение об ошибке.
📦 Verwendete Module:
from math import sqrt
DE: math.sqrt ist notwendig, um die Quadratwurzel korrekt zu berechnen.
RU: math.sqrt необходим для корректного вычисления квадратного корня.
"""
"""
Übung 3:
1. Erstellen Sie einen Generator RangeIterator, der einen Iterator implementiert, 
der ähnlich wie die eingebaute Funktion range() funktioniert. 
Der Generator soll einen Startwert, einen Endwert und einen Schrittwert annehmen, 
über die Werte iterieren und die Iteration beenden, wenn das Ende des Bereichs erreicht ist.
--------
DE: Wir definieren eine Klasse RangeIterator, die das Verhalten der range-Funktion nachbildet.
RU: Мы создаём класс RangeIterator, который имитирует поведение встроенной функции range.
__init__ speichert Start-, End- und Schrittwert.
RU: Метод __init__ сохраняет начальное значение, конец и шаг.
__iter__ gibt das Objekt selbst zurück (erforderlich für Iteration).
RU: Метод __iter__ возвращает сам объект — это нужно, чтобы он стал итерируемым.
__next__ erhöht den Wert um den Schritt, bis zum Ende.
RU: Метод __next__ увеличивает текущее значение, пока не достигнет конца.
"""
# class RangeIterator:
#     def __init__(self, start, end, step=1):
#         self.current = start
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         value = self.current
#         self.current += self.step
#         return value
#
# # Beispiel für RangeIterator
# print("RangeIterator von 0 bis 5:")
# for num in RangeIterator(0, 5):
#     print(num)
"""
2. Schreiben Sie eine Funktion file_line_iterator, die einen Dateinamen annimmt 
und einen Iterator zurückgibt, der der Reihe nach die Zeilen der Datei zurückgibt. 
Verwenden Sie diesen Iterator, um alle Zeilen der Datei einzeln zu lesen und auszugeben.
---------
DE: Diese Funktion nutzt yield, um eine Datei zeilenweise zu lesen.
RU: Эта функция использует yield для построчного чтения файла.
Datei wird mit open(filename) geöffnet.
RU: Файл открывается с помощью open(filename).
Jede Zeile wird einzeln mit yield zurückgegeben.
RU: Каждая строка поочерёдно возвращается через yield.
"""
# def file_line_iterator(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             yield line.strip()
#         oder: yield from (line.strip() for line in file)
#
# # Beispiel für file_line_iterator (Datei muss existieren)
# for line in file_line_iterator("beispiel.txt"):
#     print(line)
"""
3. Schreiben Sie einen Generator fibonacci, 
der die Fibonacci-Zahlenfolge bis zu einer bestimmten Anzahl von Elementen generiert. 
Testen Sie den Generator, indem Sie eine Liste der ersten 10 Fibonacci-Zahlen erstellen.
-------
DE: Wir nutzen yield, um n Fibonacci-Zahlen zu generieren.
RU: Используем yield, чтобы сгенерировать n чисел Фибоначчи.
Start mit a = 0, b = 1.
RU: Начальные значения a = 0, b = 1.
In jeder Schleife: yield a, dann neue Werte berechnen.
RU: На каждом шаге: выдаём a, затем пересчитываем a и b.
"""
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#         oder: return (a := b, b := a + b)[0] for _ in range(n)
#
# # Beispiel für fibonacci
# print("Erste 10 Fibonacci-Zahlen:")
# print(list(fibonacci(10)))
"""
4. Schreiben Sie einen Generator infinite_counter, 
der eine unendliche Sequenz von natürlichen Zahlen, beginnend mit 1, generiert. 
Verwenden Sie itertools.islice, um die ersten 20 Zahlen aus dieser Sequenz zu erhalten.
------
DE: Ein Generator liefert unendlich viele natürliche Zahlen.
RU: Генератор создаёт бесконечную последовательность натуральных чисел.
while True: ewige Schleife, beginnt bei 1.
RU: Цикл while True — бесконечный, начинается с 1.
itertools.islice(generator, 20) extrahiert nur 20 Zahlen.
RU: itertools.islice(generator, 20) извлекает первые 20 значений.
📦 Importiert:
from itertools import islice
DE: islice erlaubt es, Teile eines unendlichen Generators zu begrenzen.
RU: islice позволяет «обрезать» генератор и получить ограниченное количество элементов.
"""
# from itertools import islice
#
# def infinite_counter():
#     num = 1
#     while True:
#         yield num
#         num += 1
#         
#
# # Beispiel für infinite_counter mit islice
# print("Erste 20 Zahlen vom unendlichen Zähler:")
# print(list(islice(infinite_counter(), 20)))
# oder:
# from itertools import islice, count
#
# def infinite_counter():
#     return count(1)
#
# # Beispiel für infinite_counter mit islice
# print("Erste 20 Zahlen vom unendlichen Zähler:")
# print(list(islice(infinite_counter(), 20)))

"""
5. Schreiben Sie einen Generator random_numbers, 
der zwei Parameter start und end annimmt 
und eine unendliche Sequenz von Zufallszahlen in diesem Bereich generiert. 
Verwenden Sie den Generator, um die ersten 5 Zufallszahlen zu erhalten.
-------
DE: Wir generieren endlos viele Zufallszahlen im Bereich start bis end.
RU: Мы бесконечно генерируем случайные числа от start до end.
📦 Importiert:
import random
DE: random.randint(a, b) erzeugt zufällige Ganzzahlen zwischen a und b.
RU: random.randint(a, b) генерирует случайное целое число от a до b.
"""
# import random
#
# def random_numbers(start, end):
#     while True:
#         yield random.randint(start, end)
#
# # Beispiel für random_numbers
# print("5 Zufallszahlen zwischen 1 und 10:")
# rng = random_numbers(1, 10)
# for _ in range(5):
#     print(next(rng))
# oder:
# import random
#
# def random_numbers(start, end):
#     return (random.randint(start, end) for _ in iter(int, 1))  # unendlicher Generator
#
# # Beispiel für random_numbers
# print("5 Zufallszahlen zwischen 1 und 10:")
# print([next(random_numbers(1, 10)) for _ in range(5)])

"""
6. Erstellen Sie einen Generator even_numbers, 
der nur gerade Zahlen aus einem gegebenen Bereich generiert. 
Testen Sie den Generator, indem Sie die geraden Zahlen von 1 bis 20 generieren und ausgeben.
------
DE: Wir iterieren über eine Zahlenspanne und geben nur gerade Zahlen aus.
RU: Перебираем диапазон чисел и выдаём только чётные.
range(start, end + 1) erzeugt die Zahlenspanne.
if number % 2 == 0: Test auf gerade Zahl.
yield number gibt sie zurück.
"""
# def even_numbers(start, end):
#     for number in range(start, end + 1):
#         if number % 2 == 0:
#             yield number
#      oder: return (x for x in range(start, end + 1) if x % 2 == 0)
#
# # Beispiel für even_numbers
# print("Gerade Zahlen von 1 bis 20:")
# print(list(even_numbers(1, 20)))
"""
7. Schreiben Sie einen Generator square_numbers, 
der eine Liste von Zahlen annimmt und deren Quadrate generiert. 
Testen Sie den Generator anhand der Liste [5, 2, 7, 4, 1].
------
DE: Wir berechnen die Quadrate aller Zahlen in einer Liste.
RU: Вычисляем квадраты всех чисел из списка.
for number in numbers: Iteration durch Liste.
yield number ** 2: Quadrat wird zurückgegeben.
"""
# def square_numbers(numbers):
#     for number in numbers:
#         yield number ** 2
#      oder: return map(lambda x: x ** 2, numbers)
#
# # Beispiel für square_numbers
# print("Quadrate der Zahlen [5, 2, 7, 4, 1]:")
# print(list(square_numbers([5, 2, 7, 4, 1])))
"""
8. Schreiben Sie einen Generator repeat_string, 
der eine Zeichenkette und die Anzahl der Wiederholungen annimmt 
und die Zeichenkette die angegebene Anzahl von Malen generiert. 
Testen Sie den Generator mit der Zeichenkette "Hello", die 3 Mal wiederholt wird.
-----
DE: Wir wiederholen eine Zeichenkette times-mal mit yield.
RU: Повторяем строку заданное количество раз с помощью yield.
Schleife läuft times-mal.
yield string gibt die Zeichenkette zurück.
"""
# def repeat_string(string, times):
#     for _ in range(times):
#         yield string
#     oder: return (string for _ in range(times))
#
# # Beispiel für repeat_string
# print("Wiederhole 'Hello' 3 Mal:")
# print(list(repeat_string("Hello", 3)))


"""
def get_integer():
    try:
        return int(input("Bitte geben Sie eine ganze Zahl ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")
        return get_integer()

# Aufruf der Funktion
get_integer()

DE:
Die Funktion versucht, den eingegebenen Wert direkt in eine ganze Zahl umzuwandeln (int(input(...))).
Falls dies fehlschlägt (z. B. durch Buchstaben), wird der Fehler ValueError ausgelöst.
Dann wird eine Fehlermeldung ausgegeben und die Funktion ruft sich selbst erneut auf.
RU:
Функция пытается сразу преобразовать ввод в целое число с помощью int(input(...)).
Если ввод некорректен (например, буквы), возникает исключение ValueError.
В этом случае выводится сообщение об ошибке, и функция рекурсивно вызывает сама себя.
❗ Примечание:
Рекурсия работает, но в теории может вызвать переполнение стека 
при очень большом числе неудачных вводов.
В реальной практике для пользовательского ввода лучше оставить while!
"""
# def get_integer():
#     return next(
#         map(
#             lambda x: int(x),
#             iter(lambda: input("Bitte geben Sie eine ganze Zahl ein: "), None)
#         )
#     )
#
# try:
#     print(get_integer())
# except ValueError:
#     # Wiederhole die Funktion im Fehlerfall (rekursiv oder mit Schleife, je nach Wunsch)
#     print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")
#     get_integer()
"""
1. iter(lambda: input(...), None)
DE: Erstellt einen endlosen Iterator, der jedes Mal input() aufruft.
RU: Создаётся бесконечный итератор, вызывающий input() при каждом шаге.
2. map(lambda x: int(x), ...)
DE: Wendet int() auf jeden eingegebenen Wert an.
RU: К каждому введённому значению применяется int() с помощью map().
3. next(...)
DE: Holt den ersten gültigen Wert, der durch map() verarbeitet wird.
RU: Возвращается первое успешно преобразованное значение.
4. Fehlerbehandlung mit try/except
DE: Falls der erste Wert fehlerhaft ist (z. B. Buchstaben), wird ValueError ausgelöst.
RU: Если преобразование не удалось, возникает ValueError, и мы повторно вызываем функцию.
❗ Примечание:
Это немного читерский способ, 
потому что при ошибке мы один раз ловим исключение и заново запускаем get_integer() — 
но всё же он демонстрирует, как можно заменить while и использовать map для обработки ввода.

Вот финализированная версия функции get_integer(), где:
map() используется как цикл,
input() оборачивается в бесконечный итератор через iter(),
ошибки обрабатываются внутри с повтором — без while, но с функциональной логикой.
DE: Ein unendlicher Iterator, der jedes Mal input() aufruft.
RU: Бесконечный итератор, вызывающий input().
🧠 map(safe_parse, ...)
DE: Wendet die Funktion safe_parse auf jede Eingabe an.
RU: Применяет функцию safe_parse к каждому введённому значению.
🛡 safe_parse()
DE: Versucht int() umzuwandeln; gibt None zurück bei Fehler, sonst die Zahl.
RU: Преобразует ввод в int, в случае ошибки — возвращает None.
✅ if value is not None: return value
DE: Gibt das erste gültige Ergebnis zurück.
RU: Возвращает первое удачное значение.
🔄 Что получилось:
Без while
С map как основной итератор
Элегантная и безопасная реализация
"""

# def get_integer():
#     # Funktion zum sicheren Parsen der Eingabe in eine ganze Zahl
#     # Функция для безопасного преобразования ввода в целое число
#     def safe_parse(x):
#         try:
#             # Versucht den Wert in eine ganze Zahl umzuwandeln
#             # Пытаемся преобразовать значение в целое число
#             return int(x)
#         except ValueError:
#             # Bei Fehler wird eine Fehlermeldung ausgegeben
#             # В случае ошибки выводим сообщение об ошибке
#             print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")
#             # Gibt None zurück, wenn der Wert ungültig ist
#             # Возвращаем None, если значение некорректно
#             return None
#
#     # map wendet safe_parse auf jeden Eingabewert an
#     # map применяет функцию safe_parse ко всем введённым значениям
#     # iter ruft input unendlich oft auf, um die Benutzereingabe zu erhalten
#     # iter вызывает input бесконечно, чтобы получать ввод от пользователя
#     for value in map(safe_parse, iter(lambda: input("Bitte geben Sie eine ganze Zahl ein: "), None)):
#         # Wenn ein gültiger Wert gefunden wird (nicht None), wird dieser zurückgegeben
#         # Если найдено корректное значение (не None), возвращаем его
#         if value is not None:
#             return value

# Testaufruf
# Тестовый вызов
# print(f"Eingegebene Zahl: {get_integer()}")

"""
Пояснение шаг за шагом:
safe_parse(x):
DE: Versucht, 
den Eingabewert in eine ganze Zahl zu konvertieren, gibt None zurück, wenn ein Fehler auftritt.
RU: Пытается преобразовать ввод в целое число, если возникает ошибка — возвращает None.
map(safe_parse, iter(...)):
DE: map wendet safe_parse auf jedes Ergebnis von input() an, bis ein gültiger Wert gefunden wird.
RU: map применяет safe_parse к каждому результату input(), пока не будет найдено корректное значение.
iter(lambda: input(...), None):
DE: iter wird verwendet, um input() unendlich oft aufzurufen. 
Dies bedeutet, dass die Eingabe so lange abgefragt wird, bis ein gültiger Wert eingegeben wird.
RU: iter используется для бесконечного вызова input(). 
Это значит, что ввод будет запрашиваться до тех пор, пока не будет введено корректное значение.
for value in map(...)::
DE: Iteriert durch die Eingaben und gibt den ersten gültigen Wert zurück.
RU: Проходит по всем введённым данным и возвращает первое корректное значение.
if value is not None::
DE: Überprüft, ob der Wert gültig ist. Wenn ja, wird der Wert zurückgegeben.
RU: Проверяет, является ли значение корректным. Если да, возвращает его.
"""