# pip3 install requests
# import requests

# response = requests.get("https://example.com")
# print(type(response))
# print(response.status_code) # Выводит код состояния ответа
# # print(response.text) # Выводит данные, полученные от сервера
# print(response.url)
# # print(response.content)
# print(response.headers) # Выводит заголовки ответа

# import requests
# response = requests.get('https://httpbin.org/get')
# print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.json())
# print(response.json()['origin'])
# #
# # print("------")


# import requests
# response = requests.head('https://httpbin.org/head')
# print(response.status_code)
# print(response.headers)
# print(response.text)


# import requests
# response = requests.get("https://api.github.com/users/github")
# data = response.json()
# print(data)
# # for k, v in data.items():
# #     print(f"{k}: {v}")



# # не работает
# import requests
#
# response = requests.get('https://regex101.com/')
# print(response.status_code)
# print(response.headers)


# # добавили заголовки
# import requests
#
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
# response = requests.get('https://regex101.com/', headers=headers)
#
# print(response.status_code)
# print(response.headers)



# import requests
# response = requests.get("https://api.github.com/users/github")
# data = response.json()
# print(type(data))
# for k, v in data.items():
#  print(f"{k}: {v}")


# --------------------------

# import requests
#
# cookies = {"session_id": "123456789"}
#
# # Отправляем запрос, куки должны быть автоматически отправлены серверу
# response = requests.get("https://httpbin.org/cookies", cookies=cookies)
#
# # Печатаем cookies, которые были отправлены сервером
# print("\nCookies после запроса:")
# print(response.json())  # Ответ сервера будет в формате JSON
# # print(response.cookies)



# import requests
#
# response = requests.get('https://random-data-api.com/api/v2/users?size=10')
# res=response.json()
# print(res)
# l = 20
# for person in res:
#     # print(person)
#     print(f"{person['last_name']:{l}} {person['first_name']:{l}} {person['email']}")
#     # print(f"{person['last_name']} {person['first_name']} {person['email']}")

