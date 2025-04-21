# 1. Напишите функцию extract_emails(text),
# которая извлекает все адреса электронной почты из заданного текста и возвращает их в виде списка.
# Пример использования:
# text = "Contact us at info@example.com or support@example.com for assistance."
# emails = extract_emails(text)
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']

import re

def extract_emails(text):
    pattern = r"[\w.-]+@[\w.-]+\.\w+"
    # pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
    return re.findall(pattern, text)


text = "Contact us at info@example.com or support@example.com for assistance al_.ex_gr-23@gmail.com."
emails = extract_emails(text)
print(emails)

# GPT:
"""
Ваш код предназначен для извлечения адресов электронной почты 
из заданного текста с использованием регулярных выражений в Python. 
Давайте подробно разберем его работу:
**1. Импорт модуля `re`:**
import re

Модуль `re` предоставляет функции для работы с регулярными выражениями в Python.

**2. Определение функции `extract_emails`:**

def extract_emails(text):
    pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
    return re.findall(pattern, text)

- **Параметр `text`**: строка, из которой необходимо извлечь адреса электронной почты.
- **Шаблон `pattern`**: регулярное выражение `r"[\w\.-]+@[\w\.-]+\.\w+"` предназначено для поиска адресов электронной почты. Разберем его:
  - `[\w\.-]+`: совпадает с одним или более символами, которые могут быть буквенно-цифровыми (`\w`), точкой (`.`) или дефисом (`-`). Это соответствует локальной части адреса (до символа `@`).
  - `@`: буквальный символ `@`.
  - `[\w\.-]+`: аналогично первому набору, соответствует доменному имени (между `@` и последней точкой).
  - `\.`: буквальный символ точки, разделяющий домен и доменную зону.
  - `\w+`: один или более буквенно-цифровых символов, соответствующих доменной зоне (например, `com`, `org`).

**3. Пример использования функции:**
text = "Contact us at info@example.com or support@example.com for assistance."
emails = extract_emails(text)
print(emails)

В этом примере функция `extract_emails` применяется к строке `text`, 
содержащей два адреса электронной почты. Ожидаемый вывод:
['info@example.com', 'support@example.com']

**Альтернативные варианты решения:**
1. **Использование более точного регулярного выражения:**
Ваше текущее регулярное выражение может не учитывать некоторые допустимые 
адреса электронной почты или, наоборот, включать недопустимые. 
Для более точного соответствия можно использовать следующее выражение:

pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

Это выражение учитывает дополнительные символы, допустимые в адресах электронной почты, 
такие как подчеркивания, плюсы и т.д.

2. **Использование модуля `email.utils`:**
Python предоставляет модуль `email.utils`, 
который может быть использован для разбора адресов электронной почты:

from email.utils import getaddresses

text = "Contact us at info@example.com or support@example.com for assistance."
addresses = getaddresses([text])
emails = [address[1] for address in addresses]
print(emails)

Этот метод особенно полезен, 
если адреса электронной почты могут быть окружены дополнительной информацией, такой как имена.

3. **Использование сторонних библиотек:**
Существуют сторонние библиотеки, 
такие как `pyap` или `email_validator`, 
которые предоставляют более сложные методы для извлечения и валидации адресов электронной почты. 
Эти библиотеки могут быть полезны, если вам требуется более сложная обработка.
"""

# 2. Напишите функцию highlight_keywords(text, keywords),
# которая выделяет все вхождения заданных ключевых слов в тексте,
# окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
# Пример использования:
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
# highlighted_text = highlight_keywords(text, keywords)
# print(highlighted_text)
# # Вывод: "This is a sample text. We need to highlight *Python* and *programming*."
# ICH
# import re
#
# def highlight_keywords(text, keywords):
#     for keyword in keywords:
#        text = re.sub(f"({keyword})", r'*\1*', text, flags=re.IGNORECASE)
#     return text
#
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
# print(highlight_keywords(text,keywords))

# GPT
import re

def highlight_keywords(text, keywords):
    for keyword in keywords:
        text = re.sub(rf"\b({keyword})\b", r"*\1*", text, flags=re.I)
    return text

text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]

print(highlight_keywords(text, keywords))
# # rf"" — это f-строка с raw-режимом (не нужно экранировать \ вручную).

# GPT
# import re
#
# def highlight_keywords(text, keywords):
#     for keyword in keywords:
#         pattern = rf"\b({keyword})\b"
#         # Используем оператор морж для промежуточного результата замены
#         while match := re.search(pattern, text, flags=re.I):
#             word = match.group(0)
#             # Заменяем только первое найденное вхождение, сохраняем регистр
#             text = text[:match.start()] + f"*{word}*" + text[match.end():]
#     return text
#
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
#
# print(highlight_keywords(text, keywords))

# Список всех найденных ключевых слов (регистронезависимо)
# import re
#
# def find_keywords(text, keywords):
#     found = [match.group(0)
#              for kw in keywords
#              if (match := re.search(rf"\b({kw})\b", text, flags=re.IGNORECASE))]
#     return found
#
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
#
# print(find_keywords(text, keywords))