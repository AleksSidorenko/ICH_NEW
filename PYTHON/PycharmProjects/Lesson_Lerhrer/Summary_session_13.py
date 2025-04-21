# for dirpath, dirnames, filenames in os.walk("."):
#     for filename in filenames:
#         print(os.path.join(dirpath, "new", filename))
#     for dirname in dirnames:
#         print(os.path.join(dirpath, "new", dirname))
#
# print()

# import os
# path = os.path.join('/path/to', 'file.txt')
# print(path)
# absolute_path_correct = os.path.abspath(os.getcwd())
# print(absolute_path_correct)
# absolute_path = os.path.abspath(path)
# print(absolute_path)
# exists = os.path.exists(absolute_path_correct)
# print(exists)
# exists = os.path.exists(absolute_path)
# print(exists)
# is_directory = os.path.isdir(absolute_path_correct)
# is_file = os.path.isfile(absolute_path_correct)
# print(is_file)
# print(is_directory)

# import os
# path1 = "folder1"
# path2 = "folder2"
# path3 = "file.txt"
# result = os.path.join(path1, path2, path3)
# print(result)
# result = "/".join([path1, path2, path3])
# print(result)

# Напишите программу, которая принимает в качестве аргумента командной строки
# путь к директории и выводит список всех файлов с расширением .txt внутри этой
# директории и ее поддиректорий.
# Для этой задачи используйте рекурсивную функцию, которая будет обходить все
# поддиректории и искать файлы с расширением .txt.

import os


def find_list_txt_files(directory, list_files = None):
    if not list_files:
        list_files = []
    for filename in os.listdir(directory):
        if os.path.isfile(filename) and filename.endswith(".txt"):
            list_files.append(os.path.join(filename))
        elif os.path.isdir(filename):
            find_list_txt_files(filename, list_files)
    return list_files



print(find_list_txt_files(os.getcwd()))