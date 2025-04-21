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
