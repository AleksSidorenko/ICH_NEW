"""
1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу
и возвращает объект ответа. Затем выведите следующую информацию об ответе:
- Код состояния (status code)
- Текст ответа (response text)
- Заголовки ответа (response headers)
Пример использования:
url = "https://api.example.com"
response = get_response(url)
print("Status Code:", response.status_code)
print("Response Text:", response.text)
print("Response Headers:", response.headers)
"""

# import requests
#
# def get_response(url):
#     return requests.get(url)
#
#
# response = get_response("https://example.com")
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
# print("Response Headers:", response.headers)

"""
2. Напишите функцию find_common_words(url_list), 
которая принимает список URL-адресов 
и возвращает список наиболее часто встречающихся слов на веб-страницах. 
Для каждого URL-адреса функция должна получить содержимое страницы с помощью запроса GET 
и использовать регулярные выражения для извлечения слов. 
Затем функция должна подсчитать количество вхождений каждого слова 
и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.
"""
# GPT 1
# import requests
# import re
# from collections import Counter
#
# def find_common_words(url_list):
#     all_words = []
#
#     for url in url_list:
#         try:
#             html = requests.get(url).text
#             text = re.sub(r'<[^>]+>', ' ', html)
#             words = re.findall(r'\b\w+\b', text.lower())
#             all_words.extend(words)
#         except requests.RequestException as e:
#             print(f"Ошибка при получении {url}: {e}")
#             continue
#
#     return Counter(all_words)
#
#
# url_list = ["https://www.example.com", "https:/google.com"]
# word_counter = find_common_words(url_list)
# top_n = 5
# for word, count in word_counter.most_common(top_n):
#     print(f"{word}: {count}")

# GPT 2
# import requests
# from bs4 import BeautifulSoup
# import re
# from collections import Counter
#
# def find_common_words(url_list, top_n=10):
#     all_words = []
#
#     for url in url_list:
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#
#             soup = BeautifulSoup(response.text, 'html.parser')
#             text = soup.get_text()  # только текст без тегов
#             words = re.findall(r'\b\w+\b', text.lower())
#             all_words.extend(words)
#         except requests.RequestException as e:
#             print(f"Ошибка при обработке {url}: {e}")
#             continue
#
#     word_counts = Counter(all_words)
#     return word_counts.most_common(top_n)
#
#
# url_list = ["https://www.example.com", "https:/google.com"]
# print(find_common_words(url_list))


