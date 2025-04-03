// Sélectionner l'élément avec ID character
const characterElement = document.querySelector('#character');

// Utiliser Fetch API pour récupérer données depuis l'URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Convertir la réponse en JSON
  .then(data => {
    // Extraire nom du personnage et afficher dans élément HTML
    characterElement.textContent = data.name;
  })
  .catch(error => {
    // En cas d'erreur afficher message dans la console
    console.error('Error fetching data:', error);
  });
