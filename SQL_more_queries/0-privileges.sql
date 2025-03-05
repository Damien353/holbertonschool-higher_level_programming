-- Script pour lister les privilèges des utilisateurs 'user_0d_1' et 'user_0d_2'
--

-- Créer les utilisateurs s'ils n'existent pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Accorder les privilèges à 'user_0d_1' (exemple : lui donner tous les privilèges sur toutes les bases de données)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Accorder les privilèges à 'user_0d_2' (exemple : lui donner un accès en lecture seule)
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';

-- Afficher les privilèges de 'user_0d_1'
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Afficher les privilèges de 'user_0d_2'
SHOW GRANTS FOR 'user_0d_2'@'localhost';
