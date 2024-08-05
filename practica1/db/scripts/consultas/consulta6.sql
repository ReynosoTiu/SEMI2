SELECT (S.name)Estado, COUNT(*)Total FROM FLIGHT AS F
JOIN STATUS AS S ON S.id = F.status_id
GROUP BY S.name;