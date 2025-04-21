# filmfinder_console.py
# Консольное приложение для поиска фильмов в базе данных sakila

from search_engine import search_by_keyword, search_by_genre_and_year, get_all_genres
from logger import log_query, get_top_queries

def print_menu():
    print("\n=== FilmFinder (Консольная версия) ===")
    print("1. Поиск фильмов по ключевому слову")
    print("2. Поиск фильмов по жанру и году")
    print("3. Показать популярные запросы")
    print("4. Выйти")

def handle_keyword_search():
    keyword = input("Введите ключевое слово: ")
    log_query(keyword)
    results = search_by_keyword(keyword)
    print("\nНайдено фильмов:")
    for title, description in results:
        print(f"- {title}: {description}")

def handle_genre_year_search():
    genres = get_all_genres()
    print("\nДоступные жанры:")
    for genre in genres:
        print(f"- {genre}")
    genre = input("Введите жанр: ")
    year = input("Введите год: ")
    log_query(f"{genre} {year}")
    results = search_by_genre_and_year(genre, year)
    print("\nНайдено фильмов:")
    for title, description in results:
        print(f"- {title}: {description}")

def handle_show_popular_queries():
    print("\nТоп популярных запросов:")
    for query, count in get_top_queries():
        print(f"{query} — {count} раз")

def main():
    while True:
        print_menu()
        choice = input("Выберите действие: ")
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

if __name__ == "__main__":
    main()
