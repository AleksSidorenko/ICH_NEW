# Вывести список сервисных классов со средней стоимостью билета в каждом классе.
-- SELECT * FROM airliners;
-- SELECT * FROM tickets;
/*
SELECT service_class, ROUND(AVG(price), 2) AS avg_price
FROM tickets
GROUP BY service_class
*/
# Вывести список сервисных классов со средней ценой в каждом классе 
# и ранком каждого класса в зависимости от средней цены в сервисном классе.
/*
SELECT service_class, ROUND(AVG(price), 2) AS avg_price, RANK() OVER(ORDER BY ROUND(AVG(price), 2) DESC)
FROM tickets
GROUP BY service_class
*/
# Вывести количество билетов для каждой поездки.
/*
SELECT trip_id, COUNT(id) AS cnt_price
FROM tickets
GROUP BY trip_id
ORDER BY cnt_price DESC
*/
# Вывести топ 2 поездок (trips) по их средней стоимости билетов.
/*
SELECT *
FROM
(SELECT trip_id, ROUND(AVG(price),2) AS avg_price, RANK() OVER(ORDER BY ROUND(AVG(price),2) DESC) AS rang
FROM tickets
GROUP BY trip_id) AS t
WHERE rang < 3
*/
# для каждого самолета подсчитать среднюю стоимость билета, добавить номера строк нашей выборки
/*
SELECT air.model_name, ROUND(AVG(tick.price),2) AS avg_air_amount, row_number() OVER(ORDER BY AVG(tick.price) DESC) AS amount_rank 
FROM airliners AS air
LEFT JOIN trips AS tr ON tr.airliner_id = air.id
JOIN tickets AS tick ON tick.trip_id = tr.id
GROUP BY air.model_name
*/
# Разбить все страны на 3 группы по средней продолжительности жизни, 
# при этом указать количество городов в каждой стране, где это возможно.
-- SELECT * FROM city;
-- SELECT * FROM country;
/*
SELECT Name, LifeExpectancy, NTILE(3) OVER(ORDER BY LifeExpectancy DESC), amount_city    
FROM world.country AS con
    LEFT JOIN (SELECT CountryCode, COUNT(id) AS amount_city
                FROM world.city
                GROUP BY CountryCode) AS amount_city ON amount_city.CountryCode = con.Code;
*/



















