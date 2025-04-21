# search_engine.py
# Псевдокод:
# Содержит SQL-запросы и функции для поиска фильмов по разным сценариям
# Взаимодействует с основной базой данных sakila

import mysql.connector
from config import dbconfig

def search_by_keyword(keyword):
    try:
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title, release_year 
            FROM film 
            WHERE title LIKE %s 
            LIMIT 10;
        """, (f"%{keyword}%",))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except mysql.connector.Error as err:
        print("Ошибка при поиске по ключевому слову:", err)
        return []

def get_genres():
    try:
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM category;")
        genres = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return genres
    except mysql.connector.Error as err:
        print("Ошибка при получении жанров:", err)
        return []

def search_by_genre_and_year(genre, year):
    try:
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT f.title, f.release_year
            FROM film f
            JOIN film_category fc ON f.film_id = fc.film_id
            JOIN category c ON fc.category_id = c.category_id
            WHERE c.name = %s AND f.release_year = %s
            LIMIT 10;
        """, (genre, year))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except mysql.connector.Error as err:
        print("Ошибка при поиске по жанру и году:", err)
        return []