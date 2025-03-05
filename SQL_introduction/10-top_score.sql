-- Tâche : Ce script affiche tous les enregistrements de la table 'second_table', triés par score (du plus élevé au plus bas)
-- Les résultats doivent afficher 'score' suivi de 'name'.

-- Sélectionner score et name, triés par score (du plus élevé au plus bas)
SELECT score, name
FROM second_table
ORDER BY score DESC;
