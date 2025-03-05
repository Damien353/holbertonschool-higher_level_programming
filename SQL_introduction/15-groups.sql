-- Tâche : Ce script liste le nombre d'enregistrements ayant le même score dans la table 'second_table'.
-- Le résultat doit afficher le score et le nombre d'enregistrements pour ce score avec l'étiquette 'number'.
-- La liste sera triée par le nombre d'enregistrements (du plus grand au plus petit).

-- Sélectionner le score et le nombre d'enregistrements ayant ce score, puis trier par nombre décroissant
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
