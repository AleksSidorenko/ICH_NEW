## Регулярные выражения

## Функция findall

Функция **`re.findall()`** ищет **все совпадения шаблона** в строке и возвращает их в виде списка.  

#### Синтаксис:  
```python
re.findall(pattern, string)
```
- **`pattern`** – регулярное выражение (шаблон поиска).  
- **`string`** – строка, в которой выполняется поиск.  

#### Пример: Поиск всех чисел в строке  
```python
import re

text = "Python 3.9, Java 17, C++ 14"

numbers = re.findall(r"\d+", text)  # Поиск всех чисел
print(numbers)
```


## Основные символы в регулярных выражениях

| Символ | Описание                 |
|--------|--------------------------|
| `\d`   | Любая цифра (`0-9`)      |
| `\D`   | Любой символ, кроме `\d` |
| `\w`   | Буквы, цифры и `_`       |
| `\W`   | Любой символ, кроме `\w` |
| `\s`   | Пробел, `\t`, `\n`       |
| `\S`   | Любой символ, кроме `\s` |
| `.`    | Любой символ, кроме `\n` |


#### Примеры:

```python
import re

text = "\tPython 3.12, Java 17, C++ 14!\n"

print("Цифры:", re.findall(r"\d", text))
print("Двузначные цифры:", re.findall(r"\d\d", text))

print("НЕ цифры:", re.findall(r"\D", text))

print("Буквы, цифры, _:", re.findall(r"\w", text))

print("НЕ буквы, цифры, _:", re.findall(r"\W", text))

print("Пробелы:", re.findall(r"\s", text))

print("НЕ пробелы:", re.findall(r"\S", text))

print("Все символы (кроме \\n):", re.findall(r".", text))
```


## Символ 'r' перед строкой шаблона

Python обрабатывает **`\` (обратный слэш) как управляющий символ**, из-за чего могут возникнуть ошибки.  
Чтобы избежать этого, перед строкой **рекомендуется ставить `r` ("сырая" строка, raw string)**.  


#### Пример: Если не использовать `r`:  
```python
import re

pattern = "\d"  # ОШИБКА: \d будет воспринято как управляющий символ
print(re.findall(pattern, "Price: 123"))
```


## Классы символов

| Запись     | Описание                                 |
|------------|------------------------------------------|
| `[afc]`    | Один из символов `a`, `f` или `c`        |
| `[0-9]`    | Любая цифра от `0` до `9` (аналог `\d`)  |
| `[a-z]`    | Любая строчная буква от `a` до `z`       |
| `[A-Z]`    | Любая заглавная буква от `A` до `Z`      |
| `[a-zA-Z]` | Любая буква (заглавная или строчная)     |
| `[^abc]`   | Любой символ, **кроме** `a`, `b` или `c` |
| `[^0-9]`   | Любой символ, **кроме** цифры            |


#### Примеры:

```python
import re

text = "Report, report, report2, report10"


print("Буквы r или R в слове:", re.findall(r"[rR]eport", text))

print("Все цифры:", re.findall(r"[0-9]", text))

print("Заглавные буквы:", re.findall(r"[A-Z]", text))

print("Строчные буквы:", re.findall(r"[a-z]", text))

print("Все буквы:", re.findall(r"[a-zA-Z]", text))

print("Все, кроме цифр:", re.findall(r"[^0-9]", text))
```


## Квантификаторы

| Квантификатор | Описание                            |
|---------------|-------------------------------------|
| `+`           | Один или более раз (`1, 2, 3...`)   |
| `*`           | Ноль или более раз (`0, 1, 2...`)   |
| `?`           | Ноль или один раз (`0, 1`)          |
| `{n}`         | Ровно `n` раз                       |
| `{n,}`        | `n` и более раз                     |
| `{n,m}`       | От `n` до `m` раз                   |

#### Примеры:

```python
import re

text = """
Orders: ID123, ID4567, ID89
Numbers: 123-45-67, 321-45-67
Prices: 100$, 199.50$, 99.99€, 0.49€, .99€
File names: report.txt, report2.txt, report10.txt
"""

print("Одна или более цифр:", re.findall(r"\d+", text))

print("Телефонные номера (формата xxx-xx-xx):", re.findall(r"\d{3}-\d{2}-\d{2}", text))

print("Цены (числа с десятичной точкой):", re.findall(r"\d+\.\d+", text))

print("ID-коды:", re.findall(r"ID\d{2,}", text))

print("Имена файлов 0+ цифр:", re.findall(r"report\d*.txt", text))

print("Имена файлов 0/1 цифр:", re.findall(r"report\d?.txt", text))

print("Имена файлов 1/2 цифр:", re.findall(r"report\d{1,2}.txt", text))
```


## Жадные и ленивые квантификаторы

| Квантификатор | Тип      | Описание                                                   |
|---------------|----------|------------------------------------------------------------|
| `*`           | Жадный   | Захватывает **максимально возможное** количество символов  |
| `*?`          | Ленивый  | Захватывает **минимально возможное** количество символов   |
| `+`           | Жадный   | Захватывает **минимум 1 символ**, но **как можно больше**  |
| `+?`          | Ленивый  | Захватывает **минимум 1 символ**, но **как можно меньше**  |
| `{n,m}`       | Жадный   | Захватывает **от `n` до `m`**, но **как можно больше**     |
| `{n,m}?`      | Ленивый  | Захватывает **от `n` до `m`**, но **как можно меньше**     |


#### Примеры:
```python
import re
text = "<div>Hello</div><div>World</div>"

greedy = re.findall(r"<.*>", text)  # Жадный
lazy = re.findall(r"<.*?>", text)   # Ленивый

print(greedy)
print(lazy)
```


## Экранирование специальных символов

#### Примеры:

```python
import re

text = "report.txt, report2.txt, report10.txt, some_txt_report, some_report_txt"

print("Имена файлов с txt:", re.findall(r"\w+.txt", text))

# Имена файлов с расширением .txt
print("Имена файлов с расширением .txt:", re.findall(r"\w+\.txt", text))

# Имена файлов в папке
print("Имена файлов в папке:", re.findall(r"\w+\\\w+\.\w+", r"reports\report.txt, report2.txt"))
```


## Якоря


| Якорь   | Описание         |
|---------|------------------|
| `^`     | Начало строки    |
| `$`     | Конец строки     |
| `\b`    | Граница слова    |
| `\B`    | Не граница слова |


#### Примеры:

```python
import re

text = "Hello world! Welcome to world"

print("Слово в начале строки:", re.findall(r"^\w+", text))
print("Слово в конце строки:", re.findall(r"\w+$", text))


text2 = "category wildcat education _cat_ catalog"

print("Слова с 'cat' внутри:", re.findall(r"\w+cat\w+", text2))
print("Слова с 'cat' в начале слов:", re.findall(r"\bcat\w*", text2))
print("Слова с 'cat' в конце слов:", re.findall(r"\w*cat\b", text2))

text3 = "X123X 234 4567X X999"
print("Числа внутри строк:", re.findall(r"\B\d+\B", text3))
```


## Альтернативы

#### Примеры:
```python
import re

text = "Meeting on 2024-05-10 or 10/05/2024 at 14:30"

# Найдём даты в формате YYYY-MM-DD или DD/MM/YYYY
print("Даты:", re.findall(r"(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})", text))
```


## Группы

#### Пример: Извлечение данных с помощью групп

Функция `re.search()` и `re.match()` позволяют **доступ к частям совпадений** через `group()`.  

```python
import re

text = "Order ID: 12345, Invoice No: 67890"

# Найдём ID заказа и счёта
match = re.search(r"Order ID: (\d+), Invoice No: (\d+)", text)

if match:
    print("ID заказа:", match.group(1))
    print("Номер счёта:", match.group(2))
```

#### Пример: Использование негруппирующих скобок

Если группа нужна для логики, но не для извлечения данных, можно использовать `(?:...)`.  

```python
import re

text = "USD 100, EUR 200, GBP 300"

# Найдём суммы, не выделяя валюту
matches = re.findall(r"(?:USD|EUR|GBP) (\d+)", text)
print("Суммы:", matches)

# Найдём суммы и валюту
matches = re.findall(r"(USD|EUR|GBP) (\d+)", text)
print("Суммы:", matches)
```


## Функции модуля re

### Функция re.match

Функция **`re.match()`** проверяет, **начинается ли строка с заданного шаблона**.  
Если совпадение найдено, функция возвращает **объект `Match`**, который содержит информацию о совпадении, иначе `None`.  


### Объект Match

Объект `Match` содержит **информацию о найденном фрагменте**, включая:  
- **`.group()`** – само совпадение.  
- **`.start()`** – индекс начала совпадения.  
- **`.end()`** – индекс конца совпадения.  
- **`.span()`** – кортеж `(start, end)`, показывающий границы совпадения.  


#### Пример:
```python
import re

text = "ID12345 is confirmed. ID23456 is confirmed"

# Проверяем, начинается ли строка с "ID" + цифры
match = re.match(r"ID\d+", text)

if match:
    print("Объект Match:", match)
    print("Само совпадение:", match.group())
    print("Диапазон совпадения:", match.span())
else:
    print("Нет совпадения.")
```


### Функция re.search

Функция **`re.search()`** ищет **первое совпадение** регулярного выражения **в любой части строки** и возвращает **объект `Match`**.  

#### Пример:
```python
import re

text = "Order ID: 12345, Invoice No: 67890, Ref: ABC9876"

# Найдём первое число в тексте
match = re.search(r"\d+", text)

if match:
    print("Объект Match:", match)
    print("Само совпадение:", match.group())
    print("Индекс начала:", match.start())
    print("Индекс конца:", match.end())
    print("Диапазон совпадения:", match.span())
else:
    print("Нет совпадения.")
```


### Флаг re.IGNORECASE

Флаг **`re.IGNORECASE`** (или сокращённо `re.I`) делает поиск **регистронезависимым** — шаблон будет находить совпадения **в любом регистре**, 
даже если написан в нижнем или верхнем.

#### Пример:
```python
import re

text = "Python is popular."

# Найдём слово "python" без учёта регистра
match = re.search(r"python", text, re.IGNORECASE)

if match:
    print("Найдено:", match.group())
```


### Функция re.finditer

Функция **`re.finditer()`** ищет **все совпадения** регулярного выражения в строке и возвращает **итератор объектов `Match`**.  


#### Пример:
```python
import re

text = "Order ID: 12345, Invoice No: 67890, Ref: ABC9876"

# Найдём все числа в тексте
matches = re.finditer(r"\d+", text)

for match in matches:
    print("Объект Match:", match)
    print("Само совпадение:", match.group())
    print("Диапазон совпадения:", match.span())
    print()
```


### Функция re.split

Функция **`re.split()`** разделяет строку на части, используя **регулярное выражение как разделитель**.  
Она работает аналогично `str.split()`, но позволяет **разбивать текст по сложным шаблонам**, а не только по одному символу.  

#### Пример:
```python
import re

text = """Python is popular. It is used in web development, data science, 
and automation. Many developers choose Python for its simplicity."""

# Разделяем строку по запятым, пробелам и точкам
words = re.split(r"[,\s.]+", text)

print("Список слов:", words)
```


### Функция re.sub

Функция **`re.sub()`** заменяет все найденные совпадения **на указанную строку или результат функции**.  
Это полезно для **форматирования текста, удаления лишних символов и исправления данных**.  

#### Синтаксис:
```python
re.sub(pattern, repl, string)
```
- **`pattern`** – шаблон для поиска.  
- **`repl`** – строка, на которую будет заменено совпадение.  
- **`string`** – исходный текст.  

#### Пример:
```python
import re

text = "apple,   banana ,  orange ,grape"

# Удаляем лишние пробелы перед и после запятых
clean_text = re.sub(r"\s*,\s*", ", ", text)

print("Отформатированный текст:", clean_text)
```


### Функция re.compile 

Функция **`re.compile()`** позволяет **предварительно скомпилировать регулярное выражение**, чтобы затем использовать его **многократно** без повторного пересоздания.  

#### Синтаксис:
```python
pattern = re.compile(regular_expression)
```

#### Пример:
```python
import re

texts = [
    "Order ID: 12345, Invoice No: 67890, Ref: ABC9876",
    "Shipment ID: 54321, Tracking No: 98765, Customer Ref: XYZ123",
    "Invoice 22222 processed successfully."
]

# Компилируем регулярное выражение для поиска числовых идентификаторов
number_pattern = re.compile(r"\d+")

# Применяем шаблон к разным текстам
for text in texts:
    match = number_pattern.findall(text)
    if match:
        print(f"Совпадение в тексте: {match}")
```


## Полезные сайты

- [**regex101.com**](https://regex101.com/)  
- [**regexr.com**](https://regexr.com/)  

## Комбинации
Ctrl + F             в этом файле
Ctrl + Shift + F     по всему проекту

