# Найти количество сотрудников у каждого менеджера. 
# Вывести manager_id и employees_cnt
-- SELECT * FROM employees;
-- SELECT * FROM departments;
/*
SELECT manager_id, COUNT(employee_id) 
FROM employees
GROUP BY manager_id;
*/
# Вывести Фамилию и Имя менеджера в предыдущей задаче.
/*
SELECT first_name, last_name, nq1.emp_cnt
FROM
    (SELECT manager_id, COUNT(employee_id) emp_cnt
    FROM employees
    GROUP BY manager_id
    ) nq1
JOIN employees emp ON nq1.manager_id = emp.employee_id;
*/
# Работаем с базой World. Выведите седьмой по густонаселенности город. 
# Подсказка: использовать функцию dense_rank() и оконные функции.
-- SELECT * FROM city;
/*
select *, dense_rank() over (order by Population desc) dr_pop_d from city;
select * from (select *, dense_rank() over (order by Population desc) dr_pop_d from city) t1
where dr_pop_d = 7;
*/
# Выведите название города, население и максимальное население для каждого города в странах
/*
SELECT CountryCode, Name, Population, MAX(Population) OVER(PARTITION BY CountryCode) AS city_pop
FROM city
*/
# Напишите запрос для определения разницы в продолжительности жизни между текущей страной 
# и страной с самой высокой продолжительностью жизни.
SELECT * FROM country;
/*
select Name, LifeExpectancy, max(LifeExpectancy) over() - LifeExpectancy
from country
*/
# Выполните ранжирование стран по средней численности населения городов 
# и вернем значение 0 для стран, где информации о населении городов нет.
/*
select co.Name, round(ifnull(avg(ci.Population), 0)) as avg_pop, dense_rank() over(order by(ifnull(avg(ci.Population), 0)) desc)
from country as co 
left join city as ci on ci.CountryCode = co.Code
group by co.Name;
*/
# На основании предыдущего запроса выведите топ 6 стран по средней численности населения 
# (Используйте LIMIT) и оконные функции
/*
select co.Name, round(ifnull(avg(ci.Population), 0)) as avg_pop, dense_rank() over(order by ifnull(avg(ci.Population), 0) desc)
from country as co 
left join city as ci on ci.CountryCode = co.Code
group by co.Name
LIMIT 6
*/
/*
SELECT * FROM
(select co.Name, round(ifnull(avg(ci.Population), 0)) as avg_pop, 
dense_rank() over(order by ifnull(avg(ci.Population), 0) desc) AS rang
from country as co 
left join city as ci on ci.CountryCode = co.Code
group by co.Name) AS t
WHERE rang < 7
*/
# Напишите запрос для определения доли населения города от общей численности 
# населения страны и проведите ранжирование городов в пределах каждой страны:
/*
SELECT Name, CountryCode, Population, SUM(Population) OVER(PARTITION BY CountryCode) AS pop_sum,
ROUND((Population / SUM(Population) OVER(PARTITION BY CountryCode) * 100), 2) AS tail,
DENSE_RANK() OVER(PARTITION BY CountryCode ORDER BY Population DESC)
FROM city
*/
# Написать SQL-запрос для выбора городов, занимающих первое место по населению в своих странах 
# и превышающих среднее население по всем городам.
/*
select Name, CountryCode, Population, avg(Population) over() as avg_pop, DENSE_RANK() OVER(PARTITION BY CountryCode ORDER BY Population DESC) as rank_pop
from city;

select * 
from (select Name, CountryCode, Population, avg(Population) over() as avg_pop, DENSE_RANK() OVER(PARTITION BY CountryCode ORDER BY Population DESC) as rank_pop
		from city) as t1
where t1.Population > avg_pop AND rank_pop = 1
*/
# Выведите страны, где количество городов больше 10
/*
select c.Name, count(ID) as cnt
from country as c
LEFT JOIN city ON c.Code = city.CountryCode
Group by c.Name
having cnt > 10
order by cnt desc
*/
# Выведите список форм правления (GovernmentForm) c количеством стран, 
# где есть эта форма правления.
/*
select GovernmentForm,count(Code) 
from country
group by GovernmentForm 
order by count(Code) DESC;
*/

# Выведите формы правления, которые есть в 10 и более странах.
/*
select GovernmentForm,count(Code) 
from country
group by GovernmentForm 
having count(Code) > 10 
order by count(Code) DESC;
*/
# Написать SQL-запрос для выбора городов, занимающих первое место по населению 
# в своих странах и превышающих среднее население по всем городам.
# решить без использования оконных функций.

# __ without WINDOWS __
/*
SELECT CountryCode, Name, Population
FROM world.city;
SELECT CountryCode, MAX(Population) AS max_pop
        FROM world.city
GROUP BY CountryCode;
SELECT cit.CountryCode, cit.Name, cit.Population, max_pop
FROM world.city AS cit
    JOIN    (SELECT CountryCode, MAX(Population) AS max_pop
            FROM world.city
            GROUP BY CountryCode) AS t1 ON t1.CountryCode = cit.CountryCode AND Population = max_pop;
SELECT cit.CountryCode, cit.Name, max_pop
FROM world.city AS cit
    JOIN    (SELECT CountryCode, MAX(Population) AS max_pop
            FROM world.city
            GROUP BY CountryCode) AS t1 ON t1.CountryCode = cit.CountryCode AND Population = max_pop;
            
SELECT cit.CountryCode, cit.Name, max_pop
FROM world.city AS cit
    JOIN    (SELECT CountryCode, MAX(Population) AS max_pop
            FROM world.city
            GROUP BY CountryCode) AS t1 ON t1.CountryCode = cit.CountryCode AND Population = max_pop
WHERE Population > (SELECT AVG(Population) FROM world.city);
*/

# Вывести количество людей говорящих на каждом языке. 
# (для подсчета количества использовать население городов).
/*
SELECT SUM(Population) as pop_sum, cl.language
FROM city
LEFT JOIN countrylanguage as cl on cl.CountryCode = city.CountryCode
GROUP BY Language
ORDER BY pop_sum DESC
*/

# Для предыдущей задачи рассчитать в каком % стран, где он используется, он является официальным.
/*
SELECT SUM(Population) as pop_sum, cl.language, COUNT(IF(IsOfficial = 'T', 'T', null)), COUNT(*), ROUND(COUNT(IF(IsOfficial = 'T', 'T', null)) / COUNT(*) * 100, 0)
FROM city
LEFT JOIN countrylanguage as cl on cl.CountryCode = city.CountryCode
GROUP BY Language
ORDER BY pop_sum DESC
*/
























































