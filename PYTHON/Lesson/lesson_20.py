# На вход программе подается слово в виде строки.
# Необходимо прочитать это слово и его первую букву сделать заглавной,
# а остальные - малыми. Результат отобразить на экране.
# Option 1
# name = input("What is your name? ")
# print(name.capitalize()) # делает первую букву заглавной
# Option 2
# user_input = input(f'Введите строку: ')
# first_letter = user_input[0].upper()
# rest_letters = user_input[1:].lower()
# print(first_letter + rest_letters)

# На вход программе подается строка.
# Необходимо прочитать эту строку и определить число вхождений дефисов (-) в ней.
# На экране отобразить полученное число.
# s = input("Enter a string: ")
# s.count("-")
# print(s.count("-"))

# На вход программе подается строка. Прочитайте эту строку и с помощью метода
# найдите в ней индекс первого вхождения
# фрагмента "ra". Полученное число (индекс) выведите на экран.
# Option 1
# s = input("Enter a string: ")
# print(s.find("ra"))
# Option 2
# s = input("Enter a string: ")
# print(s.index("ra"))

# На вход программе подается строка.
# Прочитайте ее и замените в ней все двойные дефисы (--) и тройные (---) на одинарные (-).
# Подумайте, в какой последовательности следует выполнять эти замены.
# Результат преобразования выведите на экран.
# Option 1
# s = input("Enter a string: ")
# s1 = s.replace("---", "-").replace("--", "-")
# print(s1)
# # Option 2
# user_input = input("Enter your string with hyphen: ")
# print(user_input.replace("---", "-").replace("--", "-"))

# На вход программе подаются три целых положительных числа (максимум трехзначные),
# записанные в одну строчку через пробел. Необходимо их прочитать из входного потока.
# Затем, для двухзначных и однозначных чисел добавить слева незначащие нули так,
# чтобы все числа содержали по три цифры.
# Вывести на экран полученные числа в столбик (каждое с новой строки) в порядке их чтения из входного потока.
# a,b,c = map(str,input().split())
# print(a.rjust(3, "0"), b.rjust(3, "0"), c.rjust(3,"0"), sep = "\n")

# На вход программе подается строка, состоящая из названий городов, разделенных пробелом.
# Необходимо прочитать эту строку и преобразовать так,
# чтобы названия городов шли через точку с запятой (без пробелов).
# Результат (строку) отобразите на экране
# s = input("Enter a string: ")
# s1 = s.split()
# print(";".join(s1))

# Разное:
# text1 = "I'm a programmer"
# text2 = 'I\'m a programmer' # экранирование
# text2 = 'I\'m \t a programmer' # табуляция
# text2 = 'I\'m \n a programmer'
# text2 = 'I\'m \n a progra\a mmer'
# path = "D:\\Python\\Projects\\ster\\tex1.py"
# print(path)
# text2 = "She said: \"Hello!\""
# print(text2)

# метод format:
# 1.
# name = "Maksim"
# age = 18
# print("Меня зовут {0}, мне {1}, Я люблю программировать".format(name, age))
# 2.
# name = "Maksim"
# age = 18
# print(f"Меня зовут {name}, мне {age} лет. Я люблю программировать")
# 3.
# print("Меня зовут " + name +", мне " + str(age) +" лет. Я люблю программировать")

# price = 9.99
# quantity = 5
# total = price * quantity
# text = "Total: ${:.2f}".format(total)
# print(text)
# {:.2f} спецификатор форматирования, : - начало, .2f - формат числа с двумя знаками после запятой,
# f - флотовое число
# f указывает, что это число должно быть представлено в виде с плавающей точкой (float).
# .2 указывает на то, что после десятичной точки должно быть ровно 2 знака.
# .2f — формат числа с двумя знаками после запятой:
# {:.2f}: это спецификатор форматирования, который указывает, как нужно вывести число:

# text = "|{:>10}|{:^10}|{:<10}|".format("право", "центр", "лево")
# print(text)
# :> выравнивание вправо.
# :< выравнивание влево.
# :^ выравнивание по центру.

# print("{:d}".format(42))  # десятичная
# print("{:x}".format(255)) # шестнадцатеричная
# print("{:b}".format(10)) # двоичная

# name = "John"
# age = 30
# text = f"My name is {name} and I am {age} years old."
# print(text)

# price = 9.99
# q = 5
# total = price * q
# text = f'Total:$ {total:.2f}'
# print(text)

# name = "John"
# age = 30
# text = f'My name is {name:>5} and I am  {age:-^10} years old.' # name cдвигается вправо на 30 спробелов заполняется =
# print(text)
# print(f"{'Hello':*<10}") # заполняется *

#  На вход приходят имя-фамилия-пол-возраст.
#  Программа выводит приветственную строку,
#  в которую вставлены имя-фамилия и пишет дополнительно
#  что средний возраст всех людей твоего пола среди встреченных ранее – такой-то.
#  Реализовать без хранения списков или иных массивов в памяти.
# total_age = 0
# count_man = 0
# count_woman = 0
# while count_man <= 3 or count_woman <= 3:
#     name = input("Enter your name: ")
#     last_name = input("Enter your second name: ")
#     gender = input("Enter your gender: ")
#     age = int(input("Enter your age: "))
#     print(f"Hello, {name} {last_name}!")
#     if gender == 'male':
#         total_age += age
#         count_man += 1
#         average_age = total_age / count_man
#         print(f"Average age from all respondents your gender is {average_age:.1f} years old.")
#     elif gender == 'female':
#         total_age += age
#         count_woman += 1
#         average_age = total_age / count_woman
#         print(f"Average age from all respondents your gender is {average_age:.1f} years old.")
#     ask = input("Do you want to continue? (yes/no): ")
#     if ask == 'no':
#         break

# Напишите программу, которая выводит на экран следующий текст,
# используя строковые литералы и экранирование символов:
# "Hello\tWorld!\nHow are you?"
# print("Hello\tWorld!\nHow are you?")

# не доработана задача
# Приходит текст из 5 строк, надо
#   1) сделать так, чтобы все предложения начинались с большой буквы.
#   2) не было подряд несколько пробелов, запятых, многоточий и т.п.
#   3) Строка не должна начинаться с пробелов,
#       допустима только табуляция (отступ).
#   4) Не забывайте, что точка не всегда значит конец предложения!
#   Например, и т.д. и т.п.
# text = " ".join("""   это пример текста. с несколькими строками! он начинается с пробелов?
# и т.д. есть лишние пробелы. и даже многоточия...""".split())
# format_text = text.split(". ")
# i = 0
# while i < len(format_text):
#     format_text[i] = format_text[i].capitalize()
#     i += 1
# print(f'{format_text}')

# Работа со срезами
# s = input("Enter a string: ")
# print(s[2])
# print(s[-2])
# print(s[::-1])
# print(s[:5])

# выведите все символы с четными индексами
# (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
# s = input("Enter a string: ")
# print(s[::2]) # вывод четных чисел
# print(s[1::2]) # вывод нечетных чисел






