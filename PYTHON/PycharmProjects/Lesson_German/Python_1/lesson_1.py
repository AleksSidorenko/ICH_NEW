# Aufgabe 1. Grundlagen der Arbeit mit Python
# Schreiben Sie ein Programm, das zwei Zahlen vom Benutzer entgegen nimmt
# und grundlegende mathematische Operationen durchführt:
# Addition, Subtraktion, Multiplikation, Division, Ganzzahldivision und Potenzieren.
# Geben Sie die Ergebnisse im Format "Operation: Ergebnis" aus.

# def basic_operations():
#     a = float(input("Geben Sie die erste Zahl ein: "))
#     b = float(input("Geben Sie die zweite Zahl ein: "))
#
#     print(f"Addition: {a + b}")
#     print(f"Subtraktion: {a - b}")
#     print(f"Multiplikation: {a * b}")
#     print(f"Division: {a / b if b != 0 else 'Nicht definiert'}")
#     print(f"Ganzzahldivision: {a // b if b != 0 else 'Nicht definiert'}")
#     print(f"Potenzieren: {a ** b}")
#
# basic_operations()

# Aufgabe 2. Operatoren und Ausdrücke
# Erstellen Sie ein Programm, das die Summe
# und das Produkt der Ziffern einer zweistelligen Zahl berechnet, die der Benutzer eingegeben hat.
# Verwenden Sie den Modulo-Operator und die Ganzzahldivision, um die Ziffern zu extrahieren.

# def sum_and_product():
#     number = int(input("Geben Sie eine zweistellige Zahl ein: "))
#
#     if 10 <= number <= 99:
#         tens = number // 10
#         ones = number % 10
#         print(f"Summe der Ziffern: {tens + ones}")
#         print(f"Produkt der Ziffern: {tens * ones}")
#     else:
#         print("Bitte geben Sie eine gültige zweistellige Zahl ein.")
#
# sum_and_product()

# Aufgabe 3. Boolesche Datentypen und Vergleiche
# Schreiben Sie ein Programm, das prüft,
# ob man aus drei vom Benutzer eingegebenen Zahlen a, b und c ein rechtwinkliges Dreieck bilden kann.
# Das Programm soll True oder False als Ergebnis ausgeben.

# def is_right_triangle():
#     a, b, c = sorted([int(input("a: ")), int(input("b: ")), int(input("c: "))])
#     print(a**2 + b**2 == c**2)
#
# is_right_triangle()

# Aufgabe 4. Bedingungsoperator if
# Schreiben Sie ein Programm,
# das eine Bewertung des Benutzers (eine ganze Zahl von 1 bis 5 entgegen nimmt
# und den entsprechenden Text ausgibt:
# "Sehr schlecht" für 1, "Schlecht" für 2, "Befriedigend" für 3, "Gut" für 4, "Sehr gut" für 5.

# def grade_description():
#     grade = int(input("Geben Sie eine Note von 1 bis 5 ein: "))
#     descriptions = {1: "Sehr schlecht", 2: "Schlecht", 3: "Befriedigend", 4: "Gut", 5: "Sehr gut"}
#     print(descriptions.get(grade, "Ungültige Note"))
#
# grade_description()


# Aufgabe 5. Schleife while
# Schreiben Sie ein Programm, das eine Zahl vom Benutzer abfragt
# und alle ihre Teiler unter Verwendung einer whileSchleife ausgibt.

# def divisors():
#     num = int(input("Geben Sie eine Zahl ein: "))
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             print(i, end=" ")
#         i += 1
#
# divisors()

# Aufgabe 6. Einführung in Zeichenketten
# Erstellen Sie ein Programm, das eine Zeichenkette vom Benutzer entgegen nimmt
# und eine Zeichenkette zurückgibt,
# bei der sich Groß- und Kleinbuchstaben abwechseln (zum Beispiel "Hallo" → "HaLlO").

# def alternate_case():
#     text = input("Geben Sie eine Zeichenkette ein: ")
#     result = "".join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text)])
#     print(result)
#
# alternate_case()

# Aufgabe 7. Zeichenketten: Methoden
# Schreiben Sie ein Programm, das eine Zeichenkette entgegennimmt,
# das längste Wort darin findet und ausgibt.
# Wenn mehrere Wörter die maximale Länge haben, geben Sie eines davon aus.

# def longest_word():
#     text = input("Geben Sie einen Satz ein: ")
#     words = text.split()
#     longest = max(words, key=len)
#     print("Längstes Wort:", longest)
#
# longest_word()

#  Aufgabe 8. Zeichenketten: Formatierung
# Erstellen Sie ein Programm, das den Namen, Nachnamen
# und das Alter des Benutzers abfragt und den Text im Format "Guten Tag, Nachname Vorname>!
# Sie sind Alter> Jahre alt." ausgibt.

# def greet_user():
#     vorname = input("Vorname: ")
#     nachname = input("Nachname: ")
#     alter = input("Alter: ")
#     print(f"Guten Tag, {nachname} {vorname}! Sie sind {alter} Jahre alt.")
#
# greet_user()


# Aufgabe 9. Schleife for und Grundlagen der Dateiarbeit
# Schreiben Sie ein Programm, das eine Textdatei erstellt
# und die Zahlen von 1 bis 100, jeweils eine Zahl pro Zeile,
# in die Datei schreibt. Lesen Sie anschließend die Datei und berechnen Sie die Summe aller Zahlen.

# def file_operations():
#     with open("zahlen.txt", "w") as f:
#         for i in range(1, 101):
#             f.write(f"{i}\n")
#
#     with open("zahlen.txt", "r") as f:
#         numbers = [int(line.strip()) for line in f]
#
#     print("Summe der Zahlen:", sum(numbers))
#
# file_operations()

# Aufgabe 10. Funktionen
# Erstellen Sie eine Funktion, die drei Zahlen entgegennimmt und die größte davon zurückgibt.
# Verwenden Sie diese Funktion in einem Programm,
# das drei Zahlen vom Benutzer abfragt und die größte Zahl ausgibt.

# def max_of_three(a, b, c):
#     return max(a, b, c)
#
# def main():
#     a = int(input("Erste Zahl: "))
#     b = int(input("Zweite Zahl: "))
#     c = int(input("Dritte Zahl: "))
#     print("Die größte Zahl ist:", max_of_three(a, b, c))
#
# main()
