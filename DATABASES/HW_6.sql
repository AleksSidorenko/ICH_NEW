-- 1. Подключитесь к базе данных world (которая находится на удаленном сервере). 
-- USE world;

-- 2. Выведите список стран с языками, на которых в них говорят.
-- SELECT LocalName, Language
-- FROM country AS a_country
-- INNER JOIN countrylanguage AS a_lang ON a_country.Code = a_lang.CountryCode;

-- 3. Выведите список городов с их населением и названием стран
-- SELECT a_city.Name, a_city.Population, LocalName
-- FROM city AS a_city
-- INNER JOIN country AS a_country ON a_city.CountryCode = a_country.Code;

-- 4. Выведите список городов в South Africa
-- SELECT a_city.Name, LocalName
-- FROM city AS a_city
-- INNER JOIN country AS a_country ON a_city.CountryCode = a_country.Code AND a_country.LocalName in ('South Africa');

-- 5. Выведите список стран с названиями столиц. 
--    Подсказка: в таблице country есть поле Capital, которое содержит номер города из таблицы City.
-- SELECT LocalName, a_city.Name
-- FROM country AS a_country
-- INNER JOIN city AS a_city ON a_country.Capital = a_city.ID;

-- 6. Измените запрос 4 таким образом, чтобы выводилось население в столице.
-- SELECT LocalName, a_city.Name, a_city.Population
-- FROM city AS a_city
-- INNER JOIN country AS a_country ON a_country.Capital = a_city.ID AND a_country.LocalName = 'South Africa';

-- 7. Напишите запрос, который возвращает название столицы United States.
-- SELECT LocalName, a_city.Name
-- FROM country AS a_country
-- INNER JOIN city AS a_city ON a_country.Capital = a_city.ID AND a_country.LocalName = 'United States';

-- 8. Используя базу hr_data.sql, вывести имя, фамилию и город сотрудника.
-- USE hr;
-- SELECT a_emp.first_name, a_emp.last_name, a_loc.city
-- FROM employees AS a_emp
-- INNER JOIN departments AS a_dep ON a_emp.department_id = a_dep.department_id
-- LEFT JOIN locations AS a_loc ON a_loc.location_id = a_dep.location_id

-- 9. Используя базу hr_data.sql, вывести города и соответствующие городам страны.
-- SELECT a_loc.city, a_country.country_name
-- FROM locations AS a_loc
-- LEFT JOIN countries AS a_country ON a_country.country_id = a_loc.country_id










