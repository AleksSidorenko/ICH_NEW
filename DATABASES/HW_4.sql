/*
1. Не подглядывая в решение в классе, создать таблицу weather с тремя полями:
- название города (city)
- дата (forecast_date)
- температура в эту даты (temperature)
*/
USE 111124_Sidorenko;
/*
CREATE TABLE weather(
id int PRIMARY KEY auto_increment,
city varchar(30), 
forecast_date date, 
temperature int);
*/
/*
2. Добавить данные в таблицу, используя запрос INSERT
“29 августа 2023 года в Берлине было 30 градусов”
*/
/*
INSERT INTO weather(city, forecast_date, temperature)
values
('Berlin', '2023-08-29', 30);
*/

-- 3. Добавить еще 3 записи в таблицу (произвольную погоду в разных городах в разные дни). 
/* INSERT INTO weather(city, forecast_date, temperature)
values
('Madrid', '2023-08-30', 35),
('Vankuver', '2023-08-31', 25),
('Milan', '2023-08-29', 28);
*/
-- 4. Написать запрос, который возвращает содержимое таблицы. 
-- SELECT * FROM weather;
-- 5. Изменить данные в таблице о температуре в Берлине с 30 на 26 градусов.
/*
UPDATE weather
SET temperature = 26
WHERE city = 'Berlin';
*/
-- 6. Поменяйте во всей таблице название города на Paris для записей, где температура выше 25 градусов. 
/*
UPDATE weather
SET city = 'Paris'
WHERE temperature > 25;
*/
-- 7. Добавить к таблице weather дополнительный столбец min_temp типа integer.
/*
ALTER TABLE weather
ADD min_temp int;
*/
-- 8. Используя команду update, установить значение поля min_temp в 0 для всех записей в таблице.
/*
UPDATE weather
SET min_temp = 0;
*/
-- SELECT * FROM weather