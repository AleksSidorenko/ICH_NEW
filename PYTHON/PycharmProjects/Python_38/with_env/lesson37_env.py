# pip install python-dotenv
import os
import dotenv
from pathlib import Path
import mysql.connector


dotenv.load_dotenv(Path('.env'))
dbconfig = {'host': os.environ.get('host'),
            'user': os.environ.get('user'),
            'password': os.environ.get('password'),
            'database': 'ich_edit'}

connection = mysql.connector.connect(**dbconfig)
cursor = connection.cursor()

cursor.execute(
'''
    show tables
''')

result = cursor.fetchall()
# print(result)

for num, table in enumerate(result, start=1):
    print(f"{num}: {table[0]}")

# table_num = int(input("Choose table num: "))
# cursor.execute(f'SELECT * FROM {result[table_num - 1][0]}')
# result = cursor.fetchall()
# print(*result, sep='\n')

cursor.close()
connection.close()

