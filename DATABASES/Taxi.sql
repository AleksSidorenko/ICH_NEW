-- CREATE database 111124_Sidorenko_Taxi;
-- USE 111124_Sidorenko_Taxi;
/*
-- Vehicles
CREATE TABLE Vehicles (
						ID int PRIMARY KEY AUTO_INCREMENT,
						Year_production INT,
						Model VARCHAR(30),
						Plate_number VARCHAR(10),
						Color CHAR(6),
						VIN_number VARCHAR(30),
						Class CHAR(10)
					  );
-- Drivers
CREATE TABLE Drivers (
						ID int PRIMARY KEY AUTO_INCREMENT,
                        Vehicle_id INT UNIQUE,
						First_name VARCHAR(70),
						Last_name VARCHAR(70),
						Driver_license VARCHAR(30),
						Phone_number INT,
						DOB DATE,
						Rating DECIMAL(3,2),
                        Hire_date DATE,
                        Salary DECIMAL(8,2),
                        FOREIGN KEY (ID) REFERENCES Vehicles(ID) 
					  );

-- Reviews
CREATE TABLE Reviews (
						ID int PRIMARY KEY,
						Rating INT,
                        Comment VARCHAR(1000),
                        Review_date DATETIME
					  );
-- Companies
CREATE TABLE Companies (
						ID int PRIMARY KEY,
                        Name VARCHAR(20),
                        Location VARCHAR(255)
					    );
-- Tarifs
CREATE TABLE Tarifs (
						ID int PRIMARY KEY,
                        Class VARCHAR(20),
                        Coefficient DECIMAL(3,2)
					    );
-- Clients
CREATE TABLE Clients (
						ID int PRIMARY KEY AUTO_INCREMENT,
						First_name VARCHAR(70),
						Last_name VARCHAR(70),
						DOB DATE,
						Gender CHAR(1),
						Phone_number INT,
						Email VARCHAR(100)
					  );
-- Orders
CREATE TABLE Orders (
						ID int PRIMARY KEY,
						Price DECIMAL(8,2),
						Client_id INT,
						Start_point_long DECIMAL(15,12),
						Start_point_lat DECIMAL(15,12),
                        End_point_long DECIMAL(15,12),
						End_point_lat DECIMAL(15,12),
						Driver_id INT,
						Start_date DATETIME,
                        End_date DATETIME,
                        Distance DECIMAL(8,2),
                        Review_id INT,
                        Tarif_id INT,
                        Order_type INT,
                        Status INT,
                        Companies_id INT,
                        FOREIGN KEY (Client_id) REFERENCES Clients(ID),
                        FOREIGN KEY (Driver_id) REFERENCES Drivers(ID),
                        FOREIGN KEY (Review_id) REFERENCES Reviews(ID),
                        FOREIGN KEY (Tarif_id) REFERENCES Tarifs(ID),
                        FOREIGN KEY (Companies_id) REFERENCES Companies(ID)
					);
*/
/*
SELECT * FROM Clients;
SELECT * FROM Companies;
SELECT * FROM Drivers;
SELECT * FROM Orders;
SELECT * FROM Reviews;
SELECT * FROM Tarifs;
SELECT * FROM Vehicles;
*/
-- SHOW TABLES;