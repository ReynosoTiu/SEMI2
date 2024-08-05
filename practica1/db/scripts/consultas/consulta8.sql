SELECT TOP 5 (CO.name)Continente, COUNT(*)Total FROM FLIGHT AS F
JOIN AIRPORT AS C ON C.id = F.airport_id
JOIN CONTINENT AS CO ON CO.id = C.continent_id
GROUP BY CO.name
ORDER BY Total DESC;