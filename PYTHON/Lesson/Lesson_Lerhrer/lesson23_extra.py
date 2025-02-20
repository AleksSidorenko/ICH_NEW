# # return в генераторе
# def my_generator():
#     yield 1
#     yield 2
#     return "End"
#
# gen = my_generator()
# print(next(gen))  # 1
# print(next(gen))  # 2
# try:
#     print(next(gen))  # StopIteration: End
# except StopIteration as e:
#     print(e.value)  # End
#
#
# # return в генераторе
# def process_data(data):
#     for i in data:
#         if i == "STOP":
#             return "Processing stopped"  # Завершает генератор
#         yield i
#
# gen = process_data(["a", "b", "c", "STOP", "d"])
# for item in gen:
#     print(item)



# def show_letters(some_str):
#     for symbol in some_str:
#         if symbol.isalpha():
#             yield symbol
#
# my_generator = show_letters("hff8e2938ec82r92c")
# for i in my_generator:
#     print(i)

# def show_letters(some_str):
#     yield from (letter for letter in some_str if letter.isalpha())
#
# gen = show_letters("python")
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())


# def my_generator(pattern=None):
#     if pattern is None:
#         pattern = ['>-<', '-*-', '>*<']
#     while True:
#         for i in pattern:
#             yield i
#
# gen = my_generator(['>---<', '-***-', '>***<'])
# for i in range(7):
#     print(gen.__next__())


