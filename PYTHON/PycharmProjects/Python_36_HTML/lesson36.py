# import requests
# from bs4 import BeautifulSoup
# html = requests.get("https://google.com").text
# html = BeautifulSoup(html, "html.parser")
# print(html.get_text)
# print(type(html))


# Создание объекта Beautiful Soup из HTML-страницы
# soup = BeautifulSoup(html, "html.parser")
# print(soup)
# print(type(soup))
#
# # Извлечение данных из тегов
# title = soup.title
# links = soup.find_all("a")
# print(title)
# print(title.text)
# print(links)
# Навигация по структуре документа
# p = soup.find("p")
# print(p)
# print(p.parent)
# print(p.next_sibling)

# next_sibling = soup.find("div").next_sibling
# # Манипуляции с содержимым
# new_tag = soup.new_tag("a", href="https://example.com")
# soup.body.append(new_tag)






