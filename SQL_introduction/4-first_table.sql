-- Tâche : Ce script crée une table appelée 'first_table' dans la base de données actuelle.
-- Si la table 'first_table' existe déjà, le script ne doit pas échouer.

-- Créer la table 'first_table' uniquement si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
