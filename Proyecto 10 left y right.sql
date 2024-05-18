-- LEFT JOIN: Devuelve todas las filas de la tabla de la izquierda (PERSONAL) y las filas coincidentes de la tabla de la derecha (facturas)
SELECT *
FROM PERSONAL
LEFT JOIN facturas ON PERSONAL.ID = facturas.cliente_id;

-- RIGHT JOIN: Devuelve todas las filas de la tabla de la derecha (facturas) y las filas coincidentes de la tabla de la izquierda (PERSONAL)
SELECT *
FROM PERSONAL
RIGHT JOIN facturas ON PERSONAL.ID = facturas.cliente_id;
