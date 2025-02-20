print("Homework №1")
decimal_number_1 = int(input("Enter the first number: "))
decimal_number_2 = int(input("Enter the second number: "))
print(decimal_number_1 + decimal_number_2)
print(decimal_number_1 - decimal_number_2)
print(decimal_number_1 * decimal_number_2)
print(decimal_number_1 / decimal_number_2)
print(decimal_number_1 % decimal_number_2)
print(decimal_number_1 ** decimal_number_2)

print("Homework №2")
radius_circle = float(input("Enter the radius of the circle: "))
pi = 3.14
circumferens = 2 * pi * radius_circle
area_circle = pi * radius_circle ** 2
print(f'The circumference:  {circumferens}')
print(f'The area of the circle: {area_circle}')

print("Homework №3")
print("Enter the coordinates of the first point (x1, y1)")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Enter the coordinates of the sekond point (x2, y2)")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
dinstanse = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f'Distance between points: {dinstanse}')
