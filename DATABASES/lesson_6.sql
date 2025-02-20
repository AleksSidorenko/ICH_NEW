/* 1) Написать запрос, возвращающий всех сотрудников, c job_id = IT_PROG.
 (Не подглядывая в классный конспект с решением, но подглядывая в схему базы данных 
*/
SELECT * FROM hr.employees WHERE job_id = 'IT_PROG';

-- 2) Изменить запрос так, чтобы вывести всех сотрудников с job_id равной AD_VP?
SELECT * FROM hr.employees WHERE job_id = 'AD_VP';

/* 3) Выполнить эти два запроса: 
SELECT * from HR.EMPLOYEES where job_id = 'IT_PROG' и SELECT * from HR.EMPLOYEES where job_id = 'AD_VP'
*/

/* 4) Воспроизвести самостоятельно следующие запросы:
Найдите сотрудников, с зп от 10 000 до 20 000 (включая концы)
Найдите сотрудников не из 60, 30 и 100 департамента
Найдите сотрудников у которых есть две буквы ll подряд в середине имени
Найдите сотрудников, у которых фамилия кончается на a
*/
SELECT * FROM hr.employees WHERE salary BETWEEN 10000 AND 20000; -- a 
SELECT * FROM hr.employees WHERE department_id NOT IN (60, 30, 100); -- b 
SELECT * FROM hr.employees WHERE first_name LIKE '_%ll_%'; -- c 
SELECT * FROM hr.employees WHERE last_name LIKE '_%a'; -- d 

-- 5) Найти всех сотрудников с зарплатой выше 10000
SELECT * FROM hr.employees WHERE salary > 10000;

-- 6) Найти всех сотрудников, с зарплатой выше 10000 и чья фамилия начинается на букву L
SElECT * FROM hr.employees WHERE salary > 10000 AND last_name LIKE 'L%';



