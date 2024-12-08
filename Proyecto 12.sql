SELECT facturas.*, Productos.NombreProducto
FROM facturas
LEFT JOIN Productos ON facturas.id_factura = Productos.ID;
