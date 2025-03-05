-- Script pour créer la table 'id_not_null' dans la base de données spécifiée
-- Créer la table 'id_not_null' si elle n'existe pas déjà

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,  -- La colonne 'id' a la valeur par défaut de 1
    name VARCHAR(256)  -- La colonne 'name' peut être NULL par défaut
);
