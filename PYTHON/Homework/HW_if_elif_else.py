# print("-------- Homework №5 ---------")
# print("1. Напишите программу, которая запрашивает у пользователя три числа "
#       "и выводит их в порядке возрастания, разделенные запятой. "
#       "Используйте условные операторы и вложенные условия для решения задачи. "
#       "Предполагается, что все три числа различны.")
#
# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# z = int(input("Enter the third number: "))
# if x > y:
#     first = y
#     if y > z:
#         first = z
#         second = y
#         third = x
#     else:
#         if z > x:
#             second = x
#             third = z
#         else:
#             second = z
#             third = x
# else:
#     first = x
#     if x > z:
#         first = z
#         second = x
#         third = y
#     else:
#         if z > y:
#             second = y
#             third = z
#         else:
#             second = z
#             third = y
# print(f'{first}, {second}, {third}')
# if x > y:
#     x, y = y, x
#     if x > z:
#         x, z, y = z, y, x
#     else:
#         x, z = x, z
# else:
#     x, y = x, y
#     if x > z:
#         x, z, y = z, y, x
#     else:
#         x, z = x, z
# print(f'{x}, {y}, {z}')

# print(max(x, y, z))
# print(min(x, y, z))

# print("2. Напишите программу, которая запрашивает у пользователя год и проверяет,"
#       "является ли он високосным. Год является високосным, если он делится на 4 без остатка,"
#       "но не делится на 100 без остатка, за исключением годов, которые делятся на 400 без остатка."
#       "Выведите соответствующее сообщение на экран с помощью команды print.")
#
# year = int(input("Enter the year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f'{year} is leap year')
# else:
#     print(f'{year} is not leap year')




