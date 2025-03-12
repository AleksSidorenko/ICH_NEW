# while True: # Цикл
#     num_1 = int(input("Enter the first number: "))
#     num_2 = int(input("Enter the second number: "))
#     if num_1 > num_2:
#         print(f' {num_1}, is greater than {num_2}')
#     elif num_1 < num_2:
#         print(f' {num_1}, is less than {num_2}')
#     else:
#         print(f' {num_1}, is equal to {num_2}')
#     ask = input("Do you want to continue? (y/n): ").lower()
#     if ask == "n":
#         break

# num = int(input("Enter a number: "))
# s = 0 # для хранения вычисленной суммы
# i = 1 # значение текущего слагаемого
# while i < num:
#     s += i # s = s + i
#     i += 1
#     print(s)
# print(f'The sum is: {s}.') # print(f'Цикл завершен. Сумма s = {s}.')

# num = int(input("Enter a number: "))
# s = 0 # для хранения вычисленной суммы
# i = 1 # значение текущего слагаемого
# while i <= num and i <= 50:
#     s += i  # s = s + i
#     i += 1
#     print(s)
# print(f'The sum is: {s}.')

# n = -10
# i = -1
# while i >= n:
#     print(i)
#     i -= 1

# pass_true = "abc"
# ps = ""
# while ps != pass_true:
#     ps = input("Enter your password: ")
# print(f'Enter complited!')

# num = int(input("Enter a number: "))
# i = 1
# while i <= num:
#    if i % 3 == 0:
#        print(i)
#    i += 1

# i = 0
# while True:
#     i += 1
#     break
# print(f'End of loop {i}')

# s = 0
# d = 1
# while d != 0:
#     d = int(input("Enter a number: "))
#     if d % 2 == 0:
#         continue
#     s += d
#     print(f's = {s}')
# print('End of loop')

# s = 1/2 + 1/3 + 1/4 + 1/5 + 1/0
# s = 0
# i = -9
# while i < -1:
#     if i == 0:
#         break
#     s += 1/i
#     i += 1
# else:
#     print('Sum is right')
# print(s)

import time
import random

# start_time = time.time()
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# summ = int(input(f"{num1} + {num2} = "))
# print(summ)
# end_time = time.time()
# result = end_time - start_time
# print(round(result, 2))

# s = random.randint(1, 100)
# print(s)
# a = random.random()
# print(round(a, 2))

# b = random.randrange(1, 100)
# print(b)

# list_names = ['bob', 'jim', 'helga', 'john']
# one_name = random.choice(list_names)
# print(one_name)






















