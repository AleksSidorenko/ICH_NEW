#!/bin/bash
#
echo "Привет! Этот скрипт добавляет права на исполнение для файлов sh в директории /opt/111124-ptm/"
#
DIRECTORY="/opt/111124-ptm"
echo "Директорий группы: $DIRECTORY"
# echo "Текущий директорий"
# CURRENT_DIR=$(pwd)
MY_DIR="$DIRECTORY/AlexSidorenko"
#
echo "Мой директорий: $MY_DIR"
echo "Текущая дата"
DATE=`date '+%d:%m:%y'`
echo $DATE
# Список всех файлов в директории
L_FILE=$(ls -p $DIRECTORY | grep -v /)
# или так: Список всех файлов в директории
# L_FILE=$(find $DIRECTORY -type f -name "*.sh")
#
# L_SH=$(ls -l $MY_DIR | awk '{print $1}' | grep "x")
#
if [[ "$L_FILE" != *.sh ]]; then
     echo "Файлов sh в директории: $DIRECTORY нет"
else
     for FILE in $L_FILE
     do
         if [[ "$FILE" == *.sh ]]; then
	      if [[ "$L_SH" == x ]]; then
		 echo "1"
	      else	 
                 chmod +x "$DIRECTORY/$FILE"
                 echo "Добавлены права на исполнение для: $FILE в $DIRECTORY"
	       fi
         fi	
     done
fi	

