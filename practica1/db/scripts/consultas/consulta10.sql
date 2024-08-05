SELECT (D.departure_date)'Fecha salida',
	COUNT(*)Total
FROM FLIGHT AS F
JOIN DATE_FL AS D ON D.id = F.date_id
GROUP BY D.departure_date
ORDER BY D.departure_date DESC;