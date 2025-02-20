# while True:
#     a = float(input('Enter a first number: '))
#     b = float(input('Enter a second number: '))
#     operation = int(input('Enter a operation 1. Plus 2. Minus 3. Division 4. Multiplication: '))
#     if operation == 1:
#         result = a + b
#         print(f'The sum of your numbers is {result}.')
#     elif operation == 2:
#         result = a - b
#         print(f'The difference of your numbers is {result}.')
#     elif operation == 3:
#         result = a / b
#         print(f'The division of your numbers is {result}.')
#     elif operation == 4:
#         result = a * b
#         print(f'The multiplication of your numbers is {result}.')
#     else:
#         print('Invalid enter')
#     exit_cycle = input('Do you want to exit the program? (y/n): ')
#     if exit_cycle == 'y':
#         break

# import time
# import random
# a = int(input('Диапазон ввода от 0 до ?: '))
# comp = random.randint(0,a) # В данном случае задуманное число
# start = time.time()
# user = int(input(f'Угадайте число от 0 до {a}: '))
# while user != comp:
#     if user > comp:
#         print('Ваше число больше загаданного!')
#     elif user < comp:
#         print('Ваше число меньше загаданного!')
#     user = int(input(f'Загадай число снова (введи число от 0 до {a}): '))
# else:
#     print('Вы угадали число!')
# end = time.time()
# result = end - start
# print(f'Вы угадали число за {round(result, 1)} секунд')


