"""
Aufgabe 4. Magische Methoden
Schreiben Sie eine Klasse Vektor,
die die Operationen Addition, Subtraktion
und Multiplikation mit einem Skalar unterstützt,
indem die entsprechenden magischen Methoden überladen werden.
Testen Sie die Klasse mit verschiedenen Beispielen.
---------
Напишите класс Vektor,
который поддерживает операции сложения, вычитания
и умножения на скаляр,
путём перегрузки соответствующих магических методов.
Протестируйте класс на различных примерах.
"""
### 🧠 **Lösungsmethode
"""
Um diese Aufgabe zu lösen, müssen wir eine eigene Klasse `Vektor` definieren,  
die sich wie ein mathematischer Vektor verhält.  
Wir verwenden dazu **magische Methoden**,  
um die Operatoren `+`, `-` und `*` für unsere Objekte zu überladen.

Jede dieser Operationen wird durch eine spezielle Methode dargestellt:
- `__add__` für Addition (`+`)
- `__sub__` für Subtraktion (`-`)
- `__mul__` für Skalarmultiplikation (`*`)

Diese Methoden erlauben es, dass Instanzen unserer Klasse mit den gewohnten Operatoren verwendet werden können,  
als wären sie normale Zahlen oder Listen.  
Dabei achten wir darauf, dass:
- Zwei Vektoren nur dann addiert oder subtrahiert werden können, wenn sie gleich lang sind.
- Die Skalarmultiplikation mit einem einzelnen Zahlenwert durchgeführt wird.

Zusätzlich definieren wir die Methode `__repr__`,  
damit eine lesbare Darstellung des Objekts beim Ausgeben im Terminal oder bei `print()` erscheint.

Am Ende testen wir die Klasse mit verschiedenen Beispielen,  
um sicherzustellen, dass die Methoden korrekt funktionieren.
"""
#### 🇷🇺 Перевод на русский:
"""
Чтобы решить эту задачу, мы должны определить собственный класс `Vektor`,  
который будет вести себя как математический вектор.  
Для этого мы используем **магические методы**,  
чтобы перегрузить операторы `+`, `-` и `*` для наших объектов.

Каждая из этих операций представляется специальным методом:
- `__add__` для сложения (`+`)
- `__sub__` для вычитания (`-`)
- `__mul__` для умножения на скаляр (`*`)

Эти методы позволяют использовать экземпляры нашего класса с обычными операторами,  
как если бы они были обычными числами или списками.  
При этом мы следим за тем, чтобы:
- Два вектора можно было складывать или вычитать только если они одинаковой длины.
- Умножение на скаляр выполнялось с отдельным числом.

Дополнительно мы определяем метод `__repr__`,  
чтобы при выводе на экран объект отображался в удобочитаемой форме.

В конце мы тестируем класс на различных примерах,  
чтобы убедиться, что методы работают правильно.
"""
# class Vektor:
#     # DE: Konstruktor der Klasse. Er speichert die Vektordaten in einer Liste.
#     # RU: Конструктор класса. Сохраняет данные вектора в виде списка.
#     def __init__(self, daten):
#         self.daten = daten
#
#     # DE: Magische Methode für die Addition zweier Vektoren.
#     # Sie addiert die entsprechenden Elemente beider Vektoren.
#     # RU: Магический метод для сложения двух векторов.
#     # Складывает соответствующие элементы обоих векторов.
#     def __add__(self, anderer):
#         return Vektor([a + b for a, b in zip(self.daten, anderer.daten)])
#
#     # DE: Magische Methode für die Subtraktion zweier Vektoren.
#     # Jedes Element des zweiten Vektors wird vom entsprechenden Element des ersten abgezogen.
#     # RU: Магический метод для вычитания двух векторов.
#     # Каждый элемент второго вектора вычитается из соответствующего элемента первого.
#     def __sub__(self, anderer):
#         return Vektor([a - b for a, b in zip(self.daten, anderer.daten)])
#
#     # DE: Magische Methode für die Multiplikation eines Vektors mit einem Skalar.
#     # Jedes Element des Vektors wird mit dem Skalar multipliziert.
#     # RU: Магический метод для умножения вектора на скаляр.
#     # Каждый элемент вектора умножается на скаляр.
#     def __mul__(self, skalar):
#         return Vektor([a * skalar for a in self.daten])
#
#     # DE: Diese Methode wird verwendet, um eine gut lesbare Darstellung des Objekts zurückzugeben.
#     # RU: Этот метод используется для возвращения читаемого строкового представления объекта.
#     def __repr__(self):
#         return f"Vektor({self.daten})"
#
#
# # DE: Beispielhafte Verwendung der Klasse:
# # RU: Примеры использования класса:
#
# v1 = Vektor([1, 2, 3])  # DE: Erster Vektor / RU: Первый вектор
# v2 = Vektor([4, 5, 6])  # DE: Zweiter Vektor / RU: Второй вектор
#
# # DE: Vektoraddition – Ergebnis ist ein neuer Vektor mit summierten Elementen.
# # RU: Сложение векторов — результатом будет новый вектор с суммами соответствующих элементов.
# print(v1 + v2)  # Ausgabe: Vektor([5, 7, 9])
#
# # DE: Vektorsubtraktion – Elementweises Abziehen.
# # RU: Вычитание векторов — поэлементное вычитание.
# print(v1 - v2)  # Ausgabe: Vektor([-3, -3, -3])
#
# # DE: Skalarmultiplikation – Jedes Element wird mit 3 multipliziert.
# # RU: Умножение на скаляр — каждый элемент умножается на 3.
# print(v1 * 3)   # Ausgabe: Vektor([3, 6, 9])
#
### ----------------------------------
"""
Aufgabe 5. Reguläre Ausdrücke
Schreiben Sie ein Programm, 
das eine Zeichenkette mit Datumsangaben im Format TT-MM-JJJJ annimmt 
und diese mit regulären Ausdrücken in das Format JJJJ-MM-TT umwandelt.

** Регулярные выражения:**
Напишите программу,  
которая принимает строку с датами в формате `ДД-ММ-ГГГГ`  
и с помощью **регулярных выражений** преобразует их в формат `ГГГГ-ММ-ДД`.
"""

## 🧠 Lösungsmethode
"""
Um dieses Problem zu lösen, verwenden wir die Bibliothek `re`,  
die reguläre Ausdrücke in Python unterstützt.  

Wir erstellen ein **reguläres Muster**,  
das nach Daten im Format `TT-MM-JJJJ` sucht:  
- Zwei Ziffern für den Tag (`\d{2}`),  
- gefolgt von einem Bindestrich (`-`),  
- zwei Ziffern für den Monat (`\d{2}`),  
- einem weiteren Bindestrich,  
- und vier Ziffern für das Jahr (`\d{4}`).

Dann verwenden wir die Funktion `re.sub()`,  
um alle gefundenen Datumsangaben umzuwandeln.  
Dabei nutzen wir **Gruppen** in runden Klammern `()` im regulären Ausdruck,  
damit wir in der Ersetzung (`replace`) die Reihenfolge ändern können:  
von `(\d{2})-(\d{2})-(\d{4})` zu `\3-\2-\1`.
"""
#### 🇷🇺 Перевод:
"""
Чтобы решить эту задачу, мы используем модуль `re`,  
который поддерживает регулярные выражения в Python.  

Мы создаём **регулярное выражение**,  
которое ищет даты в формате `ДД-ММ-ГГГГ`:  
- две цифры для дня (`\d{2}`),  
- затем дефис (`-`),  
- две цифры для месяца (`\d{2}`),  
- ещё один дефис,  
- и четыре цифры для года (`\d{4}`).

Затем мы используем функцию `re.sub()`,  
чтобы преобразовать все найденные даты.  
Мы применяем **группы** (в круглых скобках `()`),  
чтобы затем в строке замены изменить порядок:  
из `(\d{2})-(\d{2})-(\d{4})` получаем `\3-\2-\1`.
"""
# import re  # DE: Importieren der Bibliothek für reguläre Ausdrücke
#            # RU: Импортируем модуль для работы с регулярными выражениями
#
# # DE: Ursprüngliche Zeichenkette mit Datumsangaben im Format TT-MM-JJJJ
# # RU: Исходная строка с датами в формате ДД-ММ-ГГГГ
# text = "Heute ist der 13-04-2025 und morgen ist der 14-04-2025."
#
# # DE: Regulärer Ausdruck zur Erkennung des Datumsformats TT-MM-JJJJ:
# # Wir verwenden drei Gruppen:
# #   1. (\d{2}) – genau zwei Ziffern für den Tag
# #   2. (\d{2}) – genau zwei Ziffern für den Monat
# #   3. (\d{4}) – genau vier Ziffern für das Jahr
# # RU: Регулярное выражение для поиска формата ДД-ММ-ГГГГ:
# # Мы используем три группы:
# #   1. (\d{2}) – ровно две цифры для дня
# #   2. (\d{2}) – ровно две цифры для месяца
# #   3. (\d{4}) – ровно четыре цифры для года
# muster = r"(\d{2})-(\d{2})-(\d{4})"
#
# # DE: Umwandlung der gefundenen Daten mit re.sub()
# # \3 – Jahr, \2 – Monat, \1 – Tag
# # Wir vertauschen die Reihenfolge, um das Format JJJJ-MM-TT zu erhalten
# # RU: Преобразование найденных дат с помощью re.sub()
# # \3 – год, \2 – месяц, \1 – день
# # Мы меняем порядок, чтобы получить формат ГГГГ-ММ-ДД
# text_umgewandelt = re.sub(muster, r"\3-\2-\1", text)
#
# # DE: Ausgabe der umgewandelten Zeichenkette
# # RU: Вывод преобразованной строки
# print(text_umgewandelt)
#
# ### 🧪 Результат выполнения программы:
# """
# Heute ist der 2025-04-13 und morgen ist der 2025-04-14.
# """
#### -------------
"""
Aufgabe 6. Grundlagen der Netzwerkprogrammierung
Erstellen Sie ein Programm, 
das eine GET-Anfrage an eine Website sendet und den Statuscode der Antwort ausgibt. 
Verwenden Sie die Bibliothek requests.

**Основы сетевого программирования:**

Создайте программу,  
которая отправляет **GET-запрос** на веб-сайт  
и выводит **код статуса** ответа.  
Используйте библиотеку **`requests`**.
"""

"""
## 🧠 Lösungsmethode
#### 🇩🇪 Deutsch:

Um diese Aufgabe zu lösen, verwenden wir die externe Bibliothek `requests`,  
die die Arbeit mit HTTP-Anfragen in Python vereinfacht.

Zuerst importieren wir die Bibliothek.  
Dann definieren wir eine Ziel-URL als Zeichenkette (z.B. `"https://example.com"`).  
Mit der Methode `requests.get(URL)` senden wir eine HTTP-GET-Anfrage an diese Adresse.  
Die Methode gibt ein **Response-Objekt** zurück.

Aus diesem Objekt können wir mit `.status_code`  
den **Statuscode der HTTP-Antwort** auslesen.  
Zum Beispiel:
- `200` bedeutet „OK“ (alles in Ordnung),
- `404` bedeutet „Nicht gefunden“,
- `500` ist ein Serverfehler usw.

Zum Schluss geben wir diesen Statuscode mit `print()` aus.
#### 🇷🇺 Перевод:

Чтобы решить эту задачу, мы используем внешнюю библиотеку `requests`,  
которая упрощает работу с HTTP-запросами в Python.

Сначала импортируем библиотеку.  
Затем задаём целевой URL как строку (например, `"https://example.com"`).  
С помощью метода `requests.get(URL)` мы отправим HTTP-запрос типа GET по этому адресу.  
Метод возвращает **объект ответа** (`Response`).

Из этого объекта мы можем получить **статус-код HTTP-ответа** через `.status_code`.  
Например:
- `200` означает «ОК» (успешно),
- `404` означает «Не найдено»,
- `500` — ошибка сервера и т. д.

В конце мы выводим этот статус-код с помощью `print()`.
"""

# # DE: Wir importieren die Bibliothek „requests“ für HTTP-Anfragen
# # RU: Импортируем библиотеку „requests“ для выполнения HTTP-запросов
# import requests
#
# # DE: Wir definieren eine Ziel-URL als einfache Zeichenkette
# # RU: Определяем целевой URL как строку
# url = "https://example.com"
#
# # DE: Wir senden eine GET-Anfrage mit der Funktion requests.get()
# # Klammer auf: wir beginnen den Funktionsaufruf
# # Wir übergeben die URL als Argument in Klammern
# # Klammer zu: der Aufruf ist abgeschlossen
# # RU: Отправляем GET-запрос с помощью функции requests.get()
# # Открываем скобку — начинаем вызов функции
# # Передаём URL в качестве аргумента в скобках
# # Закрываем скобку — завершение вызова
# antwort = requests.get(url)
#
# # DE: Wir greifen auf das Attribut „status_code“ des Antwortobjekts zu
# # RU: Получаем доступ к атрибуту „status_code“ объекта ответа
# status = antwort.status_code
#
# # DE: Wir geben den Statuscode mit print() aus
# # Klammer auf: wir beginnen die Ausgabe
# # Klammer zu: Ausgabe abschließen
# # RU: Выводим код статуса с помощью print()
# # Открываем скобку — начинаем вывод
# # Закрываем скобку — завершаем вывод
# print("Statuscode der Antwort:", status)
#
#
# ### 🧪 Пример вывода:
# # Statuscode der Antwort: 200

"""
Aufgabe 7. Mehrmodulige Programme, Web-Scraping
Schreiben Sie ein Programm, 
das das Modul BeautifulSoup importiert und verwendet, 
um eine bestimmte Webseite zu analysieren. 
Das Programm soll den Titel der Seite ausgeben.

**Многомодульные программы, Web-Scraping:**

Напишите программу,  
которая импортирует модуль **BeautifulSoup**  
и использует его для анализа определённого веб-сайта.  
Программа должна вывести **заголовок страницы**.
"""
"""
## Lösungsmethode 
#### 🇩🇪 Deutsch:

Für diese Aufgabe verwenden wir zwei externe Bibliotheken:
- `requests`, um den HTML-Inhalt der Webseite abzurufen,
- `bs4` (BeautifulSoup), um den HTML-Code zu analysieren.

Zuerst importieren wir die Module: `requests` für den Abruf und `BeautifulSoup` aus `bs4` für das Parsen.

Wir definieren eine Ziel-URL, z.B. `"https://example.com"`.  
Mit `requests.get()` senden wir eine **HTTP-GET-Anfrage**,  
und erhalten als Antwort den HTML-Code der Seite.

Diesen HTML-Code übergeben wir an den **Konstruktor** von `BeautifulSoup`,  
zusammen mit dem Parser `"html.parser"`.

Mit `soup.title` oder `soup.title.string` greifen wir auf den `<title>`-Tag zu  
und geben den Text des Seitentitels mit `print()` aus.
#### 🇷🇺 Перевод:

Для выполнения этой задачи мы используем две внешние библиотеки:
- `requests` — для получения HTML-контента страницы,
- `bs4` (BeautifulSoup) — для разбора HTML-кода.

Сначала мы импортируем модули: `requests` — для загрузки страницы,  
а `BeautifulSoup` из `bs4` — для парсинга (анализа) HTML.

Затем задаём URL целевой страницы, например, `"https://example.com"`.  
С помощью `requests.get()` мы отправляем **HTTP-запрос**  
и получаем HTML-код страницы в ответе.

Этот HTML-код мы передаём **в конструктор** `BeautifulSoup`  
вместе с указанием парсера `"html.parser"`.

С помощью `soup.title` или `soup.title.string` мы получаем тег `<title>`  
и выводим его текст с помощью `print()`.
"""
## ✅

# # DE: Wir importieren die Bibliothek „requests“, um den HTML-Inhalt herunterzuladen
# # RU: Импортируем библиотеку „requests“ для загрузки HTML-содержимого
# import requests
#
# # DE: Wir importieren die Klasse BeautifulSoup aus dem Modul bs4
# # RU: Импортируем класс BeautifulSoup из модуля bs4
# from bs4 import BeautifulSoup
#
# # DE: Wir definieren die Ziel-URL als Zeichenkette
# # RU: Определяем целевой URL как строку
# url = "https://example.com"
#
# # DE: Wir senden eine GET-Anfrage mit requests.get()
# # Klammer auf — Beginn des Funktionsaufrufs
# # Übergabe der URL als Argument
# # Klammer zu — Funktionsaufruf abgeschlossen
# # RU: Отправляем GET-запрос с помощью requests.get()
# # Открываем скобку — начало вызова функции
# # Передаём URL как аргумент
# # Закрываем скобку — завершение вызова
# antwort = requests.get(url)
#
# # DE: Wir holen den HTML-Inhalt mit .text
# # RU: Получаем HTML-содержимое страницы через .text
# html_inhalt = antwort.text
#
# # DE: Wir analysieren den HTML-Inhalt mit BeautifulSoup
# # Klammer auf: Beginn des Objektaufbaus
# # Zwei Argumente:
# #   1. HTML-Inhalt
# #   2. Parser-Typ "html.parser"
# # Klammer zu: Objekt wird erstellt
# # RU: Анализируем HTML с помощью BeautifulSoup
# # Открываем скобку — начинаем создание объекта
# # Два аргумента:
# #   1. HTML-содержимое
# #   2. Тип парсера "html.parser"
# # Закрываем скобку — объект создан
# soup = BeautifulSoup(html_inhalt, "html.parser")
#
# # DE: Wir greifen auf den <title>-Tag zu
# # RU: Получаем доступ к тегу <title>
# seitentitel = soup.title.string
#
# # DE: Wir geben den Seitentitel mit print() aus
# # RU: Выводим заголовок страницы через print()
# print("Seitentitel:", seitentitel)
#
# ### 🧪 Пример вывода:
# # Seitentitel: Example Domain
