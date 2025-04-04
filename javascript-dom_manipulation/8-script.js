document.addEventListener('DOMContentLoaded', function () {
  // Sélectionner l'élément avec ID hello
  const helloElement = document.querySelector('#hello');

  // Vérifie si élément #hello existe
  if (!helloElement) {
    console.error('L\'élément avec l\'ID "hello" n\'a pas été trouvé.');
    return;
  }

  // Utiliser Fetch API pour récupérer la salutation depuis l'URL
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json()) // Convertir la réponse en JSON
    .then(data => {
      helloElement.textContent = data.hello; // Afficher la salutation dans l'élément
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des données :', error);
    });
});
