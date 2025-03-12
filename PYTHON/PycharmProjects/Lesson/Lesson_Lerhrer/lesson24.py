# my_generator = (x ** x for x in range(7000))            # -- () --> ГЕНЕРАТОРНОЕ ВЫРАЖЕНИЕ -- Generator expression.
# # print(my_generator)
# my_list_generator = [x ** x for x in range(7000)]
# # print(my_list_generator)
#
# import sys
# print(sys.getsizeof(my_generator))
# print(sys.getsizeof(my_list_generator))


# def my_generator():
#     try:
#         yield 1
#         yield 2
#         yield 3
#     except ValueError:
#         yield None
#     except GeneratorExit:
#         # Код для очистки ресурсов
#         print("sfdsd")
#
# gen = my_generator()
# print(next(gen)) # Выводит 1
# gen.close()
# print("34234")
# print(next(gen))
# if next(gen) < 3:
#     print(gen.throw(ValueError("Enough")))
# gen.close()

# import time
#
# def read_logs(file_path):
#     """Генератор, который читает лог-файл построчно."""
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:
#             while True:
#                 line = f.readline()
#                 if not line:
#                     time.sleep(2)  # Ждём появления новых строк
#                     continue
#                 yield line.strip()
#     except GeneratorExit:
#         print("Закрываем генератор, освобождаем ресурсы.")
#
# # Создадим тестовый лог-файл
# file_path = "logs.txt"
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("Log 1\nLog 2\n")
#
# # Запускаем генератор
# gen = read_logs(file_path)
#
# # Читаем несколько строк из логов
# for _ in range(3):
#     print(next(gen))
#
# # Решаем остановить обработку логов
# gen.close()  # Вызывает GeneratorExit внутри генератора


# def my_generator(pattern=None):
#     if pattern is None:
#         pattern = ['>-<', '-*-', '>*<']
#     while True:
#         for i in pattern:
#             yield i
#
# gen = my_generator(['>---<', '-***-', '>***<'])
# for i in range(4):
#     print(gen.__next__())
# print("-")
# for i in range(4):
#     print(gen.__next__())

# def my_generator():
#     received_value = yield 1
#     yield received_value + 1
#     yield 3
# gen = my_generator()
# print(gen.__next__())
# print(gen.send(10))
# print(gen.__next__())

# def test():
#     s = 0
#     while True:
#         x = yield s
#         s += x
# t = test()
# print(next(t))
# print(t.send(111))
# print(t.send(123))

# def my_generator():
#     value = yield
#     if value > 0:
#         yield value * 2
#     else:
#         yield value * 3
# gen = my_generator()
# next(gen)
# print(gen.send(5)) # Выводит 10
# print(gen.send(-2)) # Выводит -6

def show_letters(some_str):
    yield from (letter for letter in some_str if letter.isalpha())
random_str = show_letters('A!sdf 09 _ w')
print(next(random_str))
print(next(random_str))