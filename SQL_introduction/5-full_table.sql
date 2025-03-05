-- Ce script affiche la description de la table 'first_table' dans la base de données spécifiée.
-- La commande ne doit pas utiliser DESCRIBE ou EXPLAIN.

-- Sélectionner la base de données avant d'exécuter la requête (optionnel)
USE hbtn_0c_0;

-- Sélectionner la définition de la table 'first_table' depuis information_schema.tables
SELECT CONCAT('Table ', table_name, '    ', CREATE_TABLE) AS 'Table   Create Table'
FROM information_schema.tables
WHERE table_schema = DATABASE() AND table_name = 'first_table';
