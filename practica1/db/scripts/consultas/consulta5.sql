SELECT TOP 5 (A.name)'País', COUNT(*)Total FROM FLIGHT AS F
JOIN AIRPORT AS A ON A.id = F.airport_id
GROUP BY A.name
ORDER BY Total DESC;