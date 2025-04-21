"""
В базе данных ich_edit три таблицы. Users с полями (id, name, age),
Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
Программа должна запросить у пользователя название таблицы и вывести все ее строки или сообщение,
что такой таблицы нет.
"""
# ---------------
# разное:
# ----------------
# query_table = """SELECT * FROM {}"""
#
# # query_col = """SELECT {} FROM {}""" - запрос у пользователя на ввод поля или полей
#
#
# if num_table in valid_tables.keys():
#     cursor.execute(query_table.format(valid_tables[num_table]))
#     column_names = [desc[0] for desc in cursor.description]
#     # Заголовки
#     for row in column_names:
#         print(f"{str(row):^8}", end="")
#     print()
#     print("-" * 70)
#     # for prod, qty, price in purchases:
#     #     print(f"{prod:<20} {qty:^12} {price:>12.2f}")
#     # i = 0
#     for row in cursor.fetchall():
#         # print(dict(zip(column_names, row)))
#         # print(tabulate(rows, headers=column_names, tablefmt="grid"))
#         for item in row:
#             print(f"{item:^8}", end="")
#         print()
#         # print(f'{str(row[i]):^8}', end="")
#         # i += 1
# else:
#     print(f"Таблицы {num_table} нет.")
#
# cursor.close()
# conn.close()


# """
# -------------------------- окончательный вариант
# import mysql.connector
#
# # Настройки подключения
# dbconfig = {
#     'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'ich_edit'
# }
#
# # Словарь допустимых таблиц
# valid_tables = {
#     1: 'users',
#     2: 'product',
#     3: 'sales'
# }
#
# try:
#     # Запрос у пользователя
#     num_table = int(input("Введите номер таблицы (1. users, 2. product, 3. sales): "))
#
#     if num_table in valid_tables:
#         table_name = valid_tables[num_table]
#         query_table = f"SELECT * FROM {table_name}"
#
#         # Подключение и выполнение запроса
#         conn = mysql.connector.connect(**dbconfig)
#         cursor = conn.cursor()
#         cursor.execute(query_table)
#
#         # Получение и печать заголовков
#         column_names = [desc[0] for desc in cursor.description]
#         print("\n" + " | ".join(f"{col:^15}" for col in column_names))
#         print("-" * (len(column_names) * 18))
#
#         # Печать строк
#         for row in cursor.fetchall():
#             print(" | ".join(f"{str(item):^15}" for item in row))
#
#         cursor.close()
#         conn.close()
#     else:
#         print("Таблицы с таким номером нет.")
#
# except ValueError:
#     print("Ошибка: Введите целое число от 1 до 3.")
# except mysql.connector.Error as err:
#     print(f"Ошибка подключения к базе данных: {err}")


# --------------------------
# """


####### GPT
"""
import mysql.connector
from tabulate import tabulate

# Настройки подключения
dbconfig = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password',
    'database': 'ich_edit'
}

# Доступные таблицы
valid_tables = {
    1: 'users',
    2: 'product',
    3: 'sales'
}

def main():
    print("Выберите таблицу для просмотра:")
    for key, val in valid_tables.items():
        print(f"{key}. {val}")

    try:
        choice = int(input("\nВведите номер таблицы (1-3): "))
        if choice not in valid_tables:
            print("❌ Таблицы с таким номером нет.")
            return

        table_name = valid_tables[choice]
        query = f"SELECT * FROM {table_name}"

        # Подключение и выполнение запроса
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query)

        # Получение результатов
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]

        # Красивый вывод таблицы
        print(f"\n📄 Данные из таблицы {table_name}:\n")
        if rows:
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        else:
            print("Таблица пуста.")

        cursor.close()
        conn.close()

    except ValueError:
        print("⚠️ Пожалуйста, введите число от 1 до 3.")
    except mysql.connector.Error as err:
        print(f"🚫 Ошибка подключения к базе данных: {err}")
    except Exception as e:
        print(f"❗ Произошла неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
"""


### -----------------------------
"""
В базе данных ich_edit три таблицы. 
Users с полями (id, name, age), Products с полями (pid, prod, quantity) 
и Sales с полями (sid, id, pid).
Программа должна вывести все имена из таблицы users, 
дать пользователю выбрать одно из них и вывести все покупки этого пользователя.
"""
### -----------------------------

# import mysql.connector
#
# # Подключение к базе
# dbconfig = {
#     'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'ich_edit'
# }
#
# # Устанавливаем соединение
# try:
#     conn = mysql.connector.connect(**dbconfig)
#     cursor = conn.cursor()
# except mysql.connector.Error as err:
#     print(f"Ошибка подключения: {err}")
#     exit(1)
#
# cursor.execute("SELECT id, name FROM users")
# users = cursor.fetchall()
#
# if not users:
#     print("В базе данных нет пользователей.")
# else:
#     print("\nСписок пользователей:")
#     for i, (uid, name) in enumerate(users, start=1):
#         print(f"{i}. {name}")
#
#     selected_index = input("\nВведите номер пользователя, чтобы увидеть его покупки: ")
#
#     if not selected_index.isdigit() or not (1 <= int(selected_index) <= len(users)):
#         print("Некорректный выбор.")
#     else:
#         selected_id, selected_name = users[int(selected_index) - 1]
#
#         # Запрос покупок пользователя
#         query = """
#         SELECT p.prod, p.quantity
#         FROM sales s
#         JOIN product p ON s.pid = p.pid
#         WHERE s.id = %s
#         """
#         cursor.execute(query, (selected_id,))
#         purchases = cursor.fetchall()
#
#         print(f"\nПокупки пользователя {selected_name}:")
#         if purchases:
#             print(f"{'Товар':<20} {'Количество'}")
#             print("-" * 30)
#             for prod, qty in purchases:
#                 print(f"{prod:<20} {qty}")
#         else:
#             print("Нет покупок.")
#
# cursor.close()
# conn.close()
