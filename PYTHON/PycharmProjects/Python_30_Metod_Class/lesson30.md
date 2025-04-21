# Инкапсуляция

Инкапсуляция в объектно-ориентированном программировании (ООП) означает упаковку данных (полей) и методов, работающих с ними, внутри одного объекта и предоставление контроля над доступом к этим данным.

В Python существует три основных типа доступа к членам класса:

## 1. Публичный доступ (public):

Публичные члены класса (атрибуты и методы) доступны извне класса. К ним можно обращаться напрямую без ограничений.

Пример:
```python
class MyClass:
    def __init__(self, name):
        self.name = name  # Публичный атрибут

    def public_method(self):
        return f"Hello, {self.name}!"  # Публичный метод

obj = MyClass("John")
print(obj.name)
print(obj.public_method())
```



## 2. Защищенный доступ (protected):

Защищенный доступ (члены класса, начинающиеся с одного подчеркивания) в Python используется для того, чтобы обозначить, что эти члены не предназначены для использования извне класса, но к ним можно обращаться напрямую.

Пример:
```python
class MyClass:
    def __init__(self, protected_name, name):
        self._protected_variable = protected_name  # Защищенный атрибут
        self.name = name  # Публичный атрибут

    def _protected_method(self):
        return f"Hello, {self._protected_variable}!"  # Защищенный метод

obj = MyClass("Alice")
print(obj._protected_variable)
print(obj._protected_method())
```


Часто защищенные атрибуты и методы используются для внутренних реализаций класса. Это могут быть вспомогательные методы или переменные, которые не являются частью общего интерфейса класса.
```python
class Car:
    def __init__(self, make, model):
        self._make = make  # Защищенный атрибут
        self._model = model  # Защищенный атрибут

    def _start_engine(self):
        print(f"Engine of {self._make} {self._model} started")

    def drive(self):
        self._start_engine()
        print(f"{self._make} {self._model} is driving")

my_car = Car("Toyota", "Camry")
my_car.drive()
```


## 3. Приватный доступ:

Приватные члены класса в Python (члены, начинающиеся с двух подчеркиваний) предназначены для ограничения доступа к ним извне класса. Однако, следует отметить, что в Python приватность не является строгим ограничителем доступа, а скорее предостережением.
```python
class MyClass:
    def __init__(self, name):
        self.__private_variable = name  # Приватный атрибут

    def __private_method(self):
        return f"Hello, {self.__private_variable}!"  # Приватный метод

obj = MyClass("Bob")
# print(obj.__private_variable)      # Это вызовет ошибку
# print(obj.__private_method())       # Это вызовет ошибку
```

Обратите внимание, что в Python существует соглашение об именовании, которое регламентирует, какие члены следует считать публичными, защищенными и приватными. Однако, это всего лишь соглашение, и сам Python не делает строгого разделения на уровни доступа.

На самом деле сокрытие в Python не настоящее и доступ к атрибуту мы получить все же можем. Но для этого надо написать `Класс_или_объект._Класс__атрибут/метод`:
```python
class MyClass:
    def __init__(self, name):
        self.__private_variable = name  # Приватный атрибут

    def __private_method(self):
        return f"Hello, {self.__private_variable}!"  # Приватный метод

obj = MyClass("Bob")
print(obj._MyClass__private_variable)
print(obj._MyClass__private_method())
```

## Создание методов-геттеров и методов-сеттеров

Можно создать методы-геттеры и методы-сеттеры для доступа к приватным атрибутам. Эти методы позволяют читать и изменять значения атрибутов, предоставляя контроль над доступом.

```python
class MyClass:
    def __init__(self):
        self.__private_variable = 42  # Приватный атрибут

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, value):
        self.__private_variable = value

obj = MyClass()
print(obj.get_private_variable())
obj.set_private_variable(100)
print(obj.get_private_variable())
```

