-- Tâche : Ce script affiche tous les enregistrements de la table 'second_table' où le score est supérieur ou égal à 10
-- Les résultats doivent afficher 'score' suivi de 'name', triés par score (du plus élevé au plus bas).

-- Sélectionner score et name, filtré pour score >= 10 et trié par score (du plus élevé au plus bas)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
