
# 🎬 FilmFinder — Финальное приложение с подробным псевдокодом и Python-кодом

---

## 📁 config.py

```python
# config.py

# ===============================
# Псевдокод:
# - Храним параметры подключения к двум базам данных:
#   - sakila: основная база фильмов
#   - film_logs: база для хранения логов поисковых запросов
# ===============================

db_sakila = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password',
    'database': 'sakila'
}

db_log = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password',
    'database': 'film_logs'
}

```

---

## 🧾 logger.py

```python
# logger.py

# ===============================
# Псевдокод:
# - Класс QueryLogger:
#     - подключается к базе film_logs
#     - сохраняет запросы пользователя в таблицу query_log
#     - получает самые частые запросы
#     - при удалении объекта закрывает соединение
# ===============================

import mysql.connector
from datetime import datetime
from config import db_log

class QueryLogger:
    def __init__(self):
        # Подключение к базе логов
        self.conn = mysql.connector.connect(**db_log)
        self.cursor = self.conn.cursor(dictionary=True)

    def log_query(self, query_text, search_type):
        # Сохраняет поисковый запрос в таблицу логов
        sql = "INSERT INTO query_log (query_text, search_type, created_at) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (query_text, search_type, datetime.now()))
        self.conn.commit()

    def get_popular_queries(self, limit=10):
        # Получает наиболее популярные (повторяющиеся) поисковые запросы
        sql = (
            "SELECT query_text, COUNT(*) AS count "
            "FROM query_log "
            "GROUP BY query_text "
            "ORDER BY count DESC "
            "LIMIT %s"
        )
        self.cursor.execute(sql, (limit,))
        return self.cursor.fetchall()

    def __del__(self):
        # Закрывает соединение при завершении
        self.cursor.close()
        self.conn.close()

```

---

## 🔍 search_engine.py

```python
# search_engine.py

# ===============================
# Псевдокод:
# - Класс FilmSearcher:
#     - подключается к базе sakila
#     - выполняет поиск фильмов:
#         - по ключевому слову
#         - по жанру и году
#         - получает список жанров
#     - при удалении объекта закрывает соединение
# ===============================

import mysql.connector
from config import db_sakila

class FilmSearcher:
    def __init__(self):
        # Подключение к базе фильмов
        self.conn = mysql.connector.connect(**db_sakila)
        self.cursor = self.conn.cursor(dictionary=True)

    def search_by_keyword(self, keyword):
        # Поиск фильмов, где ключевое слово содержится в названии или описании
        sql = (
            "SELECT title, description, release_year "
            "FROM film "
            "WHERE title LIKE %s OR description LIKE %s "
            "LIMIT 10"
        )
        param = f"%{keyword}%"
        self.cursor.execute(sql, (param, param))
        return self.cursor.fetchall()

    def search_by_genre_year(self, genre, year):
        # Поиск фильмов по жанру (категории) и году выпуска
        sql = (
            "SELECT f.title, f.description, f.release_year "
            "FROM film f "
            "JOIN film_category fc ON f.film_id = fc.film_id "
            "JOIN category c ON fc.category_id = c.category_id "
            "WHERE c.name = %s AND f.release_year = %s "
            "LIMIT 10"
        )
        self.cursor.execute(sql, (genre, year))
        return self.cursor.fetchall()

    def get_all_genres(self):
        # Получает список всех доступных жанров (категорий)
        self.cursor.execute("SELECT name FROM category ORDER BY name")
        return [row["name"] for row in self.cursor.fetchall()]

    def __del__(self):
        # Закрывает соединение при завершении
        self.cursor.close()
        self.conn.close()

```

---

## 🖼️ filmfinder_gui.py

```python

# filmfinder_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from search_engine import FilmSearcher
from logger import QueryLogger


class FilmFinderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎬 FilmFinder - Поиск фильмов")
        self.geometry("800x600")
        self.searcher = FilmSearcher()
        self.logger = QueryLogger()
        self.create_widgets()
        self.style_ui()

    def create_widgets(self):
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        # Вкладка 1: Поиск по ключевому слову
        self.keyword_frame = ttk.Frame(notebook)
        notebook.add(self.keyword_frame, text="🔍 По ключевому слову")

        self.keyword_entry = ttk.Entry(self.keyword_frame, width=50)
        self.keyword_entry.pack(pady=10)

        ttk.Button(self.keyword_frame, text="Найти", command=self.search_by_keyword).pack()
        self.keyword_results = tk.Text(self.keyword_frame, height=20)
        self.keyword_results.pack(expand=True, fill="both", padx=10, pady=10)

        # Вкладка 2: Поиск по жанру и году
        self.genre_year_frame = ttk.Frame(notebook)
        notebook.add(self.genre_year_frame, text="🎞 По жанру и году")

        self.genre_combo = ttk.Combobox(self.genre_year_frame, state="readonly", values=self.searcher.get_all_genres())
        self.genre_combo.set("Выберите жанр")
        self.genre_combo.pack(pady=10)

        self.year_entry = ttk.Entry(self.genre_year_frame)
        self.year_entry.pack(pady=5)
        self.year_entry.insert(0, "Введите год")

        ttk.Button(self.genre_year_frame, text="Найти", command=self.search_by_genre_year).pack()
        self.genre_results = tk.Text(self.genre_year_frame, height=20)
        self.genre_results.pack(expand=True, fill="both", padx=10, pady=10)

        # Вкладка 3: Популярные запросы
        self.popular_frame = ttk.Frame(notebook)
        notebook.add(self.popular_frame, text="🔥 Популярные запросы")

        ttk.Button(self.popular_frame, text="Показать популярные", command=self.show_popular_queries).pack(pady=10)
        self.popular_results = tk.Text(self.popular_frame, height=20)
        self.popular_results.pack(expand=True, fill="both", padx=10, pady=10)

    def search_by_keyword(self):
        keyword = self.keyword_entry.get()
        if not keyword.strip():
            messagebox.showwarning("Внимание", "Введите ключевое слово.")
            return
        results = self.searcher.search_by_keyword(keyword)
        self.logger.log_query(keyword, "keyword")
        self.display_results(self.keyword_results, results)

    def search_by_genre_year(self):
        genre = self.genre_combo.get()
        year = self.year_entry.get()
        if genre == "Выберите жанр" or not year.isdigit():
            messagebox.showwarning("Внимание", "Выберите жанр и введите корректный год.")
            return
        results = self.searcher.search_by_genre_year(genre, int(year))
        self.logger.log_query(f"{genre}, {year}", "genre_year")
        self.display_results(self.genre_results, results)

    def show_popular_queries(self):
        queries = self.logger.get_popular_queries()
        formatted = "\n".join([f"{i+1}. {q['query_text']} ({q['count']})" for i, q in enumerate(queries)])
        self.popular_results.delete("1.0", tk.END)
        self.popular_results.insert(tk.END, formatted)

    def display_results(self, text_widget, results):
        text_widget.delete("1.0", tk.END)
        if results:
            for film in results:
                text_widget.insert(tk.END, f"{film['title']} ({film['release_year']})\nОписание: {film['description']}\n\n")
        else:
            text_widget.insert(tk.END, "Ничего не найдено.")

    def style_ui(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6, font=("Arial", 10))
        style.configure("TNotebook.Tab", font=("Arial", 11, "bold"))
        style.configure("TEntry", padding=4)
        style.configure("TCombobox", padding=4)


if __name__ == "__main__":
    app = FilmFinderApp()
    app.mainloop()

```
