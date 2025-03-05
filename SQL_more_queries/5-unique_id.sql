-- Script pour créer la table 'unique_id' dans la base de données spécifiée
-- Créer la table 'unique_id' si elle n'existe pas déjà

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,  -- La colonne 'id' a la valeur par défaut de 1 et doit être unique
    name VARCHAR(256)         -- La colonne 'name' peut être NULL par défaut
);
