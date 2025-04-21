# class Car:
#     def __init__(self, make, model, color="Black"):
#         self.make = make
#         self.model = model
#         self.color = color
#
#     # # Инит может быть только один
#     # def __init__(self, make='Ferrari', model='F430'):
#     #     self.make = make
#     #     self.model = model
#     #
#     # # Инит может быть только один
#     # def __init__(self, num, make='BMW', model='X5'):
#     #     self.make = make
#     #     self.model = model
#
#     @classmethod
#     def create_sport_car_Ferrari(cls):
#         return cls(make='Ferrari', model='F430')
#
#     @classmethod
#     def create_sport_car_BMW(cls, color):
#         return cls(color=color, make='BMW', model='F30')
#
# # Создаем спортивный автомобиль с использованием классового метода
# car = Car('Ferrari', 'A400')
# sports_car = Car.create_sport_car_Ferrari()
# print(sports_car.color)
# sports_car2 = Car.create_sport_car_BMW(color='Yellow')
# print(sports_car.make)
# print(sports_car.model)
# print(sports_car2.make)
# print(sports_car2.model)
# print(sports_car2.color)


class Singleton:
    _instance = None  # Хранит единственный экземпляр

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Создание нового объекта
        return cls._instance

    def __init__(self, value):
        self.value = value

# Проверка Singleton
obj1 = Singleton("Первый объект")
obj2 = Singleton("Второй объект")

print(obj1.value)
print(obj2.value)
print(obj1 is obj2)  # Выведет: True (один и тот же объект)
print(id(obj1))  # Выведет: True (один и тот же объект)
print(id(obj2))  # Выведет: True (один и тот же объект)






