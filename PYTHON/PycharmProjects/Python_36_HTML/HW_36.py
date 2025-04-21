"""
Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
использует библиотеку BeautifulSoup для парсинга HTML
и выводит список всех ссылок на странице.
"""
# import requests
# from bs4 import BeautifulSoup
#
# def get_html(dome):
#     url = "https://" + dome
#     try:
#         html = requests.get(url)
#         html.raise_for_status()
#     except requests.RequestException as e:
#         print(f"Ошибка при загрузке страницы: {e}")
#         return
#     soup = BeautifulSoup(html.text, "html.parser")
#     links = soup.find_all('a')
#     for link in links:
#         print(link.get('href'))
#
# name_dom = input("Введите домен (например: \"example.com\"): ")
# # name_dom = "example.com"
# get_html(name_dom)

"""
Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы 
и уровень заголовков, а затем использует библиотеку BeautifulSoup для парсинга HTML 
и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.
"""
import requests
from bs4 import BeautifulSoup

def get_headers(name_dome, header_lvl):
    url = "https://" + name_dome
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Ошибка при загрузке страницы: {error}")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    headers = soup.find_all(f'h{header_lvl}')
    if headers:
        print(f"\nЗаголовки уровня h{header_lvl}:")
        for tag in headers:
            print("-", tag.get_text(strip=True))
    else:
        print(f"Заголовки уровня h{header_lvl} в {url} не найдены.")

name_dom = input("Введите домен (например: \"example.com\"): ")
while True:
    try:
        header_level = int(input("Введите уровень заголовка (1–6): "))
        if 1 <= header_level <= 6:
            get_headers(name_dom, header_level)
            break
        raise ValueError("Уровень заголовка должен быть числом от 1 до 6.")
    except ValueError as e:
        print(e)
