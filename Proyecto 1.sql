CREATE DATABASE PROYECTOS;
CREATE TABLE PERSONAL (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(255),
    Edad INT,
    Ciudad VARCHAR(255),
    Email VARCHAR(255)
);

INSERT INTO PERSONAL (ID, Nombre, Edad, Ciudad, Email)
VALUES
(1, 'Juan', 25, 'Ciudad A', 'juan@email.com'),
(2, 'Ana', 30, 'Ciudad B', 'ana@email.com'),
(3, 'Carlos', 22, 'Ciudad C', 'carlos@email.com'),
(4, 'María', 28, 'Ciudad A', 'maria@email.com'),
(5, 'Pedro', 35, 'Ciudad B', 'pedro@email.com'),
(6, 'Laura', 29, 'Ciudad C', 'laura@email.com'),
(7, 'Miguel', 26, 'Ciudad A', 'miguel@email.com'),
(8, 'Sofía', 32, 'Ciudad B', 'sofia@email.com'),
(9, 'David', 27, 'Ciudad C', 'david@email.com'),
(10, 'Isabel', 31, 'Ciudad A', 'isabel@email.com');
