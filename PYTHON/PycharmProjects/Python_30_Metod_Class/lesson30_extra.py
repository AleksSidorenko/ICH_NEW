class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Синтаксис
        # return f"ClassName(arg1={self.attr1!r}, arg2={self.attr2!r})"
        return f"Point(x={self.x}, y={self.y})"  # Для отладки

    def __str__(self):
        return f"Coordinates: {self.x}, {self.y}"  # Для пользователей

    def _met(self):
        pass


p = Point(2, 3)
print(repr(p))
print(str(p))
print(p)


l = [p]
print(l)



# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'Cat(name={self.name}, age={self.age})'
#
#     def __repr__(self):
#         return f'Cat(name={self.name!r}, age={self.age!r})'
#
# c = Cat("White", 2)
# print(str(c))
# print(repr(c))
# new_cat = Cat(age=2, name='White')
# print(new_cat)
# print(repr(new_cat))

























