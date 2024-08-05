SELECT TOP 5 (A.arrival_airport)'País', COUNT(*)Total FROM FLIGHT AS F
JOIN ARRIVAL AS A ON A.id = F.arrival_id
WHERE A.arrival_airport <> '0'
GROUP BY A.arrival_airport
ORDER BY Total DESC;