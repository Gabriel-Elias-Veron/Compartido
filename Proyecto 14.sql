SELECT PERSONAL.Nombre AS Cliente, facturas.numero_factura, facturas.total
FROM PERSONAL
LEFT JOIN facturas ON PERSONAL.ID = facturas.cliente_id
WHERE facturas.estado = 'Pendiente';
