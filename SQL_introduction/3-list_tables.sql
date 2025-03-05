-- Tâche : Ce script liste toutes les tables d'une base de données MySQL donnée.
-- Il utilise la base de données spécifiée par l'argument.

-- Sélectionner les noms des tables de la base de données actuelle
SELECT table_name 
FROM information_schema.tables
WHERE table_schema = DATABASE();
