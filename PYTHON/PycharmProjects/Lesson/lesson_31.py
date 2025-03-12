# Операции над списками Python
# x in l — true, если элемент x есть в списке l;
# x not in l — true, если элемент x отсутствует в l;
# l1 + l2 — объединение двух списков;
# l * n , n * l — копирует список n раз;
# len(l) — количество элементов в l;
# min(l) — наименьший элемент;
# max(l) — наибольший элемент;
# sum(l) — сумма чисел списка;
# for i in list() — перебирает элементы слева направо.
# Несколько полезных советов для преобразования списка в строку
# (или любого другого итерабельного, такого как tuple).
# mylist = ['spam', 'ham', 'eggs']
# print(', '.join(mylist)) # oder: print('\n'.join(mylist))
# Однако этот простой метод не работает, если список содержит не строчные объекты,
# такие как целые числа. Если вы просто хотите получить строку с разделителями-запятыми,
# вы можете использовать этот шаблон:
# list_of_ints = [80, 443, 8080, 8081] #
# print(str(list_of_ints).strip('[]'))
# oder: print(str(list_of_ints)[1:-1])
# oder:
# print(', '.join(map(str, list_of_ints)))
# print('\n'.join(map(str, list_of_ints)))

# nums = [1, 2, 3, 4, 5]
# odd_squares = [n*n for n in nums if n%2 == 1]
# print(odd_squares) # [1, 9, 25]

# people = [{
#   "first_name": "Василий",
#   "last_name": "Марков",
#   "birthday": "9/25/1984"
# }, {
#   "first_name": "Регина",
#   "last_name": "Павленко",
#   "birthday": "8/21/1995"
# }]
#
# birthdays = [
#   person[term]
#   for person in people
#   for term in person
#   if term == "birthday"
# ]
#
# print(birthdays)

# matrix = [[x for x in range(1, 4)] for y in range(1, 4)]
# print(matrix)










