-- 1. Подключитесь к базе данных hr (которая находится на удаленном сервере). 
-- USE hr;

-- 2. Выведите количество сотрудников в базе
-- SELECT COUNT(employee_id)
-- FROM employees

-- 3. Выведите количество департаментов (отделов) в базе
-- SELECT COUNT(department_id)
-- FROM departments

-- 4. Подключитесь к базе данных World (которая находится на удаленном сервере). 
-- USE world;

-- 5. Выведите среднее население в городах Индии (таблица City, код Индии - IND)
-- SELECT Name, AVG(Population)
-- FROM city
-- WHERE CountryCode = "IND"

-- 6. Выведите минимальное и максимальное население в индийских городах.
-- SELECT Name, Population FROM city
-- WHERE CountryCode = 'IND' AND (Population = (SELECT MIN(Population) FROM city WHERE CountryCode = 'IND') 
--    OR Population = (SELECT MAX(Population) FROM city WHERE CountryCode = 'IND'))
-- SELECT Name, Population FROM city
-- WHERE CountryCode = 'IND' AND (Population = 89053 OR Population = 10500000)
--------------
-- SELECT Name, Population FROM city
-- WHERE Population = (SELECT MIN(Population) FROM city WHERE CountryCode = 'IND' ORDER BY Population LIMIT 1) 
--    OR Population = (SELECT MAX(Population) FROM city WHERE CountryCode = 'IND' ORDER BY Population DESC LIMIT 1)
-- WHERE Population = (SELECT MIN(DISTINCT Population) FROM city WHERE CountryCode = 'IND') 
--    OR Population = (SELECT MAX(DISTINCT Population) FROM city WHERE CountryCode = 'IND')
-- -----------
-- SELECT DISTINCT Population, Name FROM city
-- WHERE Population = (SELECT MIN(Population) FROM city WHERE CountryCode = 'IND') 
--    OR Population = (SELECT MAX(Population) FROM city WHERE CountryCode = 'IND')
--    
-- 7. Выведите самую большую площадь территории. 
-- SELECT MAX(SurfaceArea) FROM country;

-- 8. Выведите среднюю продолжительность жизни по странам. 
-- SELECT ROUND(AVG(LifeExpectancy))
-- FROM country

-- 9. Найдите самый населенный город (подсказка: использовать подзапросы)
-- SELECT Name, Population
-- FROM city
-- WHERE Population = (SELECT MAX(Population) FROM city)






