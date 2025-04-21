# logger.py
# Псевдокод:
# - Проверяет наличие БД query_logs, если нет — создаёт её
# - Подключается к ней, создаёт таблицу search_logs, если нужно
# - Сохраняет поисковые запросы
# - Возвращает топ популярных запросов

import mysql.connector

log_config_without_db = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password'
}

log_config_with_db = {
    **log_config_without_db,
    'database': 'query_logs'
}

def ensure_database_exists():
    try:
        conn = mysql.connector.connect(**log_config_without_db)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS query_logs;")
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("Ошибка при создании базы query_logs:", err)

def ensure_table_exists():
    try:
        conn = mysql.connector.connect(**log_config_with_db)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS search_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                query_text VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("Ошибка при создании таблицы search_logs:", err)

def log_query(query: str):
    try:
        ensure_database_exists()
        ensure_table_exists()

        conn = mysql.connector.connect(**log_config_with_db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO search_logs (query_text) VALUES (%s);", (query,))
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("Ошибка логирования запроса:", err)

def get_top_queries(limit=10):
    try:
        ensure_database_exists()
        ensure_table_exists()

        conn = mysql.connector.connect(**log_config_with_db)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT query_text, COUNT(*) as count 
            FROM search_logs 
            GROUP BY query_text 
            ORDER BY count DESC 
            LIMIT %s;
        """, (limit,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except mysql.connector.Error as err:
        print("Ошибка получения популярных запросов:", err)
        return []
