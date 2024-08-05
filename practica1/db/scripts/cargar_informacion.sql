USE semi2practica1;

INSERT INTO COUNTRY (id, name)
SELECT DISTINCT airport_country_code, country_name FROM PassengerDataTemp;

WITH Nacionalidades AS (
    SELECT nationality, ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS row_num 
    FROM (
		SELECT  DISTINCT nationality
		FROM PassengerDataTemp AS A
		LEFT JOIN COUNTRY AS C ON A.nationality = C.name
		WHERE C.name IS NULL AND A.nationality IS NOT NULL
	) AS UniqueNationalities
)
INSERT INTO COUNTRY (id, name)
SELECT 
    CAST(row_num AS VARCHAR(10)), 
    nationality
FROM Nacionalidades;

INSERT INTO CONTINENT (id, name)
SELECT DISTINCT airport_continent, continents FROM PassengerDataTemp;

INSERT INTO STATUS (name)
SELECT DISTINCT flight_status FROM PassengerDataTemp;

INSERT INTO PILOT (name)
SELECT DISTINCT pilot_name FROM PassengerDataTemp;

INSERT INTO PASSENGER (passenger_code, first_name, last_name, gender, age, country_id)
SELECT DISTINCT passenger_id, first_name, last_name, gender, age, (SELECT id FROM COUNTRY WHERE name = nationality)country_id  FROM PassengerDataTemp;

INSERT INTO AIRPORT (name, country_id, continent_id)
SELECT DISTINCT airport_name, airport_country_code, airport_continent FROM PassengerDataTemp;

INSERT INTO DATE_FL (departure_date, month_date, year_date)
SELECT DISTINCT departure_date, MONTH(departure_date)month_date, YEAR(departure_date)year_date FROM PassengerDataTemp;

INSERT INTO ARRIVAL (arrival_airport)
SELECT DISTINCT arrival_airport FROM PassengerDataTemp;

INSERT INTO FLIGHT (date_id, arrival_id, passenger_id, airport_id, pilot_id, status_id)
SELECT 
(SELECT id from DATE_FL AS A WHERE A.departure_date = P.departure_date)date_id,
(SELECT id FROM ARRIVAL AS B WHERE B.arrival_airport = P.arrival_airport)arrival_id,
(SELECT id FROM PASSENGER AS C WHERE C.passenger_code = P.passenger_id)passenger_id,
(SELECT id from AIRPORT AS D WHERE D.name = P.airport_name and D.country_id = P.airport_country_code and D.continent_id = P.airport_continent)airport_id,
(SELECT id from PILOT AS E WHERE E.name = P.pilot_name)pilot_id,
(SELECT id from STATUS AS F WHERE F.name = P.flight_status)status_id
FROM PassengerDataTemp AS P;