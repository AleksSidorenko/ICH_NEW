
# logger.py

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
        sql = """
            SELECT query_text, COUNT(*) AS count
            FROM query_log
            GROUP BY query_text
            ORDER BY count DESC
            LIMIT %s
        """
        self.cursor.execute(sql, (limit,))
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
