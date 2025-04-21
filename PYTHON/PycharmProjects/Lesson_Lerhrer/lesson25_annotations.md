## Аннотации типов

### **1. Аннотация целых чисел (`int`)**
```python
def factorial(n: int) -> int:
    """Возвращает факториал числа."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### **2. Аннотация чисел с плавающей точкой (`float`)**
```python
def convert_to_celsius(fahrenheit: float) -> float:
    """Конвертирует температуру из градусов Фаренгейта в Цельсий."""
    return (fahrenheit - 32) * 5 / 9
```

### **3. Аннотация строк (`str`)**
```python
def greet(name: str) -> str:
    """Возвращает приветственное сообщение."""
    return f"Hello, {name}!"
```

### **4. Аннотация логических значений (`bool`)**
```python
def is_even(number: int) -> bool:
    """Определяет, является ли число чётным."""
    return number % 2 == 0
```

### **5. Аннотация `None` (функция без возврата)**
```python
def log_message(message: str) -> None:
    """Выводит сообщение в консоль, но не возвращает значения."""
    print(f"LOG: {message}")
```


## Аннотации для структур данных

В Python 3.9+ можно аннотировать **списки, кортежи, множества и словари** просто указывая встроенные типы. 
Однако важно понимать, **как именно указывать тип содержимого** и какие особенности у разных структур.


### **1. Списки (`list`)**
**Синтаксис:** `list[element_type]`  
- **В скобках указывается тип элементов внутри списка.**
- **Рекомендуется** указывать тип содержимого.

#### **Пример:**
```python
def process_numbers(numbers: list[int]) -> list[int]:
   # Список чисел
   return [n ** 2 for n in numbers]
```

### **2. Кортежи (`tuple`)**
**Синтаксис:**  
- Если кортеж содержит фиксированное число элементов: `tuple[type1, type2]`
- Если длина кортежа **не фиксирована**: `tuple[element_type, ...]`

#### **Примеры:**
```python
def get_info() -> tuple[str, float]:
   # Первый элемент str, второй элемент float
    return "Bob", 4.91

def variable_tuple() -> tuple[int, ...]:
   # Кортеж произвольной длины, но только целые числа
    return 5, 8, 2
```

### **3. Множества (`set`)**
**Синтаксис:** `set[element_type]`  
- **В скобках указывается тип всех элементов множества.**
- **Рекомендуется** указывать тип содержимого.

#### **Пример:**
```python
def unique_chars(text: str) -> set[str]:
   # Множество уникальных символов
    return set(text)
```

### **4. Замороженные множества (`frozenset`)**
**Синтаксис:** `frozenset[element_type]`  
- **Работает аналогично `set`, но создаёт неизменяемое множество.**
- **Рекомендуется** указывать тип содержимого.

#### **Пример:**
```python
def frozen_example() -> frozenset[int]:
   # Множество уникальных чисел
    return frozenset([1, 2, 3])
```

### **5. Словари (`dict`)**
**Синтаксис:** `dict[key_type, value_type]`  
- **В скобках указываются типы ключей и значений.**
- **Рекомендуется** указывать типы содержимого.

#### **Пример:**
```python
def count_words(text: str) -> dict[str, int]:
    """Принимает строку и возвращает словарь с подсчётом каждого слова."""
    words = text.split()
   # Словарь, где ключи — строки, значения — целые числа
    return {word: words.count(word) for word in words}
```


### Коллекции без указания типов

#### **Пример:**
```python
# Тип элементов не указан
def process_data(data: list) -> list:  
    return [d for d in data if d]

# Элементы должны быть числами
def process_numbers(numbers: list[int]) -> list[int]:  
    return [n ** 2 for n in numbers]
```


### Аннотация в старых версиях

**В версиях Python до 3.9** для аннотации структур данных использовались **специальные классы из модуля `typing`**:  
- `List` вместо `list`
- `Tuple` вместо `tuple`
- `Set` вместо `set`
- `FrozenSet` вместо `frozenset`
- `Dict` вместо `dict`

#### **Пример различий в аннотациях:**
```python
# В Python 3.9+ (рекомендуется)
def process_numbers(numbers: list[int]) -> list[int]:
    return [n ** 2 for n in numbers]

# В Python <3.9 (старый стиль)
from typing import List

def process_numbers_old(numbers: List[int]) -> List[int]:
    return [n ** 2 for n in numbers]
```


## Аннотации Any, Union и Optional

### Any — любой тип

#### **Пример:**
```python
from typing import Any

def process_data(data: Any) -> str:
    """Принимает данные любого типа и возвращает строку с их представлением."""
    return f"Данные: {data}"

print(process_data(42)) 
print(process_data("Hello")) 
print(process_data([1, 2, 3])) 
```


### Union — несколько возможных типов

#### **Пример:**
```python
from typing import Union

def calculate(value: Union[int, float]) -> float:
    """Принимает число (целое или дробное) и возвращает его квадрат."""
    return value ** 2
print(calculate(5))
print(calculate(2.5)) 
```


### Optional — значение может быть `None`

#### **Пример:**
```python
from typing import Optional

def get_user_name(user_id: int) -> Optional[str]:
    """Возвращает имя пользователя или None, если пользователь не найден."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Может вернуть None

print(get_user_name(1)) 
print(get_user_name(3)) 
```


### Union с оператором `|`

В Python 3.10 появился более **краткий синтаксис** для аннотаций типов — вместо `Union` можно использовать оператор `|`.

#### **Пример:**
```python
def calculate(value: int | float) -> float:
    """Принимает число (целое или дробное) и возвращает его квадрат."""
    return value ** 2

print(calculate(5))
print(calculate(2.5))
```


### Аннотация Callable

**`Callable`** используется для аннотирования аргументов или возвращаемого значения, если параметр должен быть **функцией**.

#### **Пример:**
```python
from typing import Callable

def add(x: int, y: int) -> int:
    return x + y

def multiply(x: int, y: int) -> int:
    return x * y

def execute_function(func: Callable[[int, int], int], nums1: list[int], nums2: list[int]) -> list[int]:
    return [func(a, b) for a, b in zip(nums1, nums2)]

print(execute_function(add, [1, 2, 3], [4, 5, 6]))
print(execute_function(multiply, [1, 2, 3], [4, 5, 6]))
```

