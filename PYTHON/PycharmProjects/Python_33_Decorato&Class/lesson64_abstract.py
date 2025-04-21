# Практическое задание
# Добавить метод, котопый выводит сообщение "Class: <class_name>"
# Создать систему наследования для геометрических фигур: фигура, прямоугольник, квадрат,
# круг (можно добавить и другие плоские фигуры - например, параллелограмм, треугольник,
# прямоугольный треугольник).
# У всего определить площадь и периметр, а также __str__ (дополнительно можно добавить
# __repr__).
# Важно: где-то нужно переопределять методы, а площадь абстрактной фигуры не определен
import math
from abc import ABC, abstractmethod

class Figure(ABC):


    def class_name(self):
        return f"Class: {self.__class__.__name__}"


    @abstractmethod
    def perimeter(self):
        pass


    @abstractmethod
    def area(self):
        pass


class Rectangle(Figure):


    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return f"Rectangle width:{self.width}, height:{self.height}"


    def __repr__(self):
        return f"Rectangle (width={self.width}, height={self.height})"


    def perimeter(self):
        return 2 * (self.width + self.height)


    def area(self):
        return self.width * self.height


class Triangle(Figure):


    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimeter(self):
        return self.a + self.b + self.c


    def area(self):
        s = self.perimeter()/2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Circle(Figure):
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


    def perimeter(self):
        return self.pi * self.radius * 2


    def area(self):
        return self.pi * self.radius **2


figures_list = [Rectangle(4, 5), Triangle(6, 7, 8), Circle(9)]
for figure in figures_list:
    print(figure.class_name())
    print(figure.perimeter())
    print(figure.area())
    print(figure)

print(figures_list)