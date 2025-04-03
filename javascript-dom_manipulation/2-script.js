// Sélectionner l'élément avec ID red_header
const redHeader = document.querySelector('#red_header');

// Sélectionner l'élément header
const header = document.querySelector('header');

// Ajouter un gestionnaire d'événement pour l'événement click
redHeader.addEventListener('click', function() {
  // Ajouter la classe red à l'élément header
  header.classList.add('red');
});
