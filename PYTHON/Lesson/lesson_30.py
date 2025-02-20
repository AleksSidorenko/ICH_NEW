numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers)
print(*numbers)

sq_num = [num ** 2 for num in numbers]
sq_num = [print(num ** 2) for num in numbers]
print(sq_num)