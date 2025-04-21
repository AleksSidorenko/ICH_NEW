# pip install mysql-connector-python

import mysql.connector

# Подключение к базе данных
conn = mysql.connector.connect(
    host='ich-edit.edu.itcareerhub.de',  # Адрес сервера
    user='ich1',
    password='ich1_password_ilovedbs',
    database='111124_test'
)

# Создаем объект курсора для выполнения SQL-запросов
cursor = conn.cursor()
print("Подключение успешно!")
# print(conn.autocommit)

# cursor.execute("create schema IF NOT EXISTS 290724_test")
# cursor.execute("use 290724_test")

# Создаем таблицу "employees" (сотрудники)
create_table_query = '''
CREATE TABLE IF NOT EXISTS employees2 (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10, 2)
)
'''
cursor.execute(create_table_query)
print("Таблица 'employees' создана!")


# insert_query = '''
# INSERT INTO employees (first_name, last_name, hire_date, salary)
# VALUES (%(name)s, %(sur)s, %(hd)s, %(sal)s)
# '''
# data = {'name': 'Анна', 'sur': 'Кузнецова', 'hd': '2020-05-13', 'sal': 80000.00}


# cursor.execute(insert_query, data)
# # cursor.execute("INSERT INTO employees (first_name, last_name, hire_date, salary) VALUES (%s, %s, %s, %s)", ('Анна', 'Кузнецова', '2020-05-13', 80000.00))
# conn.commit()  # Сохраняем изменения

# Добавляем записи в таблицу "employees"
insert_query = '''
INSERT INTO employees2 (first_name, last_name, hire_date, salary)
VALUES (%s, %s, %s, %s)
'''
data = [
    ('Иван', 'Иванов', '2023-01-15', 50000.00),
    ('Анна', 'Смирнова', '2022-12-20', 60000.00),
    ('Петр', 'Кузнецов', '2021-06-30', 70000.00)
]

# Выполняем запрос с данными
cursor.executemany(insert_query, data)
conn.commit()  # Сохраняем изменения
print(f"{cursor.rowcount} записей добавлено в таблицу 'employees'.")


# Читаем все данные из таблицы "employees"
select_query = 'SELECT * FROM employees'
# select_query = 'SELECT department_id, count(*) FROM employees group by department_id'
cursor.execute(select_query)

# Выводим результаты
print("Список сотрудников:")
for row in cursor.fetchall():
    print(row)


# # Обновляем зарплату сотрудника с определенным ID
# update_query = '''
# UPDATE employees
# SET salary = %s
# WHERE employee_id = %s
# '''
# cursor.execute(update_query, (80000.00, 4))  # Повышаем зарплату сотруднику с ID 1
# conn.commit()
# print(f"Обновлено записей: {cursor.rowcount}")
#
#
# # Удаляем запись с определенным ID
# delete_query = 'DELETE FROM employees WHERE employee_id = %s'
# cursor.execute(delete_query, (11,))  # Удаляем сотрудника с ID 3
# conn.commit()
# print(f"Удалено записей: {cursor.rowcount}")
#
#
# # Закрываем курсор и соединение
# cursor.close()
# conn.close()
# print("Соединение закрыто.")


# # ---------------------------------------

# Контекстный менеджер
import mysql.connector

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
             'user': 'ich1',
             'password': 'password',
             'database': 'hr'}

with mysql.connector.connect(**dbconfig) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        print(cursor.fetchall())
        # cursor автоматически закрывается здесь
    # conn автоматически закрывается здесь





# import mysql.connector
# dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#             'user': 'ich1',
#             'password': 'password',
#             'database': 'ich_edit'}
#
# connection = mysql.connector.connect(**dbconfig)
# name = input("Enter name: ")
# cursor = connection.cursor()
# cursor.execute(
# f'''
# SELECT u.id, u.name, p.pid, p.prod, p.quantity
# FROM ich_edit.sales s
# inner join users as u
# on u.id = s.id
# and u.name = %s
# inner join ich_edit.product p
# on s.pid = p.pid
# ''', (name,)
# )
# result = cursor.fetchall()
# print(result)
cursor.close()
conn.close()
