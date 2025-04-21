# import re
#
# pattern = r"\b\w{3,5}\b"
# text = "Hello, |how| how are you?"
# result = re.findall(pattern, text)
# print(result)


# import re
# # (\b\w+) = \1 = hello
# # (\b\w+) = \1 = world
# pattern = r"(\b\w+\b)\.\1"
# text = "Hello.hello ---- world.world"
# # result = re.findall(pattern, text)
# # print(result)
# replaced_text = re.sub(pattern, r"\1", text, flags=re.IGNORECASE)
# print(replaced_text)

#
# import re
#
# text = "Python is an amazing programming language."
# pattern = "amazing"
# match = re.search(pattern, text)
# if match:
#     print(match)
#     print(match.start())
#     print(match.end())
#     print("Совпадение найдено:", match.group())
# else:
#     print("Совпадение не найдено")


# import re
#
# text = "ID12345 is confirmed. ID23456 is confirmed"
#
# # Проверяем, начинается ли строка с "ID" + цифры
# match = re.match(r"ID\d+", text)
#
# if match:
#     print("Объект Match:", match)
#     print("Само совпадение:", match.group())
#     print("Диапазон совпадения:", match.span())
# else:
#     print("Нет совпадения.")

#
# import re
#
# text = "Order ID: 12345, Invoice No: 67890, Ref: ABC9876"
#
# # Найдём все числа в тексте
# matches = re.finditer(r"\d+", text)
#
# for match in matches:
#     print("Объект Match:", match)
#     print("Само совпадение:", match.group())
#     print("Диапазон совпадения:", match.span())
#     print()

#
# import re
#
# text = "Hello, how are you, hello?"
# if match := re.search(r"\b\w{5}\b", text, re.IGNORECASE):
#     print("Match found:", match.group())
# else:
#     print("No match")
#

# def func(x):
#     return x
#
# result = [func_res := func(2), func_res**2, func_res**3]
# print(result)
