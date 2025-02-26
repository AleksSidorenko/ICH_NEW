#!/bin/bash 

# TARGET_ADDRESS="google.com" 
TARGET_ADDRESS=$(read -p "Введите адрес для пинга: " addr && echo "$addr")
# Проверка, что адрес введен
if [ -z "$TARGET_ADDRESS" ]; then
    echo "Не указан адрес для пинга."
    exit
fi
echo "Начинаем пинговать $TARGET_ADDRESS..."
MAX_PING_TIME=18
MAX_FAIL_COUNT=3
FAIL_COUNT=0

while true; 
      do
          PING_OUTPUT=$(ping -c 1 "$TARGET_ADDRESS" 2>/tmp/output.txt)
	  # SIZE=$(stat -f %z "/tmp/output.txt")
	  # SIZE=$(wc -c /tmp/output.txt | awk '{print $1}') 
	  
	  if echo "$PING_OUTPUT" | grep 'time='; then
          # if [ $SIZE -ge 0 ]; then  
	     
	     PING_TIME=$(echo "$PING_OUTPUT" | awk -F'time=' '{print $2}' | awk -F'.' '{print $1}')
	     if [ "$PING_TIME" -gt "$MAX_PING_TIME" ]; then 
                echo
		echo "Пинг $TARGET_ADDRESS ($PING_TIME мс) превышает $MAX_PING_TIME мс"
                ((FAIL_COUNT++))
	     else
		echo
		echo "Пинг $TARGET_ADDRESS успешен $PING_TIME мс"
             fi
          else    
              ((FAIL_COUNT++))
	      echo
              echo "Не удалось выполнить пинг ($FAIL_COUNT/$MAX_FAIL_COUNT)."
	  fi  
          if [ "$FAIL_COUNT" -ge "$MAX_FAIL_COUNT" ]; then
             echo
	     echo "Соединение прервано! Три ($FAIL_COUNT/$MAX_FAIL_COUNT) неудачные попытки подряд."
             exit
          fi
          sleep 1 
      done
