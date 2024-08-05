-- elminar_tablas.sql

USE semi2practica1; -- Reemplaza con el nombre de tu base de datos
GO

-- Desactivar las restricciones de claves foráneas temporalmente
EXEC sp_MSforeachtable 'ALTER TABLE ? NOCHECK CONSTRAINT ALL'
GO

-- Generar y ejecutar dinámicamente DROP TABLE para cada tabla
DROP TABLE FLIGHT;
DROP TABLE AIRPORT;
DROP TABLE PASSENGER;
DROP TABLE PILOT;
DROP TABLE STATUS;
DROP TABLE CONTINENT;
DROP TABLE COUNTRY;
DROP TABLE DATE_FL;
DROP TABLE ARRIVAL;

-- Reactivar las restricciones de claves foráneas
EXEC sp_MSforeachtable 'ALTER TABLE ? WITH CHECK CHECK CONSTRAINT ALL'
GO