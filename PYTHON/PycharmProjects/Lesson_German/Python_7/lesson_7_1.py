"""
Aufgabe 1. Schreiben Sie ein Python-Programm, das zufällige Fakten über Katzen ausgibt.
Im Internet gibt es viele Dienste, die zufällige Fakten über REST-APIs bereitstellen.
In dieser Aufgabe verwenden wir den Dienst CatFact Ninja.
Dieser Dienst ist kostenlos und erfordert keine Registrierung.
1. Bevor Sie das Programm schreiben, gehen Sie auf die Website von CatFact Ninja API.
   Diese Website bietet die Möglichkeit, Anfragen zu senden,
   um zufällige Katzenfakten zu erhalten
   (Wenn Sie auf der Website ein Formular zu Ihrer Person und der Bewerbung ausfüllen müssen,
   können Sie dort alles schreiben.).
2. Suchen Sie in der Dokumentation nach einer Anfrage für einen zufälligen Fakt.
   Ein Beispiel einer Anfrage:
   https://catfact.ninja/fact
3. Geben Sie diese URL in Ihren Browser ein und überprüfen Sie das Ergebnis.
   Beispiel für eine Antwort:
   {
     "fact": "Katzen benutzen ihre Schnurrhaare, um zu erkennen, ob sie durch
   einen engen Raum passen.",
     "length": 63
}
4. Untersuchen Sie die erhaltene JSONAntwort und finden Sie den Parameter fact,
   der den Katzenfakt enthält.
5. Nun gehen wir zur Praxis über. Verwenden Sie die Bibliothek requests
   und schreiben Sie ein Programm, das eine Anfrage an die API sendet,
   einen zufälligen Katzenfakt erhält und diesen an den Benutzer ausgibt.

 Hinweis: Verwenden Sie die folgende URL:
   https://catfact.ninja/fact
Beispiel eines Python-Programms:
   import requests
   def get_cat_fact():
       url = 'https://catfact.ninja/fact'
       response = requests.get(url)
       if response.status_code == 200:
           data = response.json()
           print(f"Zufälliger Fakt über Katzen: {data['fact']}")
       else:
           print("Daten konnten nicht vom Server abgerufen werden.")
   get_cat_fact()
"""
# Importiere die Bibliothek 'requests', um HTTP-Anfragen zu senden.
# Импортируем библиотеку 'requests', чтобы отправлять HTTP-запросы.
import requests

# Definiere eine Funktion namens 'get_cat_fact', die einen Katzenfakt abruft.
# Определяем функцию с именем 'get_cat_fact', которая получает факт о кошках.
def get_cat_fact():
    # Speichere die API-URL in einer Variablen.
    # Сохраняем URL API в переменной.
    url = 'https://catfact.ninja/fact'

    # Sende eine GET-Anfrage an die angegebene URL.
    # Отправляем GET-запрос по указанному URL.
    response = requests.get(url)

    # Überprüfe, ob die Antwort erfolgreich war (Statuscode 200).
    # Проверяем, был ли ответ успешным (код состояния 200).
    if response.status_code == 200:
        # Wandle die Antwort in ein JSON-Format um.
        # Преобразуем ответ в формат JSON.
        data = response.json()

        # Gib den Katzenfakt aus dem 'fact'-Feld aus.
        # Выводим факт о кошке из поля 'fact'.
        print(f"Zufälliger Fakt über Katzen: {data['fact']}")
    else:
        # Wenn der Statuscode nicht 200 ist, gib eine Fehlermeldung aus.
        # Если код состояния не 200, выводим сообщение об ошибке.
        print("Daten konnten nicht vom Server abgerufen werden.")
        # Данные не удалось получить с сервера.

# Rufe die Funktion auf, um den Katzenfakt anzuzeigen.
# Вызываем функцию, чтобы показать факт о кошке.
get_cat_fact()


"""
### **Задача 1. Напишите программу на Python, которая выводит случайные факты о кошках.**

В интернете существует множество сервисов, предоставляющих случайные факты через REST API.  
В этой задаче мы будем использовать сервис **CatFact Ninja**.

Этот сервис бесплатный и не требует регистрации.

1. Прежде чем писать программу, зайдите на сайт **CatFact Ninja API**.  
   Этот сайт позволяет отправлять запросы, чтобы получать случайные факты о кошках.  
   (Если на сайте потребуется заполнить форму о себе и вашей цели, можете написать что угодно.)

2. Найдите в документации пример запроса для получения случайного факта.  
   Пример запроса:  
   `https://catfact.ninja/fact`

3. Введите этот URL в браузере и посмотрите, какой результат вы получите.  
   Пример ответа:  
   ```json
   {
     "fact": "Кошки используют свои усы, чтобы понять, смогут ли они пролезть в узкое пространство.",
     "length": 63
   }
   ```

4. Изучите полученный ответ в формате JSON и найдите параметр `fact`, который содержит сам факт о кошках.

5. Теперь переходим к практике. Используйте библиотеку `requests` и напишите программу, которая отправляет запрос к API, получает случайный факт о кошках и выводит его пользователю.

📌 **Подсказка:** используйте следующий URL:  
`https://catfact.ninja/fact`

---

**Пример программы на Python:**
```python
import requests

def get_cat_fact():
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Случайный факт о кошках: {data['fact']}")
    else:
        print("Не удалось получить данные с сервера.")

get_cat_fact()
"""


"""
Отлично! Давай разберёмся, что такое REST API и как работает пример с CatFact Ninja.

---

## 📘 Что такое REST API?

**REST API (Representational State Transfer Application Programming Interface)** — это способ, с помощью которого разные программы могут "общаться" между собой через интернет.

Проще говоря:  
👉 REST API позволяет твоей программе **отправлять запрос** (например, "дай мне факт о кошках") на удалённый сервер,  
а сервер **отправляет в ответ данные** (например, "Кошки спят 70% своей жизни").

---

## 📩 Как это работает на практике?

Рассмотрим пошагово пример с CatFact Ninja:

### 1. URL (адрес запроса):
```
https://catfact.ninja/fact
```

Этот адрес — как дверь в офис, где сидят «кошачьи специалисты». Ты стучишь в неё с просьбой:  
*"Эй, скажите интересный факт о кошках!"*

---

### 2. HTTP-запрос:
Ты используешь метод `GET`, то есть говоришь:  
*"Дай мне информацию."*

Запрос делается с помощью библиотеки `requests` в Python:
```python
response = requests.get('https://catfact.ninja/fact')
```

---

### 3. Ответ от сервера (в формате JSON):
Сервер возвращает тебе что-то вроде:
```json
{
  "fact": "Кошки могут вращать уши на 180 градусов.",
  "length": 47
}
```

Это обычный словарь (dictionary) с двумя полями:
- `"fact"` — сам факт (тебе он и нужен!)
- `"length"` — длина этого факта (в символах)

---

### 4. Обработка ответа:
Ты превращаешь JSON-ответ в объект Python:
```python
data = response.json()
```

Теперь `data['fact']` — это строка с интересным фактом.

---

## 🛠 Что делает программа?

1. Отправляет запрос на `https://catfact.ninja/fact`
2. Получает JSON-ответ с фактом
3. Извлекает поле `"fact"` из ответа
4. Показывает его пользователю

---

## 🔁 Дополнительно

Ты можешь:
- вызывать функцию несколько раз, чтобы получать разные факты;
- сделать графический интерфейс;
- сохранять факты в файл;
- показывать длину факта (`length`) для интереса.

---

Хочешь, чтобы я добавил какие-то из этих дополнений в код?
"""
