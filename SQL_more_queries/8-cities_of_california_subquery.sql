-- Script pour lister les villes de Californie, triées par 'id' dans la table 'cities'
-- Sélectionner les villes où le 'state_id' correspond à l'ID de l'état "California" (ID récupéré via une sous-requête)

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
