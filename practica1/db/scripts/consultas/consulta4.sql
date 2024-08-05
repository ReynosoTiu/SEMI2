SELECT (C.name)'País', COUNT(*)Total FROM FLIGHT AS F
JOIN AIRPORT AS A ON A.id = F.airport_id
JOIN COUNTRY AS C ON C.id = A.country_id
GROUP BY C.name