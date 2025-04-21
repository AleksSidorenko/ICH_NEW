
# search_engine.py

import mysql.connector
from config import db_sakila

class FilmSearcher:
    def __init__(self):
        self.conn = mysql.connector.connect(**db_sakila)
        self.cursor = self.conn.cursor(dictionary=True)

    def search_by_keyword(self, keyword):
        sql = """
            SELECT title, description, release_year
            FROM film
            WHERE title LIKE %s OR description LIKE %s
            LIMIT 10
        """
        param = f"%{keyword}%"
        self.cursor.execute(sql, (param, param))
        return self.cursor.fetchall()

    def search_by_genre_year(self, genre, year):
        sql = """
            SELECT f.title, f.description, f.release_year
            FROM film f
            JOIN film_category fc ON f.film_id = fc.film_id
            JOIN category c ON fc.category_id = c.category_id
            WHERE c.name = %s AND f.release_year = %s
            LIMIT 10
        """
        self.cursor.execute(sql, (genre, year))
        return self.cursor.fetchall()

    def get_all_genres(self):
        self.cursor.execute("SELECT name FROM category ORDER BY name")
        return [row["name"] for row in self.cursor.fetchall()]

    def __del__(self):
        self.cursor.close()
        self.conn.close()
