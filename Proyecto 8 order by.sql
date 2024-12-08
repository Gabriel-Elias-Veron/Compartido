-- GROUP BY: Agrupa por la categoría y calcula el precio promedio en cada categoría
-- ORDER BY: Ordena el resultado por el precio promedio en orden ascendente
SELECT Categoria, AVG(Precio) as PrecioPromedio
FROM Productos
GROUP BY Categoria
ORDER BY PrecioPromedio ASC;
