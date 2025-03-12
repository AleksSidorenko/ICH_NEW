# import sys
# print('Список параметров, переданных скрипту')
# args = sys.argv
# print(args)
# print(sys.path)
# print([arg for arg in sys.argv if arg[0]!='-'])


# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='Path to input file')
# parser.add_argument('--output', help='Path to output file', required=True)
# args = parser.parse_args()
# print(args.input)
# print(args.output)


# import os
# import sys
#
# current_dir = os.getcwd()
# print(current_dir)
# args = len(sys.argv)
# print(args)
# print(current_dir)
# os.chdir('/path/to/directory')
# os.chdir('..')
# print(os.getcwd())
#
# files = os.listdir("..")
# print(files)
# print()
# os.mkdir('new_directory')
# os.makedirs('new_directory/sub_directory')
# open("sdfs.txt", "w")
# print(os.walk(".."))
# for i in os.walk(".."):
#     print(type(i))
#     print(i)
# for dirpath, dirnames, filenames in os.walk("."):
#     for filename in filenames:
#         print(os.path.join(dirpath, "new", filename))
#     for dirname in dirnames:
#         print(os.path.join(dirpath, "new", dirname))
#
# print()
#
# for i in os.walk("."):
#     for filename in i[2]:
#         print(os.path.join(i[0], filename))
#     for dirname in i[1]:
#         print(os.path.join(i[0], dirname))

# __ = 5
# print(__)
# l = [1, 2, 3, 4, 5]
# a, b, *_ = l
# print(a)
# print(b)
# print(_)

# a = [1, 2, 3]
#
# q, e = a
# print(q)
# # print(w)
# print(e)

#
#
# import os
# path = os.path.join('/path/to', 'file.txt')
# print(path)
# print(type(path))
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
#
# print(os.getcwd())
# print(os.path.abspath(os.getcwd()))
#
#
# import os
# path1 = "folder1"
# path2 = "folder2"
# path3 = "file.txt"
# result = os.path.join(path1, path2, path3)
# # result = "/".join([path1, path2, path3])
# print(result)
#
# import os
#
# print(type(os.path.join)) # <class 'function'>
#
# def analise_information(file_path):
#     print(file_path)
#
#
# import os
# def process_directory(directory):
#     for name in os.listdir(directory):
#         current_path = os.path.join(directory, name)
#         if os.path.isfile(current_path):
#             # Обработка файла
#             analise_information(current_path)
#         elif os.path.isdir(current_path):
#             # Рекурсивный вызов для вложенного каталога
#             process_directory(current_path)
#
#
# start_directory = '.'
# # start_directory = 'lessons'
# process_directory(start_directory)
#




import os

# Доработанный вариант решения
# def find_list_txt_files(directory, list_files=None):
#     if list_files is None:
#         list_files = []  # Создали при первом вызове
#     for filename in os.listdir(directory):
#         filepath = os.path.join(directory, filename)  # Исправили ошибку, из-за которой вложенные файлы не находятся
#         if os.path.isfile(filepath) and filepath.endswith(".txt"):
#             list_files.append(os.path.join(filepath))
#         elif os.path.isdir(filepath):
#             find_list_txt_files(filepath, list_files)
#     return list_files
#
#
# print(find_list_txt_files("."))
#
#
# # Второй вариант решения
# import os
#
# def find_txt_files(directory):
#     list_files = []
#     for filename in os.listdir(directory):
#         filepath = os.path.join(directory, filename)  # Исправили ошибку, из-за которой вложенные файлы не находятся
#         if os.path.isfile(filepath) and filepath.endswith(".txt"):
#             list_files.append(os.path.join(filepath))
#         elif os.path.isdir(filepath):
#             list_files.extend(find_txt_files(filepath))  # Собираем результаты из рекурсии
#     return list_files
#
# print(find_txt_files("."))


# import os
# print(f'Current Working Directory is: {os.getcwd()}')
#
# # print(os.path.exists('Lesson_Lerhrer'))
#
# # print(os.path.exists('lesson_40.py'))
#
# # print(os.listdir('Lesson_Lerhrer'))
#
# from glob import glob
# print(list(glob(os.path.join('Lesson_Lerhrer', '*.py'))))


