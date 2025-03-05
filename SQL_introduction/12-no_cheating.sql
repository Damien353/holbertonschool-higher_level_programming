-- Tâche : Ce script met à jour le score de Bob à 10 dans la table 'second_table'
-- La mise à jour doit être effectuée uniquement avec le champ 'name' et non l'id.

-- Mettre à jour le score de 'Bob' à 10
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
