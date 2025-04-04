// Sélectionner élément ul où les titres seront ajoutés
const listMovies = document.querySelector('#list_movies');

// Utiliser Fetch API pour récupérer les films
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Convertir réponse en JSON
  .then(data => {
    // Pour chaque film, créer un élément li et ajouter à la liste
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMovies.appendChild(listItem); // Ajouter élément li à la liste ul
    });
  })
  .catch(error => {
    // Gérer les erreurs
    console.error('Error fetching data:', error);
  });
