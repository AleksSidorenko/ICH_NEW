# print("2. Напишите программу, которая запрашивает у пользователя число N и выводит первые N чисел Фибоначчи. "
#       "Числа Фибоначчи - это последовательность чисел, "
#       "где каждое следующее число является суммой двух предыдущих чисел (начиная с 0 и 1). "
#       "Используйте цикл while для решения задачи. Выведите числа через запятую с помощью команды print.")
# while True:
#     n = int(input("Enter a number: "))
#     f1, f2 = 0, 1
#     count = 0 # счетчик
#     while count < n:
#         if count == 0:
#             print(f'Первые {n} чисел Фибоначчи: ', f1, end='')
#         else:
#             print(f', {f1}', end='')
#         f1, f2 = f2, f1 + f2
#         count += 1
#     print()

# 1. Даны два целых числа a и b. Напишите программу, которая находит большее из двух чисел и печатает сообщение, какое число больше.
# a, b = map(int,input('Enter two numbers: ') .split(","))
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# if a > b:
#     print("The first number is greater than the second.")
# else:
#     print("The second number is greater than the first.")

# a = int(input("Введите первое число : "))
# b = int(input("Введите второе число : "))
# c = int(input("Введите третье число : "))
# print ( max(a,b,c))
# if a < b < c:
#     print(f'Number {c} is the biggest number')
# elif a < c < b:
#     print(f'Number {b} is the biggest number')
# else:
#     print(f'Number {a} is the biggest number')

# 3. Есть логическая переменная  weekday.
# Напишите программу, которая выводит сообщение “рабочий день”,
# если переменная истинна и сообщение “выходной” - если ложна.

# weekday = bool(int(input(f'1 - это рабочий день, 0 - выходной: ')))
# if weekday:
#     print(f'Рабочий день.')
# else:
#     print(f'Выходной.')
# weekday = int(input(f'1 - рабочий, 2 - выходной: '))
# if weekday == 1:
#     print(f'Рабочий день.')
# elif weekday == 2:
#     print(f'Выходной.')
# else:
#     print(f'Ошибка.')

# 4. У нас есть две логические переменные:
# isWeekday, isVacation (выходной день и каникулы).
# Они могут принимать разные значения, всего 4 комбинации: true - true, true - false, false - false,
# false - true. Есть правило: мы можем поспать, если день не рабочий или мы на каникулах.
# Напишите программу, которая в зависимости от значений двух переменных печатает,
# можем ли мы поспать или нет.
# То есть для значений isWeekday = False и isVacation = False программа должна печатать “можете поспать”.

# isWeekday = bool(int(input('Введите рабочий = 1, нерабочий = 0: ')))
# isVacation = bool(int(input('Введите каникулы = 1, учимся = 0: ')))
# if isWeekday == False or isVacation == True:
#     print(f'SLEEP')
# else:
#     print('GO to Work')
# if not isWeekday or isVacation:
#     print(f'SLEEP')
# else:
#     print('WORK')




