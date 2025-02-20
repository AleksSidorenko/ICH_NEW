# file = open("names.txt")
# print(file.read())
# print(file.readline())
# print(file.readlines())

# for line in file:
#     print(line, end="")
# file.close()

# with open("names.txt") as file:
#     for line in file:
#         print(line, end="")

# Напишите программу, которая запрашивает у пользователя имя файла (переменная file) и целое
# число (переменная lines), а затем выводит на печать построчно последние строки в количестве
# lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию
# на файле article.txt со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
s = "article.txt" # input("Введите имя файла: ")
n = int(input("Введите количество строк: "))
with open(s, "r", encoding="utf-8") as f:
    print(f.readlines()[-n:])
    # result = f.readlines()
    # print(result[n:])
