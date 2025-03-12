import sys
import os.path

def Test_script(script_path):
    if os.path.isfile(script_path):
        if script_path.endswith(".py"):
            try:
                os.system(f'python {script_path}')
                print(f"Файл {script_path} успешно запущен.")
            except Exception as error:
                print(f"Неизвестная ошибка: {error}")
        else:
            return print(f"Файл '{script_path}' не является Python-скриптом.")
    else:
        return print(f"Ошибка: Файл '{script_path}' не найден.")


if len(sys.argv) != 2:  # количество аргументов вводимых в командной строке
    print(f"Введите правильно: python script_runner.py directory/name_file.py")
else:
    script_path = sys.argv[1]
    Test_script(script_path)
