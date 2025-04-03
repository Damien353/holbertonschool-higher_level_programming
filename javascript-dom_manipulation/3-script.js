// Sélectionner l'élément avec ID toggle_header
const toggleHeader = document.querySelector('#toggle_header');

// Sélectionner l'élément header
const header = document.querySelector('header');

// Ajouter un gestionnaire d'événement pour l'événement click
toggleHeader.addEventListener('click', function() {
  // Vérifier la classe actuelle et basculer entre red et green
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});
