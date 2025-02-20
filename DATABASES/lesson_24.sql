# Вывести топ клиентов (по clients_id) которые делали наибольшее количество успешных поездок.
-- USE airport;
SELECT * FROM clients;
SELECT * FROM tickets;
SELECT * FROM trips;
SELECT * FROM airliners;
/*
SELECT t2.client_id, COUNT(t2.trip_id) AS cnt
FROM trips t1
INNER JOIN tickets t2 ON t1.id = t2.trip_id 
where status = "Arrived" or status like "Departed%"
GROUP BY t2.client_id
ORDER BY cnt DESC;
*/
# К предыдущему запросу добавить имена клиентов и оптимизировать запрос.
/*
SELECT t2.client_id, t3.name, COUNT(t2.trip_id) AS cnt
FROM trips t1
INNER JOIN tickets t2 ON t1.id = t2.trip_id AND (status = "Arrived" or status like "Departed%")
LEFT JOIN clients t3 ON t3.id = t2.client_id
GROUP BY t2.client_id
ORDER BY cnt DESC;
*/
# Сделать группировку по сервис классу которым пользовались клиенты. 
# В итоге выведите количество клиентов в каждом классе.
/*
SELECT tic.service_class, COUNT(tic.client_id) AS cnt, COUNT(tr.status) FROM tickets AS tic
LEFT JOIN trips AS tr ON tic.trip_id = tr.id AND (status = "Arrived" or status like "Departed%")
GROUP BY tic.service_class

# Option 2
select count(client_id), service_class, count(IF(status = "Arrived" or status like "Departed%", status, NULL))
from tickets t1
left join trips t2 on t1.trip_id = t2.id -- and (status = "Arrived" or status like "Departed%")
group by service_class
*/
# Повторить прошлый запрос, но теперь с условием - если клиент пользовался несколькими классами, 
# то его нужно вывести в новую группу “Мульти”
/*
SELECT t1.id, t1.name, IF(COUNT(DISTINCT service_class) > 1, 'multi', t2.service_class) service_class_new
-- CASE WHEN COUNT(DISTINCT service_class) > 1 THEN 'multi' ELSE t2.service_class END service_class_new
FROM clients t1
RIGHT JOIN tickets t2 ON t2.client_id = t1.id
GROUP BY t1.id
*/
# Подсчитать количество клиентов, которые пользовались только одним сервис классом, 
# и тех, кто пользовался несколькими.
/*
SELECT  COUNT(IF(service_class_new = 'Multi', 1, NULL)) AS service_class_multi, 
		COUNT(IF(service_class_new <> 'Multi', 1, NULL)) AS service_class_1
FROM (SELECT name, 
	IF (COUNT(DISTINCT service_class) > 1, 'Multi', service_class) AS service_class_new
FROM clients
	RIGHT JOIN tickets  ON tickets.client_id = clients.id
GROUP BY client_id) AS t1;
# Option 2
SELECT SUM(if(count_class>=2, 1, 0)) AS multi_class, 
SUM(if(count_class>=2, 0, 1)) AS one_class,
COUNT(*)-SUM(if(count_class>=2, 1, 0)) AS one_class2 -- аналог через разницу.
FROM (SELECT COUNT(distinct service_class) AS count_class
FROM tickets
GROUP BY client_id) sum_cl;
*/














