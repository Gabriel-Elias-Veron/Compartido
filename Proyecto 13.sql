SELECT PERSONAL.Nombre AS Cliente, Productos.NombreProducto, Productos.Precio
FROM PERSONAL
INNER JOIN facturas ON PERSONAL.ID = facturas.cliente_id
INNER JOIN Productos ON facturas.id_factura = Productos.ID;
