# FilmFinderConsoleApp
## Описание
Консольное приложение для поиска фильмов по базе данных Sakila. Логирование поисковых запросов реализовано в оперативной памяти.

## Структура проекта
- `config.py`: Конфигурация подключения к БД
- `logger.py`: Временное логирование запросов
- `search_engine.py`: Поисковая логика
- `filmfinder_console.py`: Основной консольный интерфейс

## Запуск
```bash
python3 filmfinder_console.py
```

## Подробный псевдокод в исходном коде

### `config.py`
```python
# config.py
# Модуль конфигурации для подключения к базе данных sakila

# Словарь с параметрами подключения к MySQL базе данных
# 'host' — адрес сервера базы данных
# 'user' — имя пользователя
# 'password' — пароль для подключения
# 'database' — имя базы данных
dbconfig = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',  # Хост MySQL сервера
    'user': 'ich1',                                                # Имя пользователя базы данных
    'password': 'password',                                        # Пароль пользователя
    'database': 'sakila'                                           # Название базы данных
}

```

### `logger.py`
```python
# logger.py
# Модуль логирования поисковых запросов (в памяти, без базы данных)

from collections import Counter  # Импортируем Counter для подсчёта количества одинаковых запросов

# Глобальная переменная — словарь для хранения количества каждого поискового запроса
query_log_memory = Counter()

# Функция логирования поискового запроса
def log_query(query: str):
    # Приводим запрос к нижнему регистру и удаляем пробелы в начале и конце
    normalized_query = query.strip().lower()
    # Увеличиваем счётчик для этого запроса
    query_log_memory[normalized_query] += 1

# Функция получения самых популярных запросов
def get_top_queries(limit=10):
    # Возвращает limit самых частых запросов в виде списка кортежей (запрос, количество)
    return query_log_memory.most_common(limit)

```

### `search_engine.py`
```python
# search_engine.py
# Модуль для выполнения поиска фильмов в базе данных sakila

import mysql.connector              # Импортируем библиотеку для подключения к MySQL
from config import dbconfig        # Импортируем настройки подключения из модуля config

# Функция для подключения к базе данных
def get_connection():
    return mysql.connector.connect(**dbconfig)  # Возвращает объект подключения к базе

# Функция для получения всех жанров из таблицы category
def get_all_genres():
    try:
        conn = get_connection()             # Подключаемся к базе
        cursor = conn.cursor()              # Создаём курсор
        cursor.execute("SELECT name FROM category ORDER BY name;")  # SQL-запрос на получение жанров
        genres = [row[0] for row in cursor.fetchall()]              # Извлекаем результат запроса в список
        cursor.close()                      # Закрываем курсор
        conn.close()                        # Закрываем соединение
        return genres                       # Возвращаем список жанров
    except mysql.connector.Error as err:
        print("Ошибка при получении жанров:", err)  # Обработка ошибки
        return []

# Функция для поиска фильмов по ключевому слову в названии или описании
def search_by_keyword(keyword):
    try:
        conn = get_connection()             # Подключаемся к базе
        cursor = conn.cursor()              # Создаём курсор
        query = (
            "SELECT title, description FROM film "
            "WHERE title LIKE %s OR description LIKE %s "
            "LIMIT 10;"
        )                                   # SQL-запрос с параметрами поиска
        cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))  # Подставляем параметры
        results = cursor.fetchall()         # Получаем результаты
        cursor.close()                      # Закрываем курсор
        conn.close()                        # Закрываем соединение
        return results                      # Возвращаем список найденных фильмов
    except mysql.connector.Error as err:
        print("Ошибка при поиске по ключевому слову:", err)
        return []

# Функция для поиска фильмов по жанру и году
def search_by_genre_and_year(genre, year):
    try:
        conn = get_connection()             # Подключаемся к базе
        cursor = conn.cursor()              # Создаём курсор
        query = (
            "SELECT f.title, f.description "
            "FROM film f "
            "JOIN film_category fc ON f.film_id = fc.film_id "
            "JOIN category c ON fc.category_id = c.category_id "
            "WHERE c.name = %s AND f.release_year = %s "
            "LIMIT 10;"
        )                                   # SQL-запрос с JOIN для фильтрации по жанру и году
        cursor.execute(query, (genre, year))  # Выполняем запрос
        results = cursor.fetchall()         # Получаем результаты
        cursor.close()                      # Закрываем курсор
        conn.close()                        # Закрываем соединение
        return results                      # Возвращаем список найденных фильмов
    except mysql.connector.Error as err:
        print("Ошибка при поиске по жанру и году:", err)
        return []

```

### `filmfinder_console.py`
```python
# filmfinder_console.py
# Основной модуль консольного приложения для поиска фильмов

from search_engine import search_by_keyword, search_by_genre_and_year, get_all_genres
# Импорт функций поиска из модуля search_engine

from logger import log_query, get_top_queries
# Импорт логирования и получения популярных запросов

# Функция отображения главного меню
def print_menu():
    print("\n=== FilmFinder (Консольная версия) ===")
    print("1. Поиск фильмов по ключевому слову")
    print("2. Поиск фильмов по жанру и году")
    print("3. Показать популярные запросы")
    print("4. Выйти")

# Обработка поиска по ключевому слову
def handle_keyword_search():
    keyword = input("Введите ключевое слово: ")   # Запрос у пользователя
    log_query(keyword)                            # Логируем запрос
    results = search_by_keyword(keyword)          # Получаем результаты поиска
    print("\nНайдено фильмов:")
    for title, description in results:            # Выводим каждый результат
        print(f"- {title}: {description}")

# Обработка поиска по жанру и году
def handle_genre_year_search():
    genres = get_all_genres()                     # Получаем доступные жанры
    print("\nДоступные жанры:")
    for genre in genres:                          # Выводим список жанров
        print(f"- {genre}")
    genre = input("Введите жанр: ")               # Запрос жанра
    year = input("Введите год: ")                 # Запрос года
    log_query(f"{genre} {year}")                  # Логируем запрос
    results = search_by_genre_and_year(genre, year)  # Получаем результаты
    print("\nНайдено фильмов:")
    for title, description in results:            # Выводим каждый результат
        print(f"- {title}: {description}")

# Обработка отображения популярных запросов
def handle_show_popular_queries():
    print("\nТоп популярных запросов:")
    for query, count in get_top_queries():        # Получаем и выводим каждый запрос
        print(f"{query} — {count} раз")

# Основная функция (точка входа в программу)
def main():
    while True:                                   # Бесконечный цикл до выхода
        print_menu()                              # Показываем меню
        choice = input("Выберите действие: ")     # Получаем выбор пользователя
        if choice == "1":
            handle_keyword_search()
        elif choice == "2":
            handle_genre_year_search()
        elif choice == "3":
            handle_show_popular_queries()
        elif choice == "4":
            print("Выход из приложения.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

# Проверка, что скрипт запущен напрямую
if __name__ == "__main__":
    main()

```
