# from bs4 import BeautifulSoup, Tag

# html_doc = '<html><head><title>Test</title></head><body><p>Some text</p><p>Some text2</p><p>Some text3</p></body></html>'
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)
# #
# print(soup.text)
# print(type(soup))
# soup.find(tag) — поиск первого элемента с определённым тегом.
# print(soup.find("title"))
# print(soup.find("title").text)
# print(type(soup.find("title")))
# print()
#
# # soup.find_all(tag) — поиск всех элементов с определённым тегом.
# paragraphs = soup.find_all('p')
# for p in paragraphs:
#     print(p.text)
# print()
#
# # soup.find(class_='classname') — поиск элемента с определённым атрибутом.
# html_doc = '<div class="anotherclass">Hi</div><div class="myclass">Hello World</div>'
# soup = BeautifulSoup(html_doc, 'html.parser')
# div = soup.find(class_='myclass')
# print(div.text)
# print()
#
# soup.find_all('a') — найти все ссылки.
# soup = BeautifulSoup('<a href="https://example.com" id="sds">Link</a><a href="https://example2.com" id="1sds">Link2</a>', 'html.parser')
# links = soup.find_all('a')
# print(links)
# for link in links:
#     print(link)
#     print(link['href'])
#     print(link['id'])
# print()
#
#
# .find_parent() — получение родительского элемента:
# soup = BeautifulSoup("<div><p>Text</p><p>Text2</p></div>", 'html.parser')
# p = soup.find('p')
# # parent = p.find_parent()
# parent = p.parent
# print(type(parent))
# print(parent.name)
# print(parent)
# child = parent.children
# for ch in child:
#     print(ch)
# print()
#
#
# # .find_next_sibling() — получение следующего соседа:
# soup = BeautifulSoup("<div><p>First</p><p>Second</p><p>Third</p></div>", 'html.parser')
# p = soup.find('p')
# next_sibling = p.find_next_sibling()
# print(next_sibling.text)
# next_sibling = next_sibling.find_next_sibling()
# print(next_sibling.text)
# print()
# #
#
# # .find_previous_sibling() — получение предыдущего соседа:
# soup = BeautifulSoup("<div><p>First</p><p>Second</p></div>", 'html.parser')
# p = soup.find('p', string='Second')
# print(p.text)
# prev_sibling = p.find_previous_sibling()
# print(prev_sibling.text)
#
#



import requests
from bs4 import BeautifulSoup
#

page = requests.get("https://mignews.com/mobile")
print(page.status_code)
filteredNews = []
allNews = []
# # Создание объекта Beautiful Soup из HTML-страницы
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
allNews = soup.find_all("li", class_ ="icon-grey")
for data in allNews:
    if data.find('a', class_='ml-1 text-decoration-none') is not None:
        filteredNews.append(data.text)

for data in filteredNews:
    print(data)
#
# # Извлечение данных из тегов
# title = soup.title.text
# links = soup.find_all("p")
# print(title)
# print(links)
# print(links[0]["href"])
# print()
#
#
# # Навигация по структуре документа
# parent = soup.find("div").parent
# next_sibling = soup.find("p").next_sibling
# print(parent)
# print(next_sibling)
#
# # Манипуляции с содержимым
# new_tag = soup.new_tag("a", href="https://example.com")
# soup.body.append(new_tag)


# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup('<div><a href="https://example2.com">Start</a><div><p>Text</p><p>Another text</p></div></div>', 'html.parser')
# div = soup.find('p')
# print(div.parent)
# print(type(div.parent))
# print("-")
# print(div.parent())
# print(type(div.parent()))


# import requests
# from bs4 import BeautifulSoup
#
# html = requests.get("https://realpython.com").text
# soup = BeautifulSoup(html, "html.parser")
#
# links = soup.find_all("a")
# for i in links:
#     href = i.attrs.get("href")
#     # if href[:4]=="http":
#     print(href)



# teacher
# import re
#
# def highlight_keywords(text, keywords):
#     for word in keywords:
#         pattern = fr'\b({word})\b'
#         text = re.sub(pattern, r'*\1*', text, flags=re.IGNORECASE)
#     return text
#
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
# print(highlight_keywords(text, keywords))