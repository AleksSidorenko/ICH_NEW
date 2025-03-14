#!/bin/bash

# Cкрипт, который будет выполнять следующую задачу: копировать все файлы с определенным расширением из одной директории в другую.

# 1.Запросить исходную и целевую директории у пользователя
# Описание: Запросить у пользователя указание исходной и целевой директорий.
# Действие: Предложить пользователю ввести пути к исходной и целевой директориям.
# Использовать следующие переменне: Исходная директория - source_directory 
# Целевая директория - target_directory

# Запрашиваем исходную директорию
echo "Enter the path to the SOURCE directory:"
read source_directory

# Запрашиваем целевую директорию
echo "Enter the path to the TARGET directory:"
read target_directory

# Выводим введенные пути для проверки
echo "SOURCE directory: $source_directory"
echo "TARGET directory: $target_directory"

# 2.Запросить расширение файлов для копирования
# Описание: Запросить у пользователя указание расширения файлов, которые нужно скопировать.
# Действие: Предложить пользователю ввести расширение файлов.
# Использовать для сохранения переменную - file_extension

# file extension request
read -p "input the file extension: " file_extension

# 3.Проверить существование и доступность исходной и целевой директорий
# Описание: Проверить, существуют ли и доступны ли исходная и целевая директории.
# Действие: Проверить существование и доступность директорий. Если они не существуют или недоступны, вывести сообщение об ошибке.
# Прервать работу скрипта с кодом 1
if [ ! -d "$source_directory" ]; then
    echo "Error: Исходная директория '$source_directory' не существует или не является директорией."
    exit 1
fi

if [ ! -r "$source_directory" ]; then
    echo "Error: Нет доступа для чтения исходной директории '$source_directory'."
    exit 1
fi

if [ ! -d "$target_directory" ]; then
    echo "Error: Целевая директория '$target_directory' не существует или не является директорией."
    exit 1
fi

if [ ! -w "$target_directory" ]; then
    echo "Error: Нет доступа для записи в целевую директорию '$target_directory'."
    exit 1
fi

if [ ! -d "$source_directory" ]; then
    echo "Error: Исходная директория '$source_directory' не существует или не является директорией."
    exit 1
fi

if [ ! -r "$source_directory" ]; then
    echo "Error: Нет доступа для чтения исходной директории '$source_directory'."
    exit 1
fi

if [ ! -d "$target_directory" ]; then
    echo "Error: Целевая директория '$target_directory' не существует или не является директорией."
    exit 1
fi

if [ ! -w "$target_directory" ]; then
    echo "Error: Нет доступа для записи в целевую директорию '$target_directory'."
    exit 1
fi

# 4.Проверить наличие файлов с указанным расширением в исходной директории
# Описание: Проверить, есть ли файлы с указанным расширением в исходной директории.
# Действие: Поиск файлов с указанным расширением в исходной директории. Если файлы не найдены, вывести сообщение об ошибке.
# Прервать работу скрипта с кодом 1

if ls "$source_directory"/*."$file_extension" 1> /dev/null 2>&1; then
	echo "Файлы с расширением .$file_extension найдены в директории $source_directory"
else
	echo "Ошибка: В директории $source_directory нет файлов с расширением .$file_extension"
	exit 1
fi

# 5.Скопировать файлы с указанным расширением в целевую директорию
# Описание: Скопировать все файлы с указанным расширением из исходной директории в целевую.
# Действие: Копирование каждого файла с указанным расширением из исходной директории в целевую. Вывести сообщение о копировании каждого файла.

echo 'Copying all files with' $file_extension 'type from' $source_directory 'to' $target_directory

for file in $source_directory/*$file_extension; do
	if [ -f $file ]; then
		cp $file $target_directory
		echo 'File' $file 'copied to' $target_directory
	fi
done

echo 'All files with type' $file_extension 'was copied from' $source_directory 'to' $target_directory
