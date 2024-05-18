SELECT PERSONAL.Nombre AS Cliente, facturas.numero_factura, Productos.NombreProducto, facturas.total
FROM PERSONAL
INNER JOIN facturas ON PERSONAL.ID = facturas.cliente_id
INNER JOIN Productos ON facturas.id_factura = Productos.ID
WHERE facturas.estado = 'Pagada';
