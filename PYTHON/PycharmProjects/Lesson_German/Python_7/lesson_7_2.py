"""
Aufgabe 2. Schreiben Sie ein Python-Programm,
das Informationen über einen Film anhand des Titels abruft,
unter Verwendung der API von The Movie Database (TMDB).
The Movie Database (TMDB) bietet Informationen über Filme
und Serien über eine REST-API an. Dieser Dienst ist kostenlos,
erfordert jedoch eine Registrierung und die Erstellung eines API-Schlüssels.

1. Registrieren Sie sich auf der Website TMDB und erstellen Sie ein Konto.
   Nach der Registrierung finden Sie Ihren API-Schlüssel in den Kontoeinstellungen.
2. Besuchen Sie die Dokumentation zur Filmsuche und erfahren Sie, wie eine Anfrage
   zur Filminformation über den Titel gesendet wird.
   (https://developer.themoviedb.org/reference/search-movie)
3. Ein Beispiel für eine Anfrage zur Filmabfrage sieht wie folgt aus:
   https://api.themoviedb.org/3/search/movie?api_key=IHR_SCHLÜSSEL&query=Inception
   Wo IHR_SCHLÜSSEL Ihr API-Schlüssel ist und query=Inception der Titel des Films ist,
   den Sie suchen.
4. Geben Sie diese URL in Ihren Browser ein und überprüfen Sie das Ergebnis.
   Beispiel für eine Antwort:

   {
     "page": 1,
     "results": [
       { <...>
         "title": "Inception",
          <...>
         "release_date": "2010-07-15",
          <...>
         "overview": "A thief who steals corporate secrets ...",
          <...>
         "vote_average": 8.3
<...> }
],
     "total_results": 1
   }
5. Untersuchen Sie die JSON-Antwort und finden Sie die Parameter title, release_date,
   overview und vote_average.
6. Nun gehen wir zur Praxis über.
   Verwenden Sie die Bibliothek requests
   und schreiben Sie ein Programm, das den Benutzer nach einem Filmtitel fragt,
   eine Anfrage an die TMDB-API sendet und die wichtigsten Informationen über den Film
   ausgibt, wie z. B. den Titel, das Veröffentlichungsdatum, die Zusammenfassung
   und die Bewertung.
Hinweis: Verwenden Sie eine URL wie:
https://api.themoviedb.org/3/search/movie?api_key=IHR_SCHLÜSSEL&query=FILMTITEL
Beispiel eines Python-Programms:

   import requests
   def get_movie_info(movie_name):
       api_key = 'IHR_SCHLÜSSEL'
url =
   f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name
   }'
       response = requests.get(url)
       if response.status_code == 200:
           data = response.json()
           if data['results']:
               movie = data['results'][0]
               print(f"Filmtitel: {movie['title']}")
               print(f"Veröffentlichungsdatum: {movie['release_date']}")
               print(f"Beschreibung: {movie['overview']}")
               print(f"Bewertung: {movie['vote_average']}")
           else:
               print("Film nicht gefunden.")

       else:
        print("Daten konnten nicht vom Server abgerufen werden.")
movie_name = input("Geben Sie den Titel des Films ein: ")
get_movie_info(movie_name)

"""
"""
### **Задача 2. Напишите программу на Python, 
которая получает информацию о фильме по его названию, 
используя API The Movie Database (TMDB).**
Сервис **The Movie Database (TMDB)** предоставляет информацию о фильмах 
и сериалах через REST API.  
Этот сервис бесплатный, но требует регистрации и получения API-ключа.

**Шаги:**

1. Зарегистрируйтесь на сайте TMDB и создайте учётную запись.  
   После регистрации вы найдёте свой API-ключ в настройках аккаунта.

2. Перейдите к документации по поиску фильмов, чтобы узнать, как отправляется запрос на получение информации о фильме по его названию.  
   [Документация TMDB по поиску фильма](https://developer.themoviedb.org/reference/search-movie)

3. Пример запроса:
   ```
   https://api.themoviedb.org/3/search/movie?api_key=ВАШ_КЛЮЧ&query=Inception
   ```
   Где `ВАШ_КЛЮЧ` — ваш API-ключ, а `query=Inception` — название фильма, который вы ищете.

4. Введите URL в браузере и посмотрите, какой ответ вернёт сервер.  
   Пример ответа (JSON):
   ```json
   {
     "page": 1,
     "results": [
       {
         "title": "Inception",
         "release_date": "2010-07-15",
         "overview": "A thief who steals corporate secrets ...",
         "vote_average": 8.3
       }
     ],
     "total_results": 1
   }
   ```

5. Изучите JSON-ответ и обратите внимание на поля:
   - `title` — название фильма  
   - `release_date` — дата выхода  
   - `overview` — краткое описание  
   - `vote_average` — средняя оценка

6. Теперь реализуйте это на практике:  
   Используйте библиотеку `requests` и напишите программу, которая:
   - запрашивает у пользователя название фильма,  
   - отправляет запрос к TMDB API,  
   - выводит основную информацию о фильме (название, дата выхода, описание, оценка).

📌 **Подсказка:**  
Используйте URL такого вида:
```
https://api.themoviedb.org/3/search/movie?api_key=ВАШ_КЛЮЧ&query=НАЗВАНИЕ_ФИЛЬМА
"""


## 🧠 Python-программа с псевдокодом (DE + RU)
# Importiere die Bibliothek 'requests', um HTTP-Anfragen zu senden.
# Импортируем библиотеку 'requests' для отправки HTTP-запросов.
import requests

# Definiere eine Funktion mit dem Namen 'get_movie_info', die den Filmtitel als Eingabe erhält.
# Определяем функцию с именем 'get_movie_info', которая принимает название фильма как входной параметр.
def get_movie_info(movie_name):
    # Speichere deinen API-Schlüssel in einer Variablen.
    # Сохраняем ваш API-ключ в переменной.
    api_key = 'DEIN_API_SCHLÜSSEL'  # ← здесь нужно подставить ваш реальный ключ

    # Erstelle die URL für die Anfrage mit dem API-Schlüssel und dem Filmtitel.
    # Формируем URL запроса с API-ключом и названием фильма.
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}'

    # Sende eine GET-Anfrage an die TMDB-API.
    # Отправляем GET-запрос к TMDB-API.
    response = requests.get(url)

    # Überprüfe, ob die Anfrage erfolgreich war (Statuscode 200).
    # Проверяем, был ли запрос успешным (код 200).
    if response.status_code == 200:
        # Wandle die Antwort in ein JSON-Format um.
        # Преобразуем ответ в формат JSON.
        data = response.json()

        # Überprüfe, ob in den Ergebnissen mindestens ein Film vorhanden ist.
        # Проверяем, есть ли хотя бы один фильм в результатах.
        if data['results']:
            # Nimm den ersten Film aus der Ergebnisliste.
            # Берём первый фильм из списка результатов.
            movie = data['results'][0]

            # Gib den Titel des Films aus.
            # Выводим название фильма.
            print(f"Filmtitel: {movie['title']}")

            # Gib das Veröffentlichungsdatum des Films aus.
            # Выводим дату выхода фильма.
            print(f"Veröffentlichungsdatum: {movie['release_date']}")

            # Gib die Zusammenfassung (Übersicht) des Films aus.
            # Выводим краткое описание фильма.
            print(f"Beschreibung: {movie['overview']}")

            # Gib die durchschnittliche Bewertung des Films aus.
            # Выводим среднюю оценку фильма.
            print(f"Bewertung: {movie['vote_average']}")
        else:
            # Wenn keine Ergebnisse gefunden wurden, informiere den Benutzer.
            # Если ничего не найдено, сообщаем об этом пользователю.
            print("Film nicht gefunden.")  # Фильм не найден.
    else:
        # Wenn die Anfrage fehlgeschlagen ist, gib eine Fehlermeldung aus.
        # Если запрос не удался, выводим сообщение об ошибке.
        print("Daten konnten nicht vom Server abgerufen werden.")
        # Не удалось получить данные с сервера.

# Fordere den Benutzer auf, einen Filmtitel einzugeben.
# Запрашиваем у пользователя ввод названия фильма.
movie_name = input("Geben Sie den Titel des Films ein: ")

# Rufe die Funktion mit dem eingegebenen Filmtitel auf.
# Вызываем функцию с введённым названием фильма.
get_movie_info(movie_name)
