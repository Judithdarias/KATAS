/*Seleccioonar todos los registros de una tabla*/
SELECT * FROM movements;
/*seleccionar algunos campos de una tabla de base de datos*/
SELECT concept,quantity FROM movements;
/*para insertar nuevos registros en la tabla*/
INSERT INTO movements(date,concept,quantity) VALUES ("2026-02-12","extra trabajo",100);
/*para actualizar registros de la table de base de datos*/
/*UPDATE movements SET concept = "almuerzo",quantity=-50 WHERE id = 2;*/
SELECT * FROM movements WHERE quantity <0;
/*comando para borrar registros, importante utilizar siempre el where sino
de la tabla*/
/*DELETE from movements WHERE id = 6;*/
/*consulta select con orden aplicado*/
SELECT * from movements ORDER BY id DESC;
