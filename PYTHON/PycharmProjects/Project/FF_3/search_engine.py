# search_engine.py
# Модуль для выполнения поиска фильмов в базе данных sakila

import mysql.connector
from config import dbconfig

def get_connection():
    return mysql.connector.connect(**dbconfig)

def get_all_genres():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM category ORDER BY name;")
        genres = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return genres
    except mysql.connector.Error as err:
        print("Ошибка при получении жанров:", err)
        return []

def search_by_keyword(keyword):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = (
            "SELECT title, description FROM film "
            "WHERE title LIKE %s OR description LIKE %s "
            "LIMIT 10;"
        )
        cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except mysql.connector.Error as err:
        print("Ошибка при поиске по ключевому слову:", err)
        return []

def search_by_genre_and_year(genre, year):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = (
            "SELECT f.title, f.description "
            "FROM film f "
            "JOIN film_category fc ON f.film_id = fc.film_id "
            "JOIN category c ON fc.category_id = c.category_id "
            "WHERE c.name = %s AND f.release_year = %s "
            "LIMIT 10;"
        )
        cursor.execute(query, (genre, year))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except mysql.connector.Error as err:
        print("Ошибка при поиске по жанру и году:", err)
        return []
