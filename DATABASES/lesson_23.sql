# Работа с базой airport
# Вывести все поездки (trips) с указанием названия airliner
/*
-- USE airport;

SELECT * FROM trips;
SELECT * FROM airliners;

SELECT air.model_name, tr.id, tr.trip_code, tr.status FROM trips AS tr
LEFT JOIN airliners AS air ON air.id = tr.airliner_id
*/
# Вывести все билеты, с указанием имени клиента
/*
SELECT * FROM tickets;
SELECT * FROM clients;

SELECT cl.name, tic.id, tic.service_class FROM tickets AS tic
LEFT JOIN clients AS cl ON cl.id = tic.client_id
*/
# Вывести количество поездок по каждому airliner с указанием названия типа самолета
/*
SELECT * FROM trips;
SELECT * FROM airliners;

SELECT model_name, airliners.id, COUNT(trips.id) FROM trips
	LEFT JOIN airliners ON airliners.id = trips.airliner_id
GROUP BY airliners.id, model_name;
*/
# Вывести количество пассажиров для каждой поездки
/*
select count(client_id) , trip_id
from tickets
group by trip_id
*/
# Вывести средний возраст клиентв для каждого сервсиного класса..
/*
SELECT t2.service_class, ROUND(AVG(t1.age))
FROM clients t1
RIGHT JOIN tickets t2 ON t1.id = t2.client_id 
GROUP BY service_class
ORDER BY AVG(age) DESC
*/
# Посчитать количество билетов в каждой поездки и выведите список по убыванию количества билетов.
/*
SELECT COUNT(id), trip_id FROM tickets
GROUP BY trip_id
ORDER BY COUNT(id) DESC
*/
# Понять, является ли tirp_code в таблице trips идентификатором поездки.
# Выявить поле для связки с таблицей tickets
/*
SELECT *
FROM tickets;
SELECT *
FROM trips;

SELECT * -- tri.trip_code, tri.id, tic.trip_id
FROM trips AS tri
LEFT JOIN tickets AS tic ON tic.trip_id = tri.id

SELECT * -- tri.trip_code, tri.id, tic.trip_id
FROM trips AS tri
JOIN tickets AS tic ON tic.trip_id = tri.trip_code

SELECT id, trip_code -- Проверка уникальности двух полей
FROM trips
GROUP BY id, trip_code
*/
# Посчитать, какой процент поездок успешен и какой процент отменен.
/*
select count(if (status = "Arrived" or status like "Departed%", status, null)) as "успешные поездки",
count(if (status = "Cancelled", status, null)) as "отменённые поездки", count(status) as "общее количество поездок", 
round(count(if (status = "Arrived" or status like "Departed%", status, null)) / count(status) * 100) as "процент успешных поездок",
round(count(if (status = "Cancelled", status, null)) / count(status) * 100) as "процент отменённых поездок" from trips;

-- select count(status) from trips
-- where status = "Arrived" or status like "Departed%";
-- select count(status) from trips
-- where status = "Cancelled";
-- select count(status) from trips;
*/









