# filmfinder_console.py
# Основной модуль консольного приложения FilmFinder
# Взаимодействие с пользователем реализовано через CLI с помощью библиотеки questionary

import questionary  # Импортируем библиотеку для создания интерактивных выпадающих списков в терминале
from search_engine import search_by_keyword, search_by_genre_and_year, get_all_genres  # Импортируем функции поиска из внешнего модуля
from logger import log_query, get_top_queries  # Импортируем функции логирования пользовательских запросов

# Словарь соответствия жанров и эмодзи для красивого отображения
GENRE_EMOJIS = {
    "Action": "💥",         # Эмодзи для жанра Action
    "Animation": "🎨",      # Эмодзи для жанра Animation
    "Comedy": "😂",         # Эмодзи для жанра Comedy
    "Drama": "🎭",          # Эмодзи для жанра Drama
    "Horror": "👻",         # Эмодзи для жанра Horror
    "Music": "🎵",          # Эмодзи для жанра Music
    "Sci-Fi": "🚀",         # Эмодзи для жанра Sci-Fi
    "Fantasy": "🧙",        # Эмодзи для жанра Fantasy
    "Romance": "❤️",        # Эмодзи для жанра Romance
    "Thriller": "🔪",       # Эмодзи для жанра Thriller
    "Adventure": "🗺️",      # Эмодзи для жанра Adventure
    "Crime": "🕵️",          # Эмодзи для жанра Crime
    "Documentary": "🎬"     # Эмодзи для жанра Documentary

# 🎞️ Children
# 🎞️ Classics
# 🎞️ Family
# 🎞️ Foreign
# 🎞️ Games
}

# Функция отображает основное текстовое меню
def print_menu():
    print("\n🎬 === FilmFinder (Консольная версия) ===")  # Выводим заголовок
    print("1. 🔍 Поиск фильмов по ключевому слову")       # Пункт 1 — поиск по ключу
    print("2. 🎭 Поиск фильмов по жанру и году")          # Пункт 2 — поиск по фильтрам
    print("3. 📈 Показать популярные запросы")            # Пункт 3 — статистика
    print("4. ❌ Выйти")                                  # Пункт 4 — завершение работы

# Функция обработки поиска по ключевому слову
def handle_keyword_search():
    keyword = input("Введите ключевое слово: ").strip()  # Запрашиваем у пользователя слово
    if not keyword:                                      # Если пустой ввод — предупреждаем
        print("⚠️ Пустой ввод. Попробуйте снова.")
        return                                           # Выходим из функции
    log_query(keyword)                                  # Логируем запрос в память (влияет на статистику)
    results = search_by_keyword(keyword)                # Выполняем SQL-запрос с параметром (SQL-инъекция невозможна)
    print("\n🎞️ Найдено фильмов:")                       # Заголовок перед результатами
    if results:                                          # Если результаты найдены
        for title, description in results:              # Перебираем и выводим фильмы
            print(f"- {title}: {description}")
    else:
        print("⚠️ Нет результатов.")                     # Если ничего не найдено

# Функция визуального выбора жанра из списка
def select_genre(genres):
    # Генерируем список жанров с эмодзи для отображения в меню
    choices = [f"{GENRE_EMOJIS.get(g, '🎞️')} {g}" for g in genres]
    # Показываем выпадающий список и возвращаем выбор
    genre = questionary.select("🎭 Выберите жанр:", choices=choices).ask()
    # Удаляем эмодзи из строки и возвращаем чистое название жанра
    return genre.split(' ', 1)[1] if genre else None

# Функция визуального выбора года из списка
def select_year():
    years = [str(y) for y in range(2023, 1999, -1)]       # Создаём список годов от 2023 до 2000
    # Показываем выпадающий список лет с эмодзи
    year = questionary.select("📅 Выберите год выпуска:",
                              choices=[f"📽️ {y}" for y in years]).ask()
    # Возвращаем выбранный год без эмодзи
    return year.replace("📽️ ", "") if year else None

# Функция обработки поиска по жанру и году
def handle_genre_year_search():
    genres = get_all_genres()                             # Получаем список жанров из базы (внутри безопасный SQL-запрос)
    if not genres:                                        # Проверка наличия жанров
        print("⚠️ Не удалось получить список жанров.")
        return

    genre = select_genre(genres)                          # Пользователь выбирает жанр
    if not genre:                                         # Проверка отказа от выбора
        print("⚠️ Жанр не выбран.")
        return

    year = select_year()                                  # Пользователь выбирает год
    if not year:
        print("⚠️ Год не выбран.")                        # Проверка отказа от выбора
        return

    log_query(f"{genre} {year}")                          # Логируем запрос для статистики
    results = search_by_genre_and_year(genre, year)       # Выполняем безопасный параметризованный SQL-запрос
    print("\n🎞️ Найдено фильмов:")
    if results:                                           # Если есть фильмы — выводим их
        for title, description in results:
            print(f"- {title}: {description}")
    else:
        print("⚠️ Нет результатов.")                     # Если ничего не найдено

# Функция отображает наиболее частые поисковые запросы
def handle_show_popular_queries():
    print("\n📊 Топ популярных запросов:")                # Заголовок секции
    top_queries = get_top_queries()                       # Получаем данные логов (из памяти)
    if top_queries:                                       # Если есть данные — выводим
        for query, count in top_queries:
            print(f"{query} — {count} раз(а)")
    else:
        print("⚠️ Нет данных.")                          # Если запросов не было

# Главная функция, управляющая циклом работы приложения
def main():
    while True:                                           # Запускаем бесконечный цикл
        print_menu()                                      # Показываем главное меню
        choice = input("Выберите действие (1–4): ").strip()  # Получаем выбор от пользователя
        if choice == "1":
            handle_keyword_search()                       # Обработка опции 1
        elif choice == "2":
            handle_genre_year_search()                    # Обработка опции 2
        elif choice == "3":
            handle_show_popular_queries()                 # Обработка опции 3
        elif choice == "4":
            print("👋 Выход из приложения.")              # Прощаемся
            break                                         # Завершаем цикл
        else:
            print("⚠️ Неверный ввод. Попробуйте снова.")  # Ошибка ввода

# Запускаем только если скрипт вызывается напрямую
if __name__ == "__main__":
    main()


# 💡 Пояснение по безопасности:
# Все SQL-запросы, выполняемые в search_engine, используют параметризованные выражения.
# Это означает, что любые пользовательские данные передаются отдельно от SQL-кода:
# cursor.execute("SELECT * FROM films WHERE title LIKE %s", (f"%{keyword}%",))
# Благодаря этому невозможна SQL-инъекция (например, попытка завершить запрос через ' OR 1=1 --)