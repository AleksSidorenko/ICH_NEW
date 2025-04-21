# Создать класс Dog для представления собаки.
# Класс должен иметь атрибуты name (имя) и breed (порода), а также метод bark(),
# который выводит сообщение о том, что собака лает.
# Затем создать экземпляр класса Dog с заданным именем и породой и вызовите метод bark().
# Ожидаемый вывод: Шарик породы Дворняга лаял


# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def bark(self):
#         print(f"{self.name} породы {self.breed} лаял.")
#
#
# dog_1 = Dog("Шарик", "Дворняга")
# dog_2 = Dog("Красавчик", "Labrador")
# dog_1.bark()
# dog_2.bark()

# 1. Создать класс Car (машина) со следующими полями: model, year, color.
# 2. Создать 10 объектов этого класса, описывающих модели разных марок, лет и цветов.
# 3. Создать список из этих объектов.
# 4. Написать функцию, которая принимает список объектов класса Car и цвет и возвращает
# список машин этого цвета. Напечатать этот список, выводя название модели, год и цвет.
# Использовать filter и lambda функции.

# class Car:
#
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#
#
# car1 = Car(1, 2015, 'red')
# car2 = Car(2, 2015, 'blue')
# car3 = Car(3, 2015, 'green')
# car4 = Car(4, 2015, 'yellow')
# car5 = Car(5, 2015, 'red')
# car6 = Car(6, 2015, 'cyan')
# car7 = Car(7, 2015, 'magenta')
# car8 = Car(8, 2015, 'red')
# car9 = Car(9, 2015, 'white')
# car10 = Car(10, 2015, 'pink')
#
# car_list = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]
#
#
# def find_car_color(car_list, color):
#     car_list_color = []
#     for car in car_list:
#         if car.color == color:
#             car_list_color.append(car)
#     return car_list_color
#
# result = find_car_color(car_list, 'red')
# for car in result:
#     print(car.model, ', ',  car.year, ', ', car.color)
#
