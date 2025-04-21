# logger.py
"""
Псевдокод:
- Используется внутренний словарь (Counter) как временная таблица
- Метод log_query имитирует "сохранение" запроса
- Метод get_top_queries возвращает "самые частые" запросы
- Никакая база данных не используется
"""

from collections import Counter

# Временное хранилище запросов в виде словаря (эмуляция таблицы search_logs)
query_log_memory = Counter()

def log_query(query: str):
    """
    Эмуляция сохранения поискового запроса в виртуальную таблицу.
    Запрос приводится к нижнему регистру и учитываются повторы.
    """
    normalized_query = query.strip().lower()
    query_log_memory[normalized_query] += 1
    # Логически это равносильно: INSERT INTO search_logs (query_text) VALUES (normalized_query);

def get_top_queries(limit=10):
    """
    Возвращает список самых популярных запросов.
    Аналог: SELECT query_text, COUNT(*) FROM search_logs GROUP BY query_text ORDER BY COUNT(*) DESC;
    """
    return query_log_memory.most_common(limit)