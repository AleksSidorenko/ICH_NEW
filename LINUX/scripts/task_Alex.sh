#!/bin/bash
# Создание 10 файлов с порядковым номером и датой создания: 
# 1_20.04.23 , 2_20.04.23 , 3_20.04.23 .. 10_20.04.23 
# Директорий группы
DIRECTORY="/opt/111124-ptm"
# Мой директорий
MY_DIR="$DIRECTORY/AlexSidorenko"
#
DATE=$(date +"%d.%m.%y")
#
filePath=$MY_DIR/$i'_'$DATE
for i in {1..10}
do
    # touch $MY_DIR/$i'_'$DATE | date +'%H:%M:%S' >> $MY_DIR/$i'_'$DATE
    touch $filePath && date +'%H:%M:%S' >> $filePath
done

