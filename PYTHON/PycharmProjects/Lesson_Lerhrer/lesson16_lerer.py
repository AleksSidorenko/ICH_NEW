# numbers = (0, 1, 3, 14, 2, 7, 9, 8, 10)
# print(*numbers)

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [x**2 for x in numbers]
# print(squared_numbers)

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = []
# for num in numbers:
#     squared_numbers.append(num ** 2)
# print(numbers)
# print(squared_numbers)

#
# :
#     squared_numbers.append()

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# # print(6, 7, 8)
# # squared_numbers = [num ** 2 for num in numbers]
# squared_numbers = [print(num ** 2) for num in numbers]
# print(squared_numbers)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[1])
# print(matrix[1][2])
# print(matrix[1[2]])  # не валидно
# matrix_q = [
#     [1, 2, 3],
#     "python",
#     [7, 8, 9]
# ]
# matrix_q = None
# print(matrix_q[1[2]])  # не валидно
# print([4, 5, 6][2])

# numbers = (3, [5,3], 7, [[9,2],[1,2,3]])
# # print(len(numbers))
# for el in numbers:
#     print(el)

# stack = []
# stack.append(1) # Добавление элемента в стек
# stack.append(2)
# stack.append(3)
# top_element = stack.pop() # Извлечение верхнего элемента из стека
# print(top_element)
# print(stack)

# numbers = [0, 1, 3, 14, 2, 7, 9, 8, 10]
# new = [20, 30]
# numbers.append(new)
# print(numbers)
# new.pop()
# print(new)
# print(numbers)
# # [0, 1, 3, 14, 2, 7, 9, 8, 10]

# from collections import deque
# queue = deque()
# queue.append(1) # Добавление элемента в очередь
# queue.append(2)
# queue.append(3)
# first_element = queue.popleft() # Извлечение первого элемента из очереди
# print(first_element) # 1
# print(queue)
#
# my_list = [4, 2, 1, 3]
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)
#
# def say_hi(name, symbol="!"):
#     print(f"Hi, {name}{symbol}")
#
# say_hi([4, 2, 1, 3])
# say_hi("Tanya", "!!!")
# say_hi("Tanya", ".")

# a = ['бета', '"альфа"', 'дельта', 'Гамма']
# a.sort()
# print('Отсортированный список:', a)