SELECT 
    (P.gender)Genero,
	COUNT(*)Total,
	(SUBSTRING(CAST(((COUNT(*)*10000/(SELECT COUNT(*) FROM FLIGHT) + 0.00)/100) AS VARCHAR(50)), 0, 6) + '%')Porcentaje
FROM FLIGHT AS F
JOIN PASSENGER AS P ON P.id = F.passenger_id
GROUP BY gender;
