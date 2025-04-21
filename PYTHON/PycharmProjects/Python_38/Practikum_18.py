# Строка из call на сайте http://api.weatherapi.com/v1/current.json?key=0ec94fe4eefb4c04840105427251504&q=Stuttgart&aqi=no

# import requests
# # берем отсюда три пары ключ - значение
# # weather = requests.get('http://api.weatherapi.com/v1/current.json?key=0ec94fe4eefb4c04840105427251504&q=Stuttgart&aqi=no')
# city = input("Enter City: ")
#
# dictionary = {"key": "0ec94fe4eefb4c04840105427251504",
#               "q": city,
#               "aqi": "no"}
#
# weather = requests.get('http://api.weatherapi.com/v1/current.json', params=dictionary)
# if weather.status_code == 200:
#     weather_data = weather.json()['current']
#     print(f'Temperature is {weather_data['temp_c']}')

"""
Задача: скачать к себе на компьютер 100 последних фотографий со страницы Explore | Flickr.

Разобьем задачу на две части:
1. Вывести URL всех картинок. Пример URL
https://live.staticflickr.com/65535/53534030316_e8e655393a_w.jpg
2. Скачать каждую картинку по ее URL и сохранить ее на диске.
Первая задача - обязательная, вторая - опциональная.
При использовании нужно использовать библиотеки BeautifulSoap и requests, пройденное по теме
работы с файлами для сохранения картинок в файл. Вам также пригодятся лямбда-функции и
работа со списками.
Учтите, что на страничке по ссылке выше выводится много картинок и нам нужны не все. Нужные
нам имеют аттрибут loading="lazy". Отфильтруйте ненужные картинки и скачивайте только нужные.
"""

import requests
from bs4 import BeautifulSoup
import os

url = "https://www.flickr.com/explore/"
response = requests.get(url)
# print(response.text)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    imgs = soup.find_all("img", loading="lazy")
    # print(imgs)
    imgs_url = []
    for img in imgs:
        # urls = "https:" + img.get("src")
        urls = "https:" + img["src"]
        imgs_url.append(urls)
    print(imgs_url)
    os.makedirs("save_folder", exist_ok=True)
    for i, el in enumerate(imgs_url, 1):
        response_img = requests.get(el)
        with open(f"save_folder/{i}.png", "wb") as f:
            f.write(response_img.content)










