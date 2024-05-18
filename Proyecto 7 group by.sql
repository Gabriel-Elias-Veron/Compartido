-- GROUP BY: Agrupa por la ciudad y cuenta la cantidad de personas en cada ciudad
-- ORDER BY: Ordena el resultado por la cantidad de personas en orden descendente
SELECT Ciudad, COUNT(*) as CantidadDePersonas
FROM PERSONAL
GROUP BY Ciudad
ORDER BY CantidadDePersonas DESC;
