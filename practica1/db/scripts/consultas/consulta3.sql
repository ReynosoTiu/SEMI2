SELECT (n)Nacionalidad, (MAX(m))Mes, (MAX(a))'Año', (MAX(t))Total FROM (
	SELECT (C.name)n, (D.month_date)m, (D.year_date)a, COUNT(*)t FROM FLIGHT AS F
	JOIN PASSENGER AS P ON P.id = F.passenger_id
	JOIN COUNTRY AS C ON C.id = P.country_id
	JOIN DATE_FL AS D ON D.id = F.date_id
	GROUP BY C.name, D.month_date, D.year_date
) AS NACIONALIDADES
GROUP BY n;