# filmfinder_console.py
# Псевдокод:
# Основной интерфейс взаимодействия с пользователем через консоль
# Вызывает search_engine и logger
# Отображает меню и обрабатывает команды

from search_engine import search_by_keyword, search_by_genre_and_year, get_genres
from logger import log_query, get_top_queries

def main_menu():
    while True:
        print("\n=== FilmFinder (Консольная версия) ===")
        print("1. Поиск фильмов по ключевому слову")
        print("2. Поиск фильмов по жанру и году")
        print("3. Показать популярные запросы")
        print("4. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            keyword = input("Введите ключевое слово: ").strip()
            results = search_by_keyword(keyword)
            log_query(keyword)
            print("\nНайдено фильмов:")
            for i, (title, year) in enumerate(results, 1):
                print(f"{i}. {title} ({year})")

        elif choice == '2':
            genres = get_genres()
            print("\nДоступные жанры:")
            for g in genres:
                print(f"- {g}")
            genre = input("Введите жанр: ").strip()
            year = input("Введите год: ").strip()
            results = search_by_genre_and_year(genre, year)
            log_query(f"{genre} {year}")
            print("\nНайдено фильмов:")
            for i, (title, year) in enumerate(results, 1):
                print(f"{i}. {title} ({year})")

        elif choice == '3':
            print("\nТоп популярных запросов:")
            top_queries = get_top_queries()
            for i, (query, count) in enumerate(top_queries, 1):
                print(f"{i}. {query} — {count} раз")

        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()