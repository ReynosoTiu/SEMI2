SELECT TOP 5 
    (P.gender)Genero,
	(P.age)Edad,
	COUNT(*)Total
FROM FLIGHT AS F
JOIN PASSENGER AS P ON P.id = F.passenger_id
GROUP BY P.gender, P.age
ORDER BY Total DESC;