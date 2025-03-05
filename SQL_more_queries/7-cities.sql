-- Script pour créer la base de données 'hbtn_0d_usa' et la table 'cities'
-- Créer la base de données si elle n'existe pas déjà

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utiliser la base de données 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Créer la table 'cities' si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,     -- 'id' est unique, auto-généré et non nul
    state_id INT NOT NULL,                    -- 'state_id' est non nul
    name VARCHAR(256) NOT NULL,               -- 'name' est non nul
    PRIMARY KEY (id),                         -- Définir 'id' comme clé primaire
    CONSTRAINT cities_ibfk_1 FOREIGN KEY (state_id) REFERENCES states(id) -- Définir la clé étrangère
);
