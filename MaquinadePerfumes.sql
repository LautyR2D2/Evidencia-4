CREATE TABLE Recetas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    alcohol DECIMAL(5,2),
    aceites_esenciales DECIMAL(5,2),
    agua DECIMAL(5,2)
);
CREATE TABLE Olores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    receta_id INT,
    nombre_olor VARCHAR(50),
    cantidad DECIMAL(5,2),
    FOREIGN KEY (receta_id) REFERENCES Recetas(id)
);
INSERT INTO Recetas (nombre, alcohol, aceites_esenciales, agua) VALUES
('Perfume Floral', 80, 15, 5),
('Perfume Amaderado', 70, 20, 10);
INSERT INTO Olores (receta_id, nombre_olor, cantidad) VALUES
(1, 'Rosa', 10),
(1, 'Jazmín', 5),
(1, 'Lavanda', 7),
(1, 'Vainilla', 3),
(2, 'Sándalo', 15),
(2, 'Cedro', 10),
(2, 'Ámbar', 5),
(2, 'Pachulí', 7);

SELECT * FROM Recetas;

SELECT o.nombre_olor, o.cantidad
FROM Olores o
JOIN Recetas r ON o.receta_id = r.id
WHERE r.nombre = 'Perfume Floral';

SELECT r.nombre AS Receta, o.nombre_olor AS Olor, o.cantidad
FROM Recetas r
JOIN Olores o ON r.id = o.receta_id;

SELECT nombre, aceites_esenciales
FROM Recetas
WHERE aceites_esenciales > 10;

SELECT r.nombre
FROM Recetas r
JOIN Olores o ON r.id = o.receta_id
WHERE o.nombre_olor = 'Cedro';
