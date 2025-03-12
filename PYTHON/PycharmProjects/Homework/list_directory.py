import sys
import os

def list_directory_contents(directory_path): # -> None:
    """Выводит полный путь ко всем файлам
    и поддиректориям внутри указанной директории."""
    if not os.path.isdir(directory_path):
        return print(f"Ошибка: Директория '{directory_path}' не найдена.")
    print(f"Содержимое директории:\033[31m {directory_path}\033[0m\n")
    for root, dirs, files in os.walk(directory_path):
        for dir_name in dirs:
            print(os.path.join(root, dir_name))  # Вывод поддиректорий
        for file_name in files:
            print(os.path.join(root, file_name))  # Вывод файлов

# Проверяем, передан ли аргумент командной строки
if len(sys.argv) != 2:  # количество аргументов вводимых в командной строке
    print(f"Введите правильно: python list_directory.py directory")
else:
    directory = sys.argv[1]
    list_directory_contents(directory)