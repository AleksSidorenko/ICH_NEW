/* USE hr; -- Вывести зарплату сотрудника с именем ‘Lex’ и фамилией ‘De Haan'
SELECT salary
FROM employees WHERE first_name = 'Lex' AND last_name = 'De Haan';

-- Вывести всех сотрудников с job_id ‘FI_ACCOUNT’ и зарабатывающих меньше 8000

-- Вывести сотрудников, у которых в фамилии в середине слова встречаются сочетания ‘kk’ или ‘ll’

-- Вывести сотрудников с commission_pct NULL
SELECT *
FROM employees WHERE commission_pct is NULL;

-- Вывести всех сотрудников кроме тех, кто работает в департаментах 80 и 110
SELECT *
FROM employees WHERE department_id NOT IN(80, 110);

-- Вывести сотрудников зарабатывающих от 5000 до 7000 (включая концы)
SElECT *
FROM employees WHERE salary BETWEEN 5000 AND 7000;
*/

-- Выведите содержимое таблиц city и country. Сколько записей в каждой?
USE world;
SELECT *
FROM city, country;

-- Введите команды describe city; и describe country;
 SELECT *
 FROM city, country;
 describe city;
 describe country;

-- Выведите все страны Азии (Asia). Сколько их в таблице? 
SELECT *
FROM country
WHERE Continent = 'ASIA'
-- Выведите тот же результат, но с помощью команды where Continent in (‘Asia’)
SELECT *
FROM country
WHERE Continent in('Asia');

-- Выведите результат из двух столбцов: Name, LocalName.
SELECT Name, LocalName
FROM country
WHERE Continent in ('Asia');
-- Выведите страны с населением более 1 млрд человек.
SELECT *
FROM country WHERE Population > 1000000000;

-- Выведите все города Индии. 
Подсказка: у города есть поле CountryCode со значением ‘IND’ для индии.
SELECT *
FROM city WHERE CountryCode = 'IND';

-- Выведите все города с названием на ‘A’
SELECT *
FROM city -- WHERE Name LIKE 'A%';
ORDER BY NAME ~DESC

-- Выведите 5 самых населенных городов. Подсказка: вывести все,
--  отсортировать по Population в порядке убывания по населению 
-- и с помощью limit 5 оставить только 5 самых больших.
SELECT *
FROM city
ORDER BY Population DESC
-- LIMIT 5;
LIMIT 2, 5; -- или LIMIT 5 OFFSET 2;

-- На скольки языках говорят в Индии?
SELECT *
FROM world.countrylanguage
WHERE CountryCode = 'IND' AND IsOfficial = 'T';

-- 








