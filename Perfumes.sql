SELECT * FROM Recetas;
SELECT o.nombre_olor, o.cantidad
FROM Olores o
JOIN Recetas r ON o.receta_id = r.id
WHERE r.nombre = 'Perfume Amaderado';
