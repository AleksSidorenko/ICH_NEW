"""
Практическое задание 1
Написать программу, которая запрашивает у пользователя возраст и выводит все строки
таблицы users, где возраст больше указанного.
"""
import mysql.connector

# dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
# 'user': 'ich1',
# 'password': 'password',
# 'database': 'social_media',
# }
# # Подключение к базе данных
# conn = mysql.connector.connect(**dbconfig)
#
# # Создаем объект курсора для выполнения SQL-запросов
# cursor = conn.cursor()
# print("Подключение успешно!")
#
#
# ratting = input("Enter: ")
#
# cursor.execute("Select rating From user where rating > %s", (ratting,))
# print(cursor.fetchall())
#
# cursor.close()
# conn.close()

"""
Практическое задание 2
В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod,
quantity) и Sales с полями (sid, id, pid).
Программа должна вывести все покупки каждого пользователя.
"""

# dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
# 'user': 'ich1',
# 'password': 'password',
# 'database': 'ich_edit'
# }
# conn = mysql.connector.connect(**dbconfig)
# cursor = conn.cursor()
#
# query = """
# SELECT * FROM users
# JOIN sales ON users.id = sales.id
# JOIN product ON product.pid = sales.pid
# """
# cursor.execute(query)
# for row in cursor.fetchall():
#     print(row)



cursor.close()
conn.close()