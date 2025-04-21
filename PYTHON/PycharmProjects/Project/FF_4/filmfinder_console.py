# filmfinder_console.py
# Основной модуль консольного приложения для поиска фильмов

from search_engine import search_by_keyword, search_by_genre_and_year, get_all_genres
# Импорт функций поиска из модуля search_engine

from logger import log_query, get_top_queries
# Импорт логирования и получения популярных запросов

# Функция отображения главного меню
def print_menu():
    print("\n=== FilmFinder (Консольная версия) ===")
    print("1. Поиск фильмов по ключевому слову")
    print("2. Поиск фильмов по жанру и году")
    print("3. Показать популярные запросы")
    print("4. Выйти")

# Обработка поиска по ключевому слову
def handle_keyword_search():
    keyword = input("Введите ключевое слово: ")   # Запрос у пользователя
    log_query(keyword)                            # Логируем запрос
    results = search_by_keyword(keyword)          # Получаем результаты поиска
    print("\nНайдено фильмов:")
    for title, description in results:            # Выводим каждый результат
        print(f"- {title}: {description}")

# Обработка поиска по жанру и году
def handle_genre_year_search():
    genres = get_all_genres()                     # Получаем доступные жанры
    print("\nДоступные жанры:")
    for genre in genres:                          # Выводим список жанров
        print(f"- {genre}")
    genre = input("Введите жанр: ")               # Запрос жанра
    year = input("Введите год: ")                 # Запрос года
    log_query(f"{genre} {year}")                  # Логируем запрос
    results = search_by_genre_and_year(genre, year)  # Получаем результаты
    print("\nНайдено фильмов:")
    for title, description in results:            # Выводим каждый результат
        print(f"- {title}: {description}")

# Обработка отображения популярных запросов
def handle_show_popular_queries():
    print("\nТоп популярных запросов:")
    for query, count in get_top_queries():        # Получаем и выводим каждый запрос
        print(f"{query} — {count} раз")

# Основная функция (точка входа в программу)
def main():
    while True:                                   # Бесконечный цикл до выхода
        print_menu()                              # Показываем меню
        choice = input("Выберите действие: ")     # Получаем выбор пользователя
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

# Проверка, что скрипт запущен напрямую
if __name__ == "__main__":
    main()
