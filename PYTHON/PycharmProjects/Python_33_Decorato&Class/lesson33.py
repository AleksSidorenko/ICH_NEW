# class Person:
#     name = "person"
#
#     def __init__(self):
#         self.name = "name"
#         print(Person.name)
#
#     @classmethod
#     def method(cls):
#         print("method", cls.name)
#
#     def obj_method(self):
#         print("method", self.name)
#
#     @staticmethod
#     def static_method():
#         print("Hello")
#
#     def static_method2(self):
#         print("Hi")
#
# # p = Person()
# # p.method()
# Person.method()
# # Person.obj_method()
# Person.static_method()


# class Person:
#     age = 25
#     def printAge(cls):
#         print('The age is:', cls.age)
# Person.printAge = classmethod(Person.printAge)
# Person.printAge()


class Shape:
    name = "shape"

    def area(self):
        print("Method 'area' must be implemented")
        # raise NotImplementedError("Method 'area' must be implemented")


#
# class Rectangle(Shape):
#     name = "rect"
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle(Shape):
#     # name = "circ"
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     # def area(self):
#     #     return 3.14 * self.radius ** 2
#
#
# shapes = [Rectangle(5, 10), Circle(3)]
# for shape in shapes:
#     print(shape.area())
#     print(shape.name)

#
# class A:
#     pass
#     # def method(self):
#     #     print("A method")
#
#
# # class C:
# class C(A):
#     def method(self):
#         print("C method")
#
#
# class B(A):
#     pass
#     # def method(self):
#     #     print("B method")
#
#
# class D(B, C):
#     pass
#
#
# obj = D()
# obj.method()
# print(D.__mro__)


#
# class CustomException(Exception):
#     pass
#
#
# try:
#     raise CustomException("This is a custom exception")
# except CustomException as e:
#     print(e)  # This is a custom exception

#
# class MyBaseClass:
#     def __init__(self, x):
#         self.x = x
#
#
# class MySubClass(MyBaseClass):
#     def __init__(self, x, y):
#         super().__init__(x)
#         self.y = y
#
#
# obj = MySubClass(1, 2)
# print(obj.x)  # 1
# print(obj.y)  # 2


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print("The animal makes a sound")
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         print(super())
#
#     def make_sound(self):
#         print(super())
#         super().make_sound()
#
#     print("The dog barks")
#
#
# my_dog = Dog("Buddy")
# my_dog.make_sound()




from abc import ABC, abstractmethod

# class BaseShape:
class BaseShape(ABC):
    @abstractmethod
    def area(self):
        pass

    def area2(self):
        pass

class Circle(BaseShape):
    def __init__(self, radius):
        self.radius = radius
        print("Inside Circle __init__")

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(BaseShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# circle = Circle(5)
# rectangle = Rectangle(4, 6)
#
# print(circle.area())
# print(rectangle.area())


# print(BaseShape())
print(Circle(5))
print(Rectangle(3, 4))

