-- Tâche : Ce script crée la table 'second_table' et insère plusieurs enregistrements dans la base de données spécifiée.
-- Si la table 'second_table' existe déjà, le script ne doit pas échouer.

-- Créer la table 'second_table' si elle n'existe pas
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insérer les lignes spécifiées dans la table 'second_table'
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
