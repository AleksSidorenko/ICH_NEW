### **Задача: Анализ продаж по категориям и датам**

# Напишите программу, которая обрабатывает текстовый файл с данными о продажах.
# Программа должна:
# 1. **Считать данные из текстового файла**, в котором каждая строка содержит информацию в следующем формате:
#    ```
#    имя,дата,сумма,категория,город
#    ```
#    Пример входных данных:
#    ```
#    Olivia Suarez,2024-08-02,4565,Electronics,Dallas
#    Jennifer Jacobs,2023-08-19,4963,Automotive,London
#    Erin Johnson,2024-08-29,1796,Clothing,Miami
#    ```
# 2. **Сгруппировать данные по годам и месяцам**, создавая для каждого года и месяца отдельную папку в указанной директории.
# 3. **Создать файлы для каждой категории товаров**, в которых должны быть указаны все продажи по данной категории в формате:
#    ```
#    дата,имя продавца,сумма
#    ```
#    Пример файла `Electronics.txt`:
#    ```
#    2025-02-01,Cynthia Maddox,538
#    2025-02-01,Kendra Martinez,3799
#    2025-02-02,Rachel Miller,1097
#    ```
#    - Все записи в файле **должны быть отсортированы по дате**.
# 4. **Создать общий отчёт по каждому месяцу** (`monthly_report.txt`), в котором указана суммарная выручка по каждой категории и общая сумма:
#    ```
#    Automotive,109539
#    Books,133160
#    Clothing,102001
#    Electronics,79403
#    Groceries,104387
#    Home Appliances,99911
#    Sports,78782
#    Full,707183
#    ```
# 5. **Программа должна принимать аргументы командной строки**:
#    ```sh
#    python sales_report.py <input_file> <output_directory>
#    ```
#    Где:
#    - `<input_file>` — путь к входному файлу с продажами.
#    - `<output_directory>` — папка, куда будут сохранены отчёты.

# Псевдокод
# 1 список словарей
# 2 словарь{критерий: список подходящих словарей}
# 3 создать папки
# 4 рассчитать сумму по группе и записать в файл


# запуск скрипта с обязательными флагами из консоли:
# python "путь к script" -f "путь к базовому файлу" -od "путь к файлу с анализом"
# script = r''
# _f = r''
# _od = r''


import argparse
import os
from datetime import datetime
from collections import defaultdict


parser = argparse.ArgumentParser()
parser.add_argument("--input_file", "-f", type=str, help="path to file", required=True)
parser.add_argument("--output_directory", "-od", type=str, help="path to output directory with report", required=True)

args = parser.parse_args()

if not os.path.exists(args.output_directory):
    os.makedirs(args.output_directory)

def create_dict_from_file(input_file):
    records = []
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                seller, date, amount, product, city = line.strip().split(',')
                record = {
                    'seller': seller,
                    'date': date,
                    'amount': amount,
                    'product': product,
                    'city': city,
                }
                records.append(record)
    except FileNotFoundError as e:
        print(e)

    return records


def group_by_year_month(records):
    grouped = defaultdict(list)
    for record in records:
        date_obj = datetime.strptime(record['date'], '%Y-%m-%d')
        year_month = date_obj.strftime('%Y-%m')  # Year, month

        # if year_month not in grouped:
        #    grouped[year_month] = []
        grouped[year_month].append(record)

    return grouped


def save_grouped_data(grouped, output_directory):
    for year_month, records in grouped.items():
        year, month = year_month.split('-')
        # Create map
        dir_path = os.path.join(output_directory, year, month)
        os.makedirs(dir_path, exist_ok=True)

        # Write in file
        file_path = os.path.join(dir_path, f"{year}_{month}_sales.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            for record in records:
                file.write(
                    f"{record['seller']},{record['date']},{record['amount']},{record['product']},{record['city']}\n")



records = create_dict_from_file(args.input_file)
# print(records)# Создаем словарь из файла
grouped = group_by_year_month(records)
for i in grouped.items():
    print(i)
    # Группируем по годам и месяцам
save_grouped_data(grouped, args.output_directory)  # Сохраняем сгруппированные файлы





