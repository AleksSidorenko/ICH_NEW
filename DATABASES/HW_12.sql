# Работаем с базой world:
# 1. Вывести количество городов для каждой страны. 
# Результат должен содержать CountryCode, CityCount (количество городов в стране). 
# Поменяйте запрос с использованием джойнов так, чтобы выводилось название страны вместо CountryCode. 
-- SELECT * FROM city;
-- SELECT * FROM country;
/*
SELECT DISTINCT CountryCode, COUNT(ID) OVER(PARTITION BY CountryCode) AS CityCount
FROM city
ORDER BY CityCount DESC;
*/
/*
SELECT CountryCode, COUNT(ID) AS CityCount
FROM city
GROUP BY CountryCode
ORDER BY CityCount DESC;

SELECT Name, CityCount
FROM
(SELECT CountryCode, COUNT(ID) AS CityCount
FROM city
GROUP BY CountryCode
ORDER BY CityCount DESC) AS cnt_l
LEFT JOIN country AS coun ON coun.Code = cnt_l.CountryCode;
*/
# 2. Вывести список стран с продолжительностью жизни и средней продолжительностью жизни (для всех стран). 
#    (Name, продолжительность жизни, средняя продолжительность жизни)
/*
SELECT Name, LifeExpectancy, ROUND(AVG(LifeExpectancy) OVER()) AS avg_life
FROM country;
*/
# 3. Используя ранжирующие функции, вывести страны по убыванию продолжительности жизни.
#    (Name, продолжительность жизни, ранг)
/*
SELECT Name, LifeExpectancy, DENSE_RANK() OVER(ORDER BY LifeExpectancy DESC) AS rang_life
FROM country;
*/
# 4. Используя ранжирующие функции, вывести третью страну с самой высокой продолжительностью жизни. 
#    (учесть, что таких стран может быть несколько).

-- SELECT Name, LifeExpectancy, DENSE_RANK() OVER(ORDER BY LifeExpectancy DESC)
-- FROM country;
/*
SELECT Name, LifeExpectancy, rang_desc
FROM (SELECT Name, LifeExpectancy, DENSE_RANK() OVER(ORDER BY LifeExpectancy DESC) AS rang_desc
FROM country) AS red_country
WHERE rang_desc = 3
*/
