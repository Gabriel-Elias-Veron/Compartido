SELECT facturas.*, PERSONAL.Nombre AS NombreCliente
FROM facturas
INNER JOIN PERSONAL ON facturas.cliente_id = PERSONAL.ID;
