-- Script pour créer la base de données 'hbtn_0d_usa' et la table 'states'
-- Créer la base de données si elle n'existe pas déjà

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utiliser la base de données 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Créer la table 'states' si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,  -- 'id' est unique, auto-généré et non nul
    name VARCHAR(256) NOT NULL,             -- 'name' ne peut pas être nul
    PRIMARY KEY (id)                       -- Définir 'id' comme clé primaire
);
