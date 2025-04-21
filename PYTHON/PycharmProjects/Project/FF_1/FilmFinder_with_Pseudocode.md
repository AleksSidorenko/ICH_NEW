
# 🎬 FilmFinder — Полная структура проекта с псевдокодом

---

## 📁 1. config.py

```python
# Псевдокод:
# Хранит параметры подключения к двум базам данных:
# - sakila (для поиска фильмов)
# - film_logs (для хранения логов запросов)

db_sakila = {
    'host': 'адрес хоста',
    'user': 'пользователь',
    'password': 'пароль',
    'database': 'sakila'
}

db_log = {
    'host': 'адрес хоста',
    'user': 'пользователь',
    'password': 'пароль',
    'database': 'film_logs'
}
```

---

## 🧾 2. logger.py

```python
# Псевдокод:
# Класс QueryLogger:
# - подключается к базе film_logs
# - log_query(): сохраняет поисковый запрос
# - get_popular_queries(): возвращает 10 самых популярных запросов

import mysql.connector
from datetime import datetime
from config import db_log

class QueryLogger:
    def __init__(self):
        self.conn = mysql.connector.connect(**db_log)
        self.cursor = self.conn.cursor(dictionary=True)

    def log_query(self, query_text, search_type):
        sql = "INSERT INTO query_log (query_text, search_type, created_at) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (query_text, search_type, datetime.now()))
        self.conn.commit()

    def get_popular_queries(self, limit=10):
        sql = '''
            SELECT query_text, COUNT(*) AS count
            FROM query_log
            GROUP BY query_text
            ORDER BY count DESC
            LIMIT %s
        '''
        self.cursor.execute(sql, (limit,))
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
```

---

## 🔍 3. search_engine.py

```python
# Псевдокод:
# Класс FilmSearcher:
# - search_by_keyword(): ищет фильмы по ключевым словам в title и description
# - search_by_genre_year(): ищет фильмы по выбранному жанру и году
# - get_all_genres(): получает список всех жанров из таблицы category

import mysql.connector
from config import db_sakila

class FilmSearcher:
    def __init__(self):
        self.conn = mysql.connector.connect(**db_sakila)
        self.cursor = self.conn.cursor(dictionary=True)

    def search_by_keyword(self, keyword):
        sql = '''
            SELECT title, description, release_year
            FROM film
            WHERE title LIKE %s OR description LIKE %s
            LIMIT 10
        '''
        param = f"%{keyword}%"
        self.cursor.execute(sql, (param, param))
        return self.cursor.fetchall()

    def search_by_genre_year(self, genre, year):
        sql = '''
            SELECT f.title, f.description, f.release_year
            FROM film f
            JOIN film_category fc ON f.film_id = fc.film_id
            JOIN category c ON fc.category_id = c.category_id
            WHERE c.name = %s AND f.release_year = %s
            LIMIT 10
        '''
        self.cursor.execute(sql, (genre, year))
        return self.cursor.fetchall()

    def get_all_genres(self):
        self.cursor.execute("SELECT name FROM category ORDER BY name")
        return [row["name"] for row in self.cursor.fetchall()]

    def __del__(self):
        self.cursor.close()
        self.conn.close()
```

---

## 🖼️ 4. filmfinder_gui.py

```python
# Псевдокод:
# Класс FilmFinderApp (наследует tk.Tk):
# - содержит 3 вкладки: поиск по ключевому слову, по жанру и году, популярные запросы
# - каждая вкладка содержит виджеты: Entry, Combobox, Text, Button
# - методы:
#   - search_by_keyword()
#   - search_by_genre_year()
#   - show_popular_queries()
#   - display_results(): отображение результатов поиска
#   - style_ui(): применение стилей через ttk.Style

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

        # Вкладка 1: По ключевому слову
        self.keyword_frame = ttk.Frame(notebook)
        notebook.add(self.keyword_frame, text="🔍 По ключевому слову")

        self.keyword_entry = ttk.Entry(self.keyword_frame, width=50)
        self.keyword_entry.pack(pady=10)

        ttk.Button(self.keyword_frame, text="Найти", command=self.search_by_keyword).pack()
        self.keyword_results = tk.Text(self.keyword_frame, height=20)
        self.keyword_results.pack(expand=True, fill="both", padx=10, pady=10)

        # Вкладка 2: По жанру и году
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
