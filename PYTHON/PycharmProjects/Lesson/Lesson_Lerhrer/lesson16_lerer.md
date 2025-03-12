## List comprehension. Стек и очередь

- [List comprehension](#List-comprehension)
- [List comprehension с условием if](#List-comprehension-с-условием-if)
- [List comprehension с условием if-else](#List-comprehension-с-условием-if-else)
- [List comprehension с вложенным циклом](#List-comprehension-с-вложенным-циклом)
- [Стек и очередь](#Стек-и-очередь)
- [Устойчивость сортировки](#Устойчивость-сортировки)


## List comprehension

```python
new_list = [expression for item in iterable]
```

- **`expression`** — выражение (функция, операция или просто элемент), которое будет применено к каждому элементу.
Результат будет добавлен в новый список.
- **`item`** — переменная для каждого элемента в итерируемом объекте.
- **`iterable`** — итерируемый объект, по которому выполняется перебор.


**Пример: Создание списка квадратов чисел**

```python
numbers = [1, 4, 6, 7, 9]
# Возведение каждого элемента numbers в квадрат
squares = [n ** 2 for n in numbers]
print(squares)
print(numbers)  # Изначальный список останется без изменений
```


### List comprehension и цикл `for`

**Пример 1: Вычисление квадратов чисел**
```python
# Создание аналогичного списка с помощью List comprehension
# List comprehension
print([x ** 2 for x in range(5)])


# Эквивалент с циклом for
squares = []
for x in range(5):
    squares.append(x ** 2)

print(squares)
```

**Пример 2: Преобразование слов в верхний регистр**
```python
# List comprehension
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]

print(uppercase_words)


# Эквивалент с циклом for
words = ["hello", "world", "python"]
uppercase_words = []
for word in words:
    uppercase_words.append(word.upper())
    
print(uppercase_words)
```

## List comprehension с условием `if`

```python
new_list = [expression for item in iterable if condition]
```

- **`expression`** — выражение (функция, операция или просто элемент), которое будет применено к каждому элементу.
Результат будет добавлен в новый список.
- **`item`** — переменная для каждого элемента в итерируемом объекте.
- **`iterable`** — итерируемый объект, по которому выполняется перебор.
- **`condition`** — условие, по которому элементы отбираются.


**Пример 1: Выбор только чётных чисел**
```python
# List comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# Эквивалент с циклом for
even_numbers = []
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers) 
```

**Пример 2: Выбор слов, содержащих букву 'a'**
```python
# List comprehension
words = ["apple", "banana", "cherry", "date"]
words_with_a = [word for word in words if 'a' in word]
print(words_with_a)

# Эквивалент с циклом for
words = ["apple", "banana", "cherry", "date"]
words_with_a = []
for word in words:
    if 'a' in word:
        words_with_a.append(word)

print(words_with_a)
```


## List comprehension с условием `if-else`

```python
new_list = [expression_if_true if condition else expression_if_false for item in iterable]
```

- **`expression`** — выражение (функция, операция или просто элемент), которое будет применено к каждому элементу.
Результат будет добавлен в новый список.
- **`item`** — переменная для каждого элемента в итерируемом объекте.
- **`iterable`** — итерируемый объект, по которому выполняется перебор.
- **`condition`** — условие для проверки.
- **`expression_if_true`** — выражение, добавляемое в список, если условие истинно.
- **`expression_if_false`** — выражение, добавляемое в список, если условие ложно.


**Пример 1: Замена нечётных чисел на -1**
```python
# List comprehension
numbers = [2, 7, 5, 4, 1, 1, 7, 8]
modified_list = [x if x % 2 == 0 else -1 for x in numbers]

print(modified_list)


# Эквивалент с циклом for
numbers = [2, 7, 5, 4, 1, 1, 7, 8]
modified_list = []
for x in numbers:
    if x % 2 == 0:
        modified_list.append(x)
    else:
        modified_list.append(-1)

print(modified_list)
```


**Пример 2: Преобразование коротких слов в верхний регистр**
```python
# List comprehension
words = ["cat", "elephant", "dog", "bird"]
modified_words = [word if len(word) > 3 else word.capitalize() for word in words]

print(modified_words) 

# Эквивалент с циклом for
words = ["cat", "elephant", "dog", "bird"]
modified_words = []
for word in words:
    if len(word) > 3:
        modified_words.append(word)
    else:
        modified_words.append(word.capitalize())

print(modified_words)
```


### List comprehension с вложенным условием `if-else`

**List comprehension** поддерживает вложенные условия, позволяя добавлять несколько уровней проверки в одном выражении.


#### Пример: Замена слов на основе условий

**Задача**: Если длина слова больше 5 символов, оставить его без изменений. 
Если длина слова от 3 до 5 символов, заменить слово на `'medium'`. Если длина слова меньше 3 символов, заменить его на `'short'`.

```python
# List comprehension
words = ["hi", "apple", "banana", "cat", "blueberry", "on"]
modified_words = [word if len(word) > 5 else ('medium' if len(word) >= 3 else 'short') for word in words]

print(modified_words)


# Эквивалент с циклом for
words = ["hi", "apple", "banana", "cat", "blueberry", "on"]
modified_words = []
for word in words:
    if len(word) > 5:
        modified_words.append(word)
    else:
        if len(word) >= 3:
            modified_words.append('medium')
        else:
            modified_words.append('short')

print(modified_words) 
```


## List comprehension с вложенным циклом

```python
new_list = [expression for item1 in iterable1 for item2 in iterable2]
```

- **`expression`** — выражение (функция, операция или просто элемент), которое будет применено к каждому элементу.
Результат будет добавлен в новый список.
- **`item1`**, **`item2`** — переменные для каждого элемента из итерируемых объектов.
- **`iterable1`**, **`iterable2`** — итерируемые объекты, по которым выполняется перебор.


### Примеры использования

**Пример 1: Создание списка пар чисел**

```python
# List comprehension
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs) 

# Эквивалент с циклом for
pairs = []
for x in range(3):
    for y in range(2):
        pairs.append((x, y))

print(pairs)
```

**Пример 2: Распаковка вложенных списков**

```python
# List comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]

print(flattened) 


# Эквивалент с циклом for
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)

print(flattened)
```


## Стек и очередь

#### Примеры использования стека:
- История браузера (возврат на предыдущие страницы).
- Операции отмены (Ctrl+Z) в текстовых редакторах.


#### Пример реализации стека в Python:
```python
stack = []

# Добавление элементов в стек
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# Удаление последних элементов из стека
print(stack.pop())
print(stack.pop()) 

# Текущий стек
print(stack)
```

#### Примеры использования очереди:
- Очередь задач в принтере.
- Обработка запросов в серверных системах.

Для очереди рекомендуется использовать `deque` из модуля `collections` для повышения производительности.

#### Пример реализации очереди в Python:
```python
from collections import deque

queue = deque()

# Добавление элементов в очередь
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Удаление первых элементов из очереди
print(queue.popleft())
print(queue.popleft())

# Текущая очередь
print(queue)
```


## Устойчивость сортировки

```python
words = ["orange", "mango", "apple", "banana", "kiwi", "cherry"]
```

Если мы используем устойчивый алгоритм сортировки, слова с одинаковой длиной сохранят свой исходный порядок:

```python
# Сортировка списка по длине строк
sorted_words = sorted(words, key=len)
for word in sorted_words:
    print(f"{len(word)}: {word}")
```
