# import requests
# print(requests.__version__)

# **Задание:**
# **Скачайте случайную картинку кота по URL из ответа и сохраните как `cat.jpg`.
## **Случайный кот**
# **Сервис:**
# (https://api.thecatapi.com/v1/images/search](https://api.thecatapi.com/v1/images/search)

# res = requests.get("https://api.thecatapi.com/v1/images/search")
# # print(res.json())
# # print(res.text)
# data_json = res.json()
# data_url = data_json[0]['url']
# get_data = requests.get(data_url)
# # print(get_data.content)
# with open('cat.ipg', 'wb') as file:
#     file.write(get_data.content)

"""
Определите, содержит ли заданная строка набор данных символов (a-z, A-Z и 0-9).
"""
# import re
# from re import findall, finditer
#
# text = "Some text"
# ser = re.search(r'[a-zA-Z0-9]', text, re.IGNORECASE)
# print(ser)
# is_exist = bool(ser)
# print(is_exist)
"""
Определите, содержит ли строка символ ‘aʼ, за которым следует 1 или более символов ‘bʼ.
"""
# import re
#
# text = "Some text and some other text."
# ser = re.search(r'a+', text, re.IGNORECASE)
# print(ser)
# is_exist = bool(ser)
# print(is_exist)
"""
Напишите программу, которая удаляет нули 0) перед цифрами в IP адресе. Например,
“192.01.001.10ˮ → “192.1.1.10ˮ
"""
# text = "192.01.001.10"
#
# new_text = re.sub(r"\b0+", "", text)
# print(new_text)

"""
Определите, содержит ли строка цифры в конце. 
"""


"""
Найдите вхождения и позиции подстроки в строке. Пример: строка “Домашние задания,
задания в классе, отпускные заданияˮ, подстрока “заданияˮ, вывод “заданияˮ на 9-15,
“заданияˮ на 18-24, “заданияˮ на 46-52.
"""
import re
text = "Домашние Задания, задания в классе, отпускные задания"

result = re.finditer(r"\bзадания\b", text, flags=re.IGNORECASE)
for word in result:
    print(word.group(0))

# Определите, содержит ли строка символ 'aʼ, за которым следует 1 или более символов 'bʼ.

# # ++++++++++
# import re
# # ++++++++++
# text = 'Some text and bababala'
# symbols = re.search(r'a[lbn]+', text, re.IGNORECASE)
# print(symbols)
# is_exists = bool(symbols)
# print(is_exists)






