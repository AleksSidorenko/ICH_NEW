### Когда полезно `dict.get()`  

#### 1. **Безопасное получение значения с подстановкой по умолчанию**  
_Ситуация:_ Проверка баланса пользователя в интернет-магазине, если данных нет — считать баланс нулевым.  
```python
user_balances = {'alice': 100, 'bob': 50}
balance = user_balances.get('charlie', 0)  # Charlie еще не делал покупок
```
→ Избегает `KeyError`, удобно при обработке данных.  

#### 2. **Поиск значения в конфигурации с дефолтными настройками**  
_Ситуация:_ Если в конфиге нет параметра, использовать стандартное значение.  
```python
config = {'theme': 'dark'}
theme = config.get('theme', 'light')  # Вернет 'dark'
timeout = config.get('timeout', 30)  # Вернет 30 (по умолчанию)
```
→ Удобно при работе с пользовательскими настройками.  

#### 3. **Подсчет количества встречаемых элементов**  
_Ситуация:_ Подсчет количества проданных товаров.  
```python
sales = {}
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

for item in items:
    sales[item] = sales.get(item, 0) + 1

print(sales)  # {'apple': 3, 'banana': 2, 'orange': 1}
```
→ Позволяет избежать лишних `if` при проверке существования ключа.  
---

### Когда полезно `dict.setdefault()`  

#### 1. **Группировка элементов по ключу**  
_Ситуация:_ Распределение студентов по курсам.  
```python
courses = {}
students = [('Math', 'Alice'), ('Math', 'Bob'), ('Physics', 'Charlie')]

for course, student in students:
    courses.setdefault(course, []).append(student)

print(courses)  # {'Math': ['Alice', 'Bob'], 'Physics': ['Charlie']}
```
→ Упрощает логику без дополнительной проверки наличия ключа.  

