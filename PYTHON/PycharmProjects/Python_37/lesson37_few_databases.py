import mysql.connector

# # 1. Работа с несколькими базами данных в одном подключении
#
# # Подключение к серверу MySQL
# conn = mysql.connector.connect(
#     host='ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',  # Адрес сервера
#     user='ich1',
#     password='password'
# )
#
# cursor = conn.cursor()
#
# # Выбор базы данных по умолчанию
# cursor.execute('USE hr')
#
# # Запрос к таблице из database1
# cursor.execute('SELECT * FROM hr.employees')
# print(cursor.fetchall())
#
# # Запрос к таблице из database2
# cursor.execute('SELECT * FROM world.countries')
# print(cursor.fetchall())
#
# conn.close()


# # ------------------------------------------------------------------------------------

# # 2. Создание отдельных подключений для разных баз данных
#
# import mysql.connector
#
# # Подключение к первой базе данных
# conn1 = mysql.connector.connect(
#     host='ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',  # Адрес сервера
#     user='ich1',
#     password='password',
#     database='hr'
# )
#
# # # Подключение ко второй базе данных
# conn2 = mysql.connector.connect(
#     host='mysql.itcareerhub.de',  # Адрес сервера
#     user='ich1',
#     password='ich1_password_ilovedbs',
#     database='hr',
# )
#
# # Работа с первой базой данных
# cursor1 = conn1.cursor()
# cursor1.execute('SELECT * FROM employees')
# print('Data from database1:', cursor1.fetchall())
#
# # Работа со второй базой данных
# cursor2 = conn2.cursor()
# cursor2.execute('SELECT * FROM employees')
# print('Data from database2:', cursor2.fetchall())
#
# # Закрытие соединений
# conn1.close()
# conn2.close()


# # ------------------------------------------------------------------------------------

# 3. Использование объединений в MySQL

import mysql.connector

conn = mysql.connector.connect(
    host='ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',  # Адрес сервера
    user='ich1',
    password='password'
)

cursor = conn.cursor()

# Объединение данных из двух баз данных
query = '''
SELECT employee_id FROM hr.employees
UNION
SELECT Code FROM world.country
'''

cursor.execute(query)
print(cursor.fetchall())

conn.close()


