# def summe(start=1, step=2, **kwargs):
#     while True:
#         yield start
#         start += step
#
# first_num = 5
# step_num = 3
# gen = summe(start=first_num, step=step_num)
# # gen = summe(start=1, step=2)
# for _ in range(10):
#     print(next(gen))
# print(next(gen))


# file = None
# try:
#     file = open('numbers.txt')
#     # print(file.read())
#     num1 = int(file.readline())
#     num2 = int(file.readline())
#     if num1 < 0 or num2 < 0:
#         raise ValueError("Число должно быть положительным.")
#     result = num1 / num2
#     print(result)
# except FileNotFoundError:
#     print("Ошибка: Файл не существует")
# except ZeroDivisionError:
#     print("Ошибка: На ноль делить нельзя")
# except ValueError as v:
#     print(v)
# finally:
#     if file:
#         file.close()
#
# print("continue")
# print(bool(None))
# print(bool(4))


######## Вариант номер 1 ######## ошибка
def summe():
    s = 5
    while True:
            x = yield s
            s += x
            if s >= 50:
                print("Happy End! ")
                break

gen = summe()
next(gen)

while True:
    your_num = int(input())
    if your_num <= 0:
        break
    print(f"Текущая сумма: {gen.send(your_num)}")



