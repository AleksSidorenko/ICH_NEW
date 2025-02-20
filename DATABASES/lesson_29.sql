-- USE airport;
# Выведите количество лайнеров в каждом году.
# Выведите количество лайнеров в каждом году с годами, 
# где количеством лайнеров больше 1.
SELECT * FROM airliners;
SELECT * FROM clients;
SELECT * FROM tickets;
SELECT * FROM trips;
/*
SELECT production_year, COUNT(id) AS cnt
FROM airliners
GROUP BY production_year
HAVING cnt > 1
*/

# Выведите список client_id, amount_of_tickets (таблица tickets), 
# который содержит айди клиентов и количество билетов у каждого. 
# Выведите только тех клиентов, у которых больше 2 билетов.
/*
SELECT client_id, COUNT(id) AS amount_of_tickets
FROM tickets
GROUP BY client_id
HAVING amount_of_tickets > 2;

SELECT cli.name, COUNT(tic.id) AS amount_of_tickets
FROM tickets AS tic
INNER JOIN clients AS cli ON cli.id = tic.client_id
GROUP BY client_id
HAVING amount_of_tickets > 2
*/
# Выведите среднюю стоимость билетов в каждом сервисном классе.
/*
SELECT service_class, ROUND(AVG(price)) AS avg_pr
FROM tickets
GROUP BY service_class
HAVING avg_pr > (
SELECT AVG(avg_pr)
FROM
(SELECT service_class, ROUND(AVG(price)) AS avg_pr
FROM tickets
GROUP BY service_class) AS a);
*/

# Решить аналогичную задачу, но оставив сервисные классы 
# со средней стоимостью выше средней стоимости по всем билетам. 
# Объединить результаты двух запросов, для сравнения в одну выборку. 
# (не забыть указать номер задания для каждой строки)
/*
SELECT service_class, ROUND(AVG(price)) AS avg_pr
FROM tickets
GROUP BY service_class
HAVING avg_pr > (
SELECT AVG(avg_pr)
FROM
(SELECT AVG(price) AS avg_pr
FROM tickets
GROUP BY service_class) AS a);

SELECT AVG(price) AS avg_pri
FROM tickets;


SELECT service_class, ROUND(AVG(price)) AS avg_pr, 2 AS num
FROM tickets
GROUP BY service_class
HAVING avg_pr > (
SELECT AVG(price) AS avg_pri
FROM tickets)
UNION ALL
SELECT service_class, ROUND(AVG(price)) AS avg_pr, 1 AS num
FROM tickets
GROUP BY service_class
HAVING avg_pr > (
SELECT AVG(avg_pr)
FROM
(SELECT AVG(price) AS avg_pr
FROM tickets
GROUP BY service_class) AS a);
*/

# Выведите список самых популярных аэропортов отправления (trips departures).
/*
SELECT departure, COUNT(id) AS cnt
FROM trips
GROUP BY departure
ORDER BY cnt DESC
LIMIT 5
*/

# Вывести второй с конца по популярности аэропорт отправления 
# (для одинаковых значений произвести сортировку по алфавиту).
/*
SELECT departure, COUNT(id) AS cnt
FROM trips
GROUP BY departure
ORDER BY cnt, departure
LIMIT 1 OFFSET 1 # oder LIMIT 1, 1
*/

# Вывести самых молодых клиентов
/*
SELECT name, age
FROM clients
WHERE age = (SELECT MIN(age) FROM clients)
*/
 # Выведите номера билетов, имена клиентов, код аэропорта отправления и прибытия
/*
select tic.id, cl.name, tr.departure, tr.arrival from tickets tic
join clients cl on cl.id = tic.client_id
join trips tr on tr.id = tic.trip_id;
*/


















 


