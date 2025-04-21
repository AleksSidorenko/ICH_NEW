# config.py
# Модуль конфигурации для подключения к базе данных sakila

# Словарь с параметрами подключения к MySQL базе данных
# 'host' — адрес сервера базы данных
# 'user' — имя пользователя
# 'password' — пароль для подключения
# 'database' — имя базы данных
dbconfig = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',  # Хост MySQL сервера
    'user': 'ich1',                                                # Имя пользователя базы данных
    'password': 'password',                                        # Пароль пользователя
    'database': 'sakila'                                           # Название базы данных
}
