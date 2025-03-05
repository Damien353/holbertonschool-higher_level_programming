-- Tâche : Ce script calcule la moyenne des scores de tous les enregistrements dans la table 'second_table'
-- Le résultat sera affiché sous le nom de colonne 'average'.

-- Calculer la moyenne des scores
SELECT AVG(score) AS average
FROM second_table;
