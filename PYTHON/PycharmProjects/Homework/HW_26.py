# 1. Напишите программу, которая принимает в качестве аргумента командной строки
# путь к файлу .py и запускает его.
# При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен".
# Если файл не существует или не может быть запущен,
# программа должна вывести соответствующее сообщение об ошибке.

# import sys
# import os.path
#
# def Test_script(script_path):
#     if os.path.isfile(script_path):
#         if script_path.endswith(".py"):
#             try:
#                 os.system(f'python {script_path}')
#                 print(f"Файл {script_path} успешно запущен.")
#             except Exception as error:
#                 print(f"Неизвестная ошибка: {error}")
#         else:
#             return print(f"Файл '{script_path}' не является Python-скриптом.")
#     else:
#         return print(f"Ошибка: Файл '{script_path}' не найден.")
#
# # Проверяем передачу аргументов командной строки
# if len(sys.argv) != 2:  # количество аргументов вводимых в командной строке
#     print(f"Введите правильно: python script_runner.py directory/name_file.py")
# else:
#     script_path = sys.argv[1]
#     Test_script(script_path)

# Option 2
# import sys
# import os
#
# def run_python_script(file_path: str) -> None:
#     """Запускает указанный Python-скрипт, обрабатывая возможные ошибки."""
#     if not os.path.isfile(file_path):
#         print(f"Ошибка: Файл '{file_path}' не найден.")
#         return
#
#     if not file_path.endswith(".py"):
#         print(f"Ошибка: Файл '{file_path}' не является Python-скриптом.")
#         return
#
#     try:
#         subprocess.run(["python", file_path], check=True)
#         print(f"Файл '{file_path}' успешно запущен.")
#     except subprocess.CalledProcessError:
#         print(f"Ошибка: Выполнение файла '{file_path}' завершилось с ошибкой.")
#     except Exception as e:
#         print(f"Неизвестная ошибка: {e}")
#
# # Проверяем, передан ли аргумент командной строки
# if len(sys.argv) != 2:
#     print("Использование: python run_script.py <путь_к_файлу.py>")
# else:
#     script_path = sys.argv[1]
#     run_python_script(script_path)

# Option 3
# import sys
# import os.path
#
# args = sys.argv
# print(args, "----------------")
# if os.path.exists(args[1]):
#     print(args[1], "exists")
#     if os.path.isfile(args[1]):
#         print(args[1], "is a file")
#         if args[1][-3:] == ".py":
#             os.system(f'python {args[1]}')
#             print(f'Файл {args[1]} успешно запущен')
#         else:
#             print('Файл не имеет расширения .py ')
#     else:
#             print('Это не файл ')
# else:
#     print(f'Файла {args[1]} не существует ')

# Option 4
# import argparse
# import runpy
#
# parser = argparse.ArgumentParser(description="Running Python-script")
# parser.add_argument("--run", help="Path to file .py", required=True)
# args = parser.parse_args()
#
# try:
#     runpy.run_path(args.run)
#     print(f'Файл {args.run} успешно запущен.')
# except FileNotFoundError:
#     print(f"Ошибка: Файл {args.run} не найден.")
# except Exception as e:
#     print(f'Ошибка при выполнении файла {e}')


# 2. Напишите программу, которая принимает в качестве аргумента командной строки
# путь к директории и выводит список всех файлов и поддиректорий внутри этой директории.
# Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.

# import sys
# import os
#
# def list_directory_contents(directory_path): # -> None:
#     """Выводит полный путь ко всем файлам
#     и поддиректориям внутри указанной директории."""
#     if not os.path.isdir(directory_path):
#         return print(f"Ошибка: Директория '{directory_path}' не найдена.")
#     print(f"Содержимое директории:\033[31m {directory_path}\033[0m\n")
#     for root, dirs, files in os.walk(directory_path):
#         for dir_name in dirs:
#             print(os.path.join(root, dir_name))  # Вывод поддиректорий
#         for file_name in files:
#             print(os.path.join(root, file_name))  # Вывод файлов
#
# # Проверяем передачу аргументов командной строки
# if len(sys.argv) != 2:  # количество аргументов вводимых в командной строке
#     print(f"Введите правильно: python list_directory.py directory")
# else:
#     directory = sys.argv[1]
#     list_directory_contents(directory)