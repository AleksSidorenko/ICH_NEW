-- Вывести количество самолетов каждой модели.
SELECT * FROM airliners;
SELECT * FROM clients;
SELECT * FROM tickets;
SELECT * FROM trips;
/*
SELECT model_name, COUNT(id) AS cnt_air
FROM airliners
GROUP BY model_name;
*/
-- добавить столбец., в котором указано какой % самолетов выпущен именно этой модели от общего числа самолетов
/*
SELECT model_name, ROUND(COUNT(id) / SUM(COUNT(id)) OVER() * 100) AS '% from_total'
FROM airliners
GROUP BY model_name;
*/
-- Вывести количество самолетов по странам, а так же % от общего числа.
/*
SELECT country, COUNT(id) AS cnt_aer, ROUND(COUNT(id) / SUM(COUNT(id)) OVER() * 100) AS '% from_total'
FROM airliners
GROUP BY country;
*/
-- Вывести количество trips для каждого типа лайнера.
/*
SELECT air.model_name, COUNT(tr.id)
FROM trips tr
LEFT JOIN airliners air ON tr.airliner_id = air.id
GROUP BY air.model_name
*/
-- Вернуть количество поездок для каждого лайнера, у которого было более 5 поездок, 
-- а также оставить 5 записей, пропустив первые 3 по количеству поездок, а так же вывести его модель.
/*
SELECT COUNT(tr.id) AS cnt_tr, air.model_name, air.id
FROM trips AS tr
LEFT JOIN airliners AS air ON air.id = tr.airliner_id
GROUP BY air.id
HAVING cnt_tr > 5
ORDER BY cnt_tr DESC
-- LIMIT 5 OFFSET 3   -- УКАЗЫВАЕМ СКОЛЬКО ПРОПУСКАЕМ, СКОЛЬКО ОСТАВЛЯЕМ
LIMIT 3, 5   -- УКАЗЫВАЕМ СКОЛЬКО ПРОПУСКАЕМ, СКОЛЬКО ОСТАВЛЯЕМ (другой способ)
*/
-- Вывести id билетов, цену билета и среднюю стоимость билета (таблица tickets).
/*
SELECT id, price, ROUND(AVG(price) OVER()) AS avg_price
FROM tickets;

SELECT id, price, (SELECT ROUND(AVG(price)) FROM tickets AS avg_price)
FROM tickets;
*/
-- Вывести среднюю стоимость билета в каждом классе обслуживания (service_class).
/*
SELECT service_class, ROUND(AVG(price))
FROM tickets
GROUP BY service_class
*/
-- Сравнить стоимость каждого билета со средней стоимостью билетов в его классе обслуживания. 
-- Результат вывести в %.
/*
SELECT id, service_class, price, ROUND(AVG(price) OVER(PARTITION BY service_class)),
ROUND(price / ROUND(AVG(price) OVER(PARTITION BY service_class)) * 100) AS '% from_total'
FROM tickets
*/
-- Вывести список поездок (trips) по убыванию количество билетов для каждой поездки.
/*
SELECT trip_code, COUNT(id)
FROM trips
GROUP BY trip_code
ORDER BY COUNT(id) DESC;
*/















