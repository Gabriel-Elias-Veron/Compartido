CREATE TABLE Productos (
    ID INT PRIMARY KEY,
    NombreProducto VARCHAR(255),
    Precio DECIMAL(10, 2),
    Stock INT,
    Categoria VARCHAR(255),
    Fabricante VARCHAR(255)
);

INSERT INTO Productos (ID, NombreProducto, Precio, Stock, Categoria, Fabricante)
VALUES
(1, 'Laptop', 1200.00, 50, 'Electrónica', 'MarcaX'),
(2, 'Teléfono móvil', 800.00, 30, 'Electrónica', 'MarcaY'),
(3, 'Camiseta', 20.00, 100, 'Ropa', 'FabricanteA'),
(4, 'Zapatillas deportivas', 50.00, 80, 'Calzado', 'FabricanteB'),
(5, 'Libro', 15.00, 200, 'Libros', 'EditorialX'),
(6, 'Cámara digital', 500.00, 15, 'Electrónica', 'MarcaZ'),
(7, 'Reloj', 100.00, 50, 'Accesorios', 'FabricanteC'),
(8, 'Silla de oficina', 80.00, 40, 'Muebles', 'FabricanteD'),
(9, 'Gafas de sol', 30.00, 60, 'Accesorios', 'FabricanteE'),
(10, 'Cafetera', 70.00, 25, 'Electrodomésticos', 'MarcaW');
