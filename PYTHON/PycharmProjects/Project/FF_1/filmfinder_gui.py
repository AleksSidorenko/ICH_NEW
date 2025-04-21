
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
