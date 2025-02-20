# Определите сумму всех элементов последовательности, завершающейся числом 0.
# Числа, следующие за первым нулем, учитывать не нужно.
# Числа считываем с клавиатуры с помощью input()
# num_sum = 0
# while True:
#     num = int(input('Enter a number: '))
#     num_sum += num
#     if num == 0:
#         break
# print(f"Сумма всех чисел равна {num_sum}")

# num_sum = 0
# line = ''
# while True:
#     num = int(input('Enter a number: '))
#     line = line + str(num) + ", "
#     num_sum += num
#     if num == 0:
#         break
# print(f"Сумма всех чисел {line} равна {num_sum}")

number = 123
total_summary = 0
while number > 0:
    digit = number % 10
    print(digit)
    total_summary += digit
    print(total_summary)
    number //= 10  # number = number // 10
    print(number)
print(f"Сумма цифр числа {number} равна: {total_summary}")


# Мнимая единица в Python
# imaginary_unit = 1j
# Пример использования мнимой единицы
# z = 3 + 4j  # Комплексное число 3 + 4i
# print(f"Мнимая единица: {imaginary_unit}")
# print(f"Комплексное число: {z}")
# print(f"Модуль комплексного числа: {abs(z)}")

# import math
# import math as m
# import decimal
from decimal import Decimal, getcontext
# price = Decimal(input('Enter price: '))
# quntity = Decimal(input('Enter quantity: '))
# total = price * quntity
# total = total.quantize(Decimal('0.01'))
# print(f'The total price is {total}')

# getcontext().prec = 2
# num1 = Decimal('1')
# num2 = Decimal('7')
# n = num1 / num2
# print(n)


# from decimal import Decimal
#
# # Создание Decimal из строки
# num_str = '3.141592653589793'
# decimal_num = Decimal(num_str)
#
# # Вывод значения
# print(decimal_num)


















