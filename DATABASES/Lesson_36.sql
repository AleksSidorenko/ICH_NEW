-- Изменить предыдущий запрос так, 
-- чтобы выводился ранк каждой поездки в зависимости от количества билетов в ней.
-- SELECT * FROM airliners;
-- SELECT * FROM clients;
-- SELECT * FROM tickets;
-- SELECT * FROM trips;
/*
select trip_id, count(id), dense_rank() over(order by count(id) desc) 
from tickets
group by trip_id
*/
-- Вывести поездку с самым большим количеством билетов
/*
SELECT *
FROM
(select trip_id, count(id), dense_rank() over(order by count(id) desc) AS rang_tr
from tickets
group by trip_id) AS t
WHERE rang_tr = 1
-- c другим рангом
SELECT *
FROM
(select trip_id, count(id), rank() over(order by count(id) desc) AS rang_tr
from tickets
group by trip_id) AS t
-- WHERE rang_tr = 3

SELECT *
FROM
(select trip_id, count(id), dense_rank() over(order by count(id) desc) AS rang_tr
from tickets
group by trip_id) AS t
WHERE rang_tr in (1, 2, 3, 5) -- вывод несколько значений
*/
-- Вывести список билетов с именами пассажиров, а также названием модели авиалайнера.
/*
SELECT cl.name, t.id , t3.model_name
FROM tickets t
INNER JOIN clients cl ON t.client_id = cl.id
INNER JOIN trips t2 ON t.trip_id = t2.id
INNER JOIN airliners t3 ON t3.id = t2.airliner_id;
*/
-- Вывести дополнительный столбец с потраченной суммой на покупку билетов каждым клиентом
/*
SELECT ti.id, cl.name, air.model_name, pr.amount_price
FROM tickets AS ti
LEFT JOIN clients As cl ON ti.client_id = cl.id
LEFT JOIN trips AS tr ON ti.trip_id = tr.id
LEFT JOIN airliners AS air ON air.id = tr.airliner_id
LEFT JOIN (SELECT client_id, SUM(price) AS amount_price
FROM tickets
GROUP BY client_id) AS pr ON pr.client_id = ti.client_id 
ORDER BY cl.name
-- другой вариант
SELECT ti.id, cl.name, air.model_name, SUM(ti.price) OVER(PARTITION BY ti.client_id) AS amount_price
FROM tickets AS ti
LEFT JOIN clients As cl ON ti.client_id = cl.id
LEFT JOIN trips AS tr ON ti.trip_id = tr.id
LEFT JOIN airliners AS air ON air.id = tr.airliner_id 
ORDER BY cl.name
*/
-- Вывести среднее количество билетов у каждого клиента.
/*
select count(id) / count(distinct client_id) as avg_ticket
from tickets;
-- Option
select avg(cnt) 
from(
select client_id , count(id) as cnt
from tickets
group by client_id) t1 ;
*/
-- Для всех стран вывести население последующей по продолжительности жизни страны
/* -- Функция смещения
SELECT Name, Population, LifeExpectancy, LEAD(Population) OVER(ORDER BY LifeExpectancy DESC) AS pop_next
FROM country
*/














