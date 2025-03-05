-- Script pour créer l'utilisateur 'user_0d_1' avec tous les privilèges
-- 

-- Créer l'utilisateur si il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges à 'user_0d_1' sur toutes les bases de données et tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
