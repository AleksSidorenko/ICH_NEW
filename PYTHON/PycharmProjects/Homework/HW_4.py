# print("-------- Homework №4 ---------")
# print("1. Даны формулы: ¬((A ∨ B) ∧ (C ∨ D)) и ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)). "
#       "Используя закон Де Моргана, докажите, что эти формулы эквивалентны.")
# a = 1
# b = 2
# c = 3
# d = 4
# check_formula_1 = not((a or b) and (c or d))
# check_formula_2 = ((not a and not b) or (not c and not d))
# rezult = check_formula_1 == check_formula_2
# print(rezult)

# print("2. Напишите программу, которая запрашивает у пользователя два логических значения (True или False)"
#     "и выводит результаты следующих логических операций:")
#
log_val_1 = input("Введите первое логическое значение (True или False): ") == 'True'
log_val_2 = input("Введите второе логическое значение (True или False): ") == 'True'
print(f'Результат логического И: {log_val_1 & log_val_2}.')
print(f'Результат логического ИЛИ: {log_val_1 | log_val_2}.')
print(f'Результат логического НЕ (для первого значения): {not log_val_1}')
print(f'Результат логического НЕ (для второго значения): {not log_val_2}')
print(f'Результат сравнения на равенство: {log_val_1 == log_val_2}')
print(f'Результат сравнения на неравенство: {log_val_1 != log_val_2}')
