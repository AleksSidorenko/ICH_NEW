# pip install mysql-connector-python

import mysql.connector

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
             'user': 'ich1',
             'password': 'password',
             'database': 'hr',
             # 'port': 3306
            }
conn = mysql.connector.connect(**dbconfig)
# conn = mysql.connector.connect(
#     host='ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#     user='ich1',
#     password='password',
#     database='hr'
# )

# # Подключение к базе данных
# conn = mysql.connector.connect(
#     host='ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',  # Адрес сервера
#     user='ich1',
#     password='password',
#     database='hr'
# )

# # Подключение к базе данных
# conn = mysql.connector.connect(
#     host='mysql.itcareerhub.de',  # Адрес сервера
#     user='ich1',
#     password='ich1_password_ilovedbs',
#     database='290724_test'
# )

# Создание курсора
cursor = conn.cursor()

# query = "SELECT * FROM employees"
# Пример запроса
# cursor.execute(query)
# emp = cursor.fetchall()
# cursor.execute("SELECT * FROM employees")
# cursor.execute("SELECT * FROM employees where employee_id = 103")
# cursor.execute("SELECT * FROM employees where employee_id = %s", (103,))

# query_emp = "SELECT * FROM employees where employee_id = %s or last_name = %s"
# person = (103, "King")
# cursor.execute(query_emp, person)
# person = (104, "Hunold")
# cursor.execute(query_emp, person)
# cursor.execute("SELECT * FROM employees where employee_id = %(id)s", {'id': 103})
cursor.execute("SELECT * FROM employees where employee_id = %(id)s or last_name = %(ln)s", {"ln": "King", 'id': 103})

# print(type(cursor))
# emp = cursor.fetchone()
# emp = cursor.fetchall()
# print(emp)
print("-----------------------")
emps = cursor.fetchmany(3)
print(emps)
for emp in emps:
    print(emp)
print("-----------------------")
cursor.reset()

cursor.execute("DESCRIBE employees")
table_info = cursor.fetchall()
print(table_info)
table_names = [el[0] for el in table_info]
print(table_names)
table_names_iter = map(lambda l: l[0], table_info)
print(list(table_names_iter))
pars = zip(table_names, emp)
# print(list(pars))
d = dict(pars)
print(d)
# print(*emp, sep='\n')
# emp = cursor.fetchall()
# print()

#
# # print(emp[0:2])
#
# # for table in cursor.fetchall():
# #     print(table)
#
# cursor.execute('SHOW TABLES')
# # for i in cursor.fetchall():
# #     print(i[0])
#
# for i, *_ in cursor.fetchall():
#     print(i)
# tab = input("Choose table: ")
#
# cursor.execute(f"describe {tab}")
# res = cursor.fetchall()
# for el in res:
#     print(el)
#
# cursor.execute(f"SELECT * FROM {tab}")
# res = cursor.fetchall()
#
# for el in res:
#     print(el[1])

# Закрытие курсора
cursor.close()
# Закрытие соединения
conn.close()
