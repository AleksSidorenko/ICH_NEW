# search_engine.py
# Модуль для выполнения поиска фильмов в базе данных sakila

import mysql.connector              # Импортируем библиотеку для подключения к MySQL
from config import dbconfig        # Импортируем настройки подключения из модуля config

# Функция для подключения к базе данных
def get_connection():
    return mysql.connector.connect(**dbconfig)  # Создаём и возвращаем объект подключения к базе данных с параметрами из конфигурации

# Функция для получения всех жанров из таблицы category
def get_all_genres():
    try:
        conn = get_connection()             # Подключаемся к базе данных
        cursor = conn.cursor()              # Создаём курсор для выполнения SQL-запросов
        cursor.execute("SELECT name FROM category ORDER BY name;")  # Выполняем SQL-запрос на получение всех жанров
        genres = [row[0] for row in cursor.fetchall()]  # Преобразуем результат в список строк
        cursor.close()                      # Закрываем курсор
        conn.close()                        # Закрываем соединение с базой данных
        return genres                       # Возвращаем список жанров
    except mysql.connector.Error as err:
        print("Ошибка при получении жанров:", err)  # Обработка ошибок при работе с базой
        return []

# Функция для поиска фильмов по ключевому слову в названии или описании
def search_by_keyword(keyword):
    try:
        conn = get_connection()             # Подключаемся к базе данных
        cursor = conn.cursor()              # Создаём курсор
        query = (
            "SELECT title, description FROM film "
            "WHERE title LIKE %s OR description LIKE %s "
            "LIMIT 10;"                     # Используем параметризованный SQL-запрос
        )
        # ПАРАМЕТРИЗАЦИЯ: Используем параметры запроса (второй аргумент execute)
        # Это гарантирует защиту от SQL-инъекций, т.к. MySQL сам экранирует значения
        cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))  # Выполняем запрос с подстановкой значений
        results = cursor.fetchall()         # Получаем результаты запроса
        cursor.close()                      # Закрываем курсор
        conn.close()                        # Закрываем соединение с базой данных
        return results                      # Возвращаем список найденных фильмов
    except mysql.connector.Error as err:
        print("Ошибка при поиске по ключевому слову:", err)
        return []

# Функция для поиска фильмов по жанру и году выпуска
def search_by_genre_and_year(genre, year):
    try:
        conn = get_connection()             # Подключаемся к базе данных
        cursor = conn.cursor()              # Создаём курсор
        query = (
            "SELECT f.title, f.description "
            "FROM film f "
            "JOIN film_category fc ON f.film_id = fc.film_id "
            "JOIN category c ON fc.category_id = c.category_id "
            "WHERE c.name = %s AND f.release_year = %s "
            "LIMIT 10;"                     # Используем параметризованный SQL-запрос с JOIN
        )
        # ПАРАМЕТРИЗАЦИЯ: значения genre и year передаются как отдельные аргументы
        # Это полностью предотвращает возможность SQL-инъекций
        # Что это означает:
        # - MySQL сам экранирует значения genre и year
        # - Пользователь не может подставить вредоносный код (например, "' OR 1=1")
        # - Безопасность запросов гарантирована
        cursor.execute(query, (genre, year))  # Выполняем запрос
        results = cursor.fetchall()         # Получаем результаты
        cursor.close()                      # Закрываем курсор
        conn.close()                        # Закрываем соединение
        return results                      # Возвращаем список фильмов
    except mysql.connector.Error as err:
        print("Ошибка при поиске по жанру и году:", err)
        return []
