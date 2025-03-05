-- Tâche : Ce script liste tous les enregistrements de la table 'second_table' où la colonne 'name' n'est pas vide.
-- Les résultats afficheront le score et le nom, triés par score décroissant.

-- Sélectionner le score et le nom, exclure les enregistrements où le nom est vide, et trier par score décroissant
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

