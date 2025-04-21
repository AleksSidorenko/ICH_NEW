"""
1. Вывести список таблиц в базе данных
2. Предоставить пользователю выбрать таблицу из предложенных:
3. Вывести список полей выбранной таблицы:
4. Позволить искать значение по определенному полю:
5. При вводе искомого значения добавить возможность выбора знака - найти записи в которых
выбранное поле больше меньше или равно введеному значению.
"""
"""

🧐-------------- Псевдокод ----------------------------
1. Подключиться к базе данных с помощью `mysql.connector`
   - Используем предоставленный словарь dbconfig
"""
# ----------------
# GPT 1
# ---------------

# import mysql.connector
#
# # Конфигурация подключения
# dbconfig = { 'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#              'user': 'ich1',
#              'password': 'password',
#              'database': 'ich_edit' }
#
# # Подключение
# conn = mysql.connector.connect(**dbconfig)
# cursor = conn.cursor()
#
# """
# 2. Получить список всех таблиц из базы данных
#    - Выполнить SQL-запрос: SHOW TABLES
#    - Сохранить список таблиц
# """
# # Получение списка таблиц
# cursor.execute("SHOW TABLES")
# tables = [table[0] for table in cursor.fetchall()]
#
# """
# 3. Вывести пользователю список таблиц и предложить выбрать одну из них
#    - Отобразить нумерованный список таблиц
#    - Прочитать выбор пользователя и получить имя выбранной таблицы
# """
# # Выбор таблицы
# print("Выберите таблицу:")
# for idx, table_name in enumerate(tables, 1):
#     print(f"{idx}. {table_name}")
# table_index = int(input("Введите номер таблицы: ")) - 1
# selected_table = tables[table_index]
#
# """
# 4. Получить список полей (столбцов) выбранной таблицы
#    - Выполнить SQL-запрос: DESCRIBE имя_таблицы
#    - Извлечь имена столбцов из результата
# """
# # Получение списка полей таблицы
# cursor.execute(f"DESCRIBE {selected_table}")
# fields = [row[0] for row in cursor.fetchall()]
#
# """
# 5. Показать пользователю список полей и предложить выбрать одно для поиска
#    - Отобразить нумерованный список полей
#    - Прочитать выбор пользователя и получить имя выбранного поля
# """
# # Выбор поля
# print(f"\nВы выбрали таблицу: {selected_table}")
# print("Выберите поле для поиска:")
# for idx, field in enumerate(fields, 1):
#     print(f"{idx}. {field}")
# field_index = int(input("Введите номер поля: ")) - 1
# selected_field = fields[field_index]
#
# """
# 6. Предложить пользователю ввести значение для поиска
#    - Запросить ввод значения (строка или число)
# """
# # Ввод значения и оператора сравнения
# value = input(f"Введите значение для поиска в поле '{selected_field}': ")
# """
# 7. Предложить выбрать оператор сравнения: '=', '<', '>'
#    - Показать варианты
#    - Прочитать выбор
# """
#
# print("Выберите оператор сравнения:")
# print("1. =\n2. <\n3. >")
# operator_choice = input("Введите номер оператора: ")
# operator_map = {'1': '=', '2': '<', '3': '>'}
# operator = operator_map.get(operator_choice, '=')
#
# """
# 8. Выполнить SQL-запрос к выбранной таблице, отфильтровав строки по выбранному полю, значению и оператору
#    - Пример: SELECT * FROM имя_таблицы WHERE поле оператор значение
# """
# # Подготовка и выполнение SQL-запроса
# query = f"SELECT * FROM {selected_table} WHERE {selected_field} {operator} %s"
# try:
#     cursor.execute(query, (value,))
#     results = cursor.fetchall()
#
#     """
#     9. Вывести найденные строки (если есть)
#        - Если строк нет — вывести сообщение об этом
#     """
#
#     if results:
#         print("\nНайденные записи:")
#         for row in results:
#             print(row)
#     else:
#         print("\nНет записей, соответствующих запросу.")
# except Exception as e:
#     print("Ошибка при выполнении запроса:", e)
#
#
# --------------------
# GPT 2
# ---------------------

# import mysql.connector
# from mysql.connector import Error
# from tabulate import tabulate
#
# def connect_to_database(config):
#     try:
#         conn = mysql.connector.connect(**config)
#         if conn.is_connected():
#             print("✅ Успешное подключение к базе данных.")
#             return conn
#     except Error as e:
#         print("❌ Ошибка подключения к базе данных:", e)
#     return None
#
# def get_tables(cursor):
#     cursor.execute("SHOW TABLES")
#     return [table[0] for table in cursor.fetchall()]
#
# def get_fields(cursor, table_name):
#     cursor.execute(f"DESCRIBE {table_name}")
#     return cursor.fetchall()
#
# def safe_choice(options, prompt):
#     while True:
#         try:
#             choice = int(input(prompt))
#             if 1 <= choice <= len(options):
#                 return choice - 1
#             else:
#                 print("🚫 Неверный номер. Пожалуйста, выберите из предложенного списка.")
#         except ValueError:
#             print("🚫 Введите целое число.")
#
# def parse_input_value(field_type):
#     is_numeric = any(x in field_type.lower() for x in ['int', 'float', 'double', 'decimal'])
#     is_date = 'date' in field_type.lower() or 'time' in field_type.lower()
#     is_string = any(x in field_type.lower() for x in ['char', 'text'])
#
#     if is_numeric:
#         input_hint = "Введите числовое значение (например: 123 или 45.67): "
#     elif is_date:
#         input_hint = "Введите дату/время в формате 'YYYY-MM-DD' или 'YYYY-MM-DD HH:MM:SS': "
#     elif is_string:
#         input_hint = "Введите текстовое значение (например: hello): "
#     else:
#         input_hint = "Введите значение: "
#
#     while True:
#         value = input(input_hint)
#         try:
#             if is_numeric:
#                 float(value)
#             return value
#         except ValueError:
#             print("🚫 Неверный формат. Попробуйте снова.")
#
# def choose_operator_for_type(field_type):
#     is_numeric_or_date = any(x in field_type.lower() for x in ['int', 'float', 'double', 'decimal', 'date', 'time'])
#     is_string = any(x in field_type.lower() for x in ['char', 'text'])
#
#     operator_map = {'1': '='}
#     if is_numeric_or_date:
#         operator_map.update({'2': '<', '3': '>'})
#
#     print("\nВыберите оператор сравнения:")
#     for key, op in operator_map.items():
#         description = {'=': 'равно', '<': 'меньше', '>': 'больше'}[op]
#         print(f"{key}. {op} ({description})")
#
#     while True:
#         choice = input("Введите номер оператора: ")
#         if choice in operator_map:
#             return operator_map[choice]
#         else:
#             print("🚫 Неверный выбор. Пожалуйста, выберите корректный номер оператора.")
#
# # Конфигурация подключения
# dbconfig = {
#     'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'ich_edit'
# }
#
# # Подключение к базе
# conn = connect_to_database(dbconfig)
# if not conn:
#     exit()
#
# cursor = conn.cursor()
#
# # Получение таблиц
# tables = get_tables(cursor)
# if not tables:
#     print("❌ Таблицы не найдены.")
#     exit()
#
# print("\n📄 Список таблиц:")
# for idx, table_name in enumerate(tables, 1):
#     print(f"{idx}. {table_name}")
#
# table_index = safe_choice(tables, "Выберите номер таблицы: ")
# selected_table = tables[table_index]
#
# # Получение полей
# field_info = get_fields(cursor, selected_table)
# fields = [row[0] for row in field_info]
# field_types = {row[0]: row[1] for row in field_info}
#
# print(f"\n📂 Таблица: {selected_table}")
# print("📌 Список полей:")
# for idx, field in enumerate(fields, 1):
#     print(f"{idx}. {field} ({field_types[field]})")
#
# field_index = safe_choice(fields, "Выберите номер поля для фильтрации: ")
# selected_field = fields[field_index]
# field_type = field_types[selected_field]
#
# # Ввод значения и выбор оператора
# print(f"\n🔍 Выбранное поле: {selected_field} (тип: {field_type})")
# value = parse_input_value(field_type)
# operator = choose_operator_for_type(field_type)
#
# # Выполнение запроса
# query = f"SELECT * FROM {selected_table} WHERE {selected_field} {operator} %s"
# try:
#     cursor.execute(query, (value,))
#     results = cursor.fetchall()
#     # Заголовки полей
#     column_names = [desc[0] for desc in cursor.description]
#     print(f"\n🔎 Результаты поиска в таблице '{selected_table}' по условию: {selected_field} {operator} {value}\n")
#     if results:
#         print(tabulate(results, headers=column_names, tablefmt="fancy_grid", stralign="center", numalign="center"))
#     else:
#         print("🚫 Записи не найдены.")
# except Error as e:
#     print("❌ Ошибка при выполнении запроса:", e)
#
# # Закрытие соединения
# cursor.close()
# conn.close()



# --------------------
# GPT 3 - окончательный скрипт
# ---------------------

# import mysql.connector
# from mysql.connector import Error
# from tabulate import tabulate
#
# # ===============================================================
# # 1. Подключение к базе данных с обработкой ошибок
# # ===============================================================
# def connect_to_database(config):
#     try:
#         conn = mysql.connector.connect(**config)
#         if conn.is_connected():
#             print("✅ Подключение к базе данных успешно.")
#             return conn
#     except Error as e:
#         print("❌ Ошибка подключения:", e)
#     return None
#
# # ===============================================================
# # 2. Получение списка таблиц из базы данных
# # ===============================================================
# def get_tables(cursor):
#     cursor.execute("SHOW TABLES")
#     return [table[0] for table in cursor.fetchall()]
#
# # ===============================================================
# # 3. Получение списка полей выбранной таблицы
# # ===============================================================
# def get_fields(cursor, table_name):
#     cursor.execute(f"DESCRIBE {table_name}")
#     return cursor.fetchall()
#
# # ===============================================================
# # 4. Безопасный выбор из списка по индексу
# # ===============================================================
# def safe_choice(options, prompt):
#     while True:
#         try:
#             choice = int(input(prompt))
#             if 1 <= choice <= len(options):
#                 return choice - 1
#             else:
#                 print("🚫 Неверный номер. Пожалуйста, выберите из списка.")
#         except ValueError:
#             print("🚫 Введите целое число.")
#
# # ===============================================================
# # 5. Подсказка по типу данных + проверка значения пользователя
# # ===============================================================
# def parse_input_value(field_type):
#     is_numeric = any(x in field_type.lower() for x in ['int', 'float', 'double', 'decimal'])
#     is_date = 'date' in field_type.lower() or 'time' in field_type.lower()
#     is_string = any(x in field_type.lower() for x in ['char', 'text'])
#
#     if is_numeric:
#         input_hint = "Введите числовое значение (например: 123 или 45.67): "
#     elif is_date:
#         input_hint = "Введите дату/время в формате 'YYYY-MM-DD' или 'YYYY-MM-DD HH:MM:SS': "
#     elif is_string:
#         input_hint = "Введите текстовое значение (например: hello): "
#     else:
#         input_hint = "Введите значение: "
#
#     while True:
#         value = input(input_hint)
#         try:
#             if is_numeric:
#                 float(value)
#             return value
#         except ValueError:
#             print("🚫 Неверный формат. Попробуйте снова.")
#
# # ===============================================================
# # 6. Выбор оператора сравнения с проверкой
# # ===============================================================
# def choose_operator_for_type(field_type):
#     is_numeric_or_date = any(x in field_type.lower() for x in ['int', 'float', 'double', 'decimal', 'date', 'time'])
#     operator_map = {'1': '='}
#     if is_numeric_or_date:
#         operator_map.update({'2': '<', '3': '>'})
#
#     print("\nВыберите оператор сравнения:")
#     for key, op in operator_map.items():
#         desc = {'=': 'равно', '<': 'меньше', '>': 'больше'}[op]
#         print(f"{key}. {op} ({desc})")
#
#     while True:
#         choice = input("Введите номер оператора: ")
#         if choice in operator_map:
#             return operator_map[choice]
#         else:
#             print("🚫 Неверный выбор. Повторите ввод.")
#
# # ===============================================================
# # 7. Выбор таблицы пользователем и проверка на пустоту таблицы
# # ===============================================================
# def choose_non_empty_table(cursor, tables, conn):
#     while True:
#         print("\n📄 Список таблиц:")
#         for idx, tbl in enumerate(tables, 1):
#             print(f"{idx}. {tbl}")
#
#         table_index = safe_choice(tables, "Выберите номер таблицы: ")
#         selected_table = tables[table_index]
#
#         # Проверка, пуста ли таблица
#         try:
#             cursor.execute(f"SELECT COUNT(*) FROM {selected_table}")
#             row_count = cursor.fetchone()[0]
#         except Error as e:
#             print(f"❌ Ошибка при проверке таблицы '{selected_table}':", e)
#             continue
#
#         if row_count == 0:
#             print(f"\n📭 Таблица '{selected_table}' пуста — нет ни одной записи.")
#             retry = input("🔁 Хотите выбрать другую таблицу? (y/n): ").lower()
#             if retry != 'y':
#                 print("🔚 Завершение работы.")
#                 cursor.close()
#                 conn.close()
#                 exit()
#         else:
#             return selected_table
#
# # ===============================================================
# # 8. Основная логика программы
# # ===============================================================
#
# # Параметры подключения
# dbconfig = {
#     'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'ich_edit'
# }
#
# # Подключение с возможностью ручного ввода параметров
# while True:
#     conn = connect_to_database(dbconfig)
#     # if not conn:
#     #     retry = input("🔁 Попробовать ввести параметры вручную? (y/n): ").lower()
#     #     if retry == 'y':
#     #         dbconfig['host'] = input("Хост (например: localhost): ")
#     #         dbconfig['user'] = input("Пользователь: ")
#     #         dbconfig['password'] = input("Пароль: ")
#     #         dbconfig['database'] = input("Имя базы данных: ")
#     #         continue
#     #     else:
#     #         print("🔚 Завершение работы.")
#     #         exit()
#
#     cursor = conn.cursor()
#     tables = get_tables(cursor)
#     if not tables:
#         print("\n📭 Таблицы в базе данных отсутствуют.")
#         cursor.close()
#         conn.close()
#         exit()
#     break  # подключение успешно и таблицы найдены
#
# # Выбор таблицы с проверкой на пустоту
# selected_table = choose_non_empty_table(cursor, tables, conn)
#
# # Получение полей выбранной таблицы
# field_info = get_fields(cursor, selected_table)
# fields = [row[0] for row in field_info]
# field_types = {row[0]: row[1] for row in field_info}
#
# print(f"\n📂 Таблица: {selected_table}")
# print("📌 Доступные поля:")
# for idx, field in enumerate(fields, 1):
#     print(f"{idx}. {field} ({field_types[field]})")
#
# # Пользователь выбирает поле и вводит значение
# field_index = safe_choice(fields, "Выберите номер поля: ")
# selected_field = fields[field_index]
# field_type = field_types[selected_field]
#
# print(f"\n🔍 Поле: {selected_field} (тип: {field_type})")
# value = parse_input_value(field_type)
# operator = choose_operator_for_type(field_type)
#
# # Выполнение SQL-запроса с поиском по условию
# query = f"SELECT * FROM {selected_table} WHERE {selected_field} {operator} %s"
# try:
#     cursor.execute(query, (value,))
#     results = cursor.fetchall()
#     column_names = [desc[0] for desc in cursor.description]
#
#     print(f"\n🔎 Результаты поиска в таблице '{selected_table}' по условию: {selected_field} {operator} {value}\n")
#     if results:
#         print(tabulate(results, headers=column_names, tablefmt="fancy_grid", stralign="center", numalign="center"))
#     else:
#         print("🚫 Записи не найдены.")
# except Error as e:
#     print("❌ Ошибка при выполнении запроса:", e)
#
# # Завершение
# cursor.close()
# conn.close()
