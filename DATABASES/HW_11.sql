-- # 1.Подключиться к базе данных world
-- -- USE world;

-- # 2.Вывести население в каждой стране. Результат содержит два поля: CountryCode, sum(Population). 
-- #   Запрос по таблице city.
-- -- SELECT * FROM city;
-- -- SELECT * FROM country;

-- SELECT CountryCode, sum(Population) AS cnt
-- FROM city
-- GROUP BY CountryCode;

-- # 3.Изменить запрос выше так, чтобы выводились только страны с населением более 3 млн человек.

-- SELECT CountryCode, sum(Population) AS cnt
-- FROM city
-- GROUP BY CountryCode
-- HAVING cnt > 3000000;

-- /* ODER:
-- SELECT CountryCode
-- FROM (SELECT CountryCode, sum(Population) AS cnt
-- FROM city
-- GROUP BY CountryCode) AS new_city
-- WHERE cnt > 3000000;
-- */

-- # 4. Сколько всего записей в результате?

-- SELECT COUNT(*) AS cnt_entries
-- FROM (SELECT CountryCode, sum(Population) AS cnt_pop
-- FROM city
-- GROUP BY CountryCode
-- HAVING cnt_pop > 3000000) AS new_city;

-- # 5. Поменять запрос выше так, чтобы в результате вместо кода страны выводилось ее название.
-- #    Подсказка: нужен join таблиц city и country по полю CountryCode.

-- SELECT cntry.Name, sum(city.Population) AS cnt_pop
-- FROM city
-- INNER JOIN country AS cntry ON cntry.Code = city.CountryCode
-- GROUP BY CountryCode
-- HAVING cnt_pop > 3000000;



-- # 6.Вывести количество городов в каждой стране (CountryCode, amount of cities).
-- #.  Подсказка: запрос по таблице city и группировка по CountryCode.

-- SELECT CountryCode, COUNT(ID) AS amount_of_cities
-- FROM city
-- GROUP BY CountryCode
-- ORDER BY amount_of_cities DESC;


-- # 7.Поменять запрос так, чтобы вместо кодов стран, было названия стран. 

-- SELECT cntry.Name, amount_of_cities
-- FROM 
-- (SELECT CountryCode, COUNT(ID) AS amount_of_cities
-- FROM city
-- GROUP BY CountryCode ORDER BY amount_of_cities DESC) AS new_city
-- LEFT JOIN country AS cntry ON cntry.Code = new_city.CountryCode;

-- # 8.Поменять запрос так, чтобы выводилось среднее количество городов в странах. 
-- #   Подсказка: разделите задачу на несколько подзадач. 
-- #   Например, сначала вывести код страны и количество городов в каждой стране.  
-- #   Затем сделать join получившегося результата с запросом, где высчитывается среднее от количества городов. 
-- #   Потом добавить join, который добавит имена стран, вместо кода. 
-- #   Разобьем запросы на части:
-- #   1. Вывести код страны и количество городов в каждой стране.
-- #   2. Получить среднее количество городов в стране.
-- #   3. Объединить результаты с именами стран.

-- SELECT ROUND(AVG(amount_of_cities)) AS avg_cities
-- FROM (
-- SELECT COUNT(ID) AS amount_of_cities
-- FROM city
-- GROUP BY CountryCode
-- ) AS new_city;



