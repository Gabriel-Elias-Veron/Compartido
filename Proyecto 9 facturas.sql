CREATE TABLE facturas (
    id_factura INT PRIMARY KEY,
    numero_factura VARCHAR(20),
    fecha_emision DATE,
    cliente_id INT,
    total DECIMAL(10, 2),
    estado VARCHAR(15)
);

INSERT INTO facturas (id_factura, numero_factura, fecha_emision, cliente_id, total, estado)
VALUES
    (1, 'F2023001', '2023-01-15', 101, 150.50, 'Pagada'),
    (2, 'F2023002', '2023-02-02', 102, 200.75, 'Pendiente'),
    (3, 'F2023003', '2023-03-10', 103, 75.20, 'Pagada'),
    (4, 'F2023004', '2023-04-05', 104, 350.00, 'Pendiente'),
    (5, 'F2023005', '2023-05-20', 105, 120.90, 'Pagada'),
    (6, 'F2023006', '2023-06-08', 106, 80.60, 'Pendiente'),
    (7, 'F2023007', '2023-07-15', 107, 220.30, 'Pagada'),
    (8, 'F2023008', '2023-08-22', 108, 300.45, 'Pendiente'),
    (9, 'F2023009', '2023-09-18', 109, 180.75, 'Pagada'),
    (10, 'F2023010', '2023-10-05', 110, 90.20, 'Pendiente');

-- Insertar 20 ejemplos adicionales de datos
INSERT INTO facturas (id_factura, numero_factura, fecha_emision, cliente_id, total, estado)
VALUES
    (11, 'F2023011', '2023-11-12', 111, 250.30, 'Pagada'),
    (12, 'F2023012', '2023-12-03', 112, 130.45, 'Pendiente'),
    (13, 'F2023013', '2024-01-08', 113, 175.60, 'Pagada'),
    (14, 'F2023014', '2024-02-14', 114, 200.00, 'Pendiente'),
    (15, 'F2023015', '2024-03-20', 115, 300.75, 'Pagada'),
    (16, 'F2023016', '2024-04-25', 116, 150.90, 'Pendiente'),
    (17, 'F2023017', '2024-05-30', 117, 280.20, 'Pagada'),
    (18, 'F2023018', '2024-06-15', 118, 90.50, 'Pendiente'),
    (19, 'F2023019', '2024-07-02', 119, 180.30, 'Pagada'),
    (20, 'F2023020', '2024-08-18', 120, 120.75, 'Pendiente'),
    (21, 'F2023021', '2024-09-10', 121, 300.60, 'Pagada'),
    (22, 'F2023022', '2024-10-05', 122, 160.45, 'Pendiente'),
    (23, 'F2023023', '2024-11-20', 123, 90.20, 'Pagada'),
    (24, 'F2023024', '2024-12-08', 124, 200.30, 'Pendiente'),
    (25, 'F2023025', '2025-01-15', 125, 150.60, 'Pagada'),
    (26, 'F2023026', '2025-02-22', 126, 180.75, 'Pendiente'),
    (27, 'F2023027', '2025-03-18', 127, 250.90, 'Pagada'),
    (28, 'F2023028', '2025-04-05', 128, 120.20, 'Pendiente'),
    (29, 'F2023029', '2025-05-12', 129, 300.45, 'Pagada'),
    (30, 'F2023030', '2025-06-28', 130, 80.30, 'Pendiente');
