# pip install mysql-connector-python

import mysql.connector

# Подключение к базе данных
conn = mysql.connector.connect(
    host='ich-edit.edu.itcareerhub.de',  # Адрес сервера
    user='ich1',
    password='ich1_password_ilovedbs',
    # database='111124_test'
)

# Создаем объект курсора для выполнения SQL-запросов
cursor = conn.cursor()
print("Подключение успешно!")
cursor.execute("CREATE SCHEMA IF NOT EXISTS 111124_test")
print("База данных '111124_test' проверена или создана.")
cursor.execute("USE 111124_test")


# 1. Создаем таблицу, если ее нет
create_table_query = '''
CREATE TABLE IF NOT EXISTS accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,  -- Уникальный ID счета
    owner_name VARCHAR(100),                    -- Имя владельца счета
    balance DECIMAL(10, 2)                      -- Баланс счета
)
'''
cursor.execute(create_table_query)
print("Таблица 'accounts' проверена или создана.")


# 2. Проверяем, есть ли данные в таблице, и добавляем начальные данные, если она пуста
cursor.execute('SELECT COUNT(*) FROM accounts')

# print(cursor.fetchone())
if cursor.fetchone()[0] == 0:
    # Вставляем начальные данные
    insert_accounts_query = '''
    INSERT INTO accounts (owner_name, balance)
    VALUES (%s, %s)
    '''
    initial_data = [
        ('Bob Brown', 10000.00),
        ('Ann Black', 15000.00)
    ]
    cursor.executemany(insert_accounts_query, initial_data)
    conn.commit()
    print("Начальные данные добавлены!")

# Проверяем текущие балансы
cursor.execute('SELECT * FROM accounts')
print("Текущие данные в таблице 'accounts':")
for row in cursor.fetchall():
    print(row)

# 3. Функция перевода средств
def transfer_funds(sender_id, receiver_id, amount):
    try:
        # Получаем баланс отправителя
        cursor.execute('SELECT balance FROM accounts WHERE account_id = %s', (sender_id, ))
        result = cursor.fetchone()
        if not result:
            raise ValueError(f"Счет отправителя с ID {sender_id} не найден.")
        sender_balance = result[0]

        if sender_balance < amount:
            raise ValueError("Недостаточно средств на счете отправителя!")

        # Снимаем деньги с баланса отправителя
        cursor.execute('UPDATE accounts SET balance = balance - %s WHERE account_id = %s', (amount, sender_id))


        # Получаем получателя
        cursor.execute('SELECT * FROM accounts WHERE account_id = %s', (receiver_id,))
        result = cursor.fetchone()
        if not result:
            raise ValueError(f"Счет получателя с ID {receiver_id} не найден.")

        # Добавляем деньги на баланс получателя
        cursor.execute('UPDATE accounts SET balance = balance + %s WHERE account_id = %s', (amount, receiver_id))

        # Подтверждаем транзакцию
        conn.commit()
        print(f"Успешный перевод {amount} от счета {sender_id} к счету {receiver_id}!")

    except Exception as e:
        # Откатываем транзакцию в случае ошибки
        conn.rollback()
        print(f"Ошибка транзакции: {e}")


# # 4. Пример перевода
transfer_funds(1, 2, 5000)

# 5. Проверяем текущие балансы
cursor.execute('SELECT * FROM accounts')
print("Текущие данные в таблице 'accounts':")
for row in cursor.fetchall():
    print(row)

# Закрываем соединение
cursor.close()
conn.close()


