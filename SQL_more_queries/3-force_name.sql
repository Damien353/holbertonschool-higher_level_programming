-- Script pour créer la table 'force_name' dans la base de données spécifiée
-- Créer la table 'force_name' si elle n'existe pas déjà

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
