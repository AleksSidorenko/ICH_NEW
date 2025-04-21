# logger.py
# Модуль логирования поисковых запросов (в памяти, без базы данных)

from collections import Counter  # Импортируем Counter для подсчёта количества одинаковых запросов

# Глобальная переменная — словарь для хранения количества каждого поискового запроса
query_log_memory = Counter()

# Функция логирования поискового запроса
def log_query(query: str):
    # Приводим запрос к нижнему регистру и удаляем пробелы в начале и конце
    normalized_query = query.strip().lower()
    # Увеличиваем счётчик для этого запроса
    query_log_memory[normalized_query] += 1

# Функция получения самых популярных запросов
def get_top_queries(limit=10):
    # Возвращает limit самых частых запросов в виде списка кортежей (запрос, количество)
    return query_log_memory.most_common(limit)
