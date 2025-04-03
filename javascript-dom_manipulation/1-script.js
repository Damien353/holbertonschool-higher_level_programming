// Sélectionner l'élément avec ID red_header
const redHeader = document.querySelector('#red_header');

// Sélectionner l'élément header
const header = document.querySelector('header');

// Ajouter un gestionnaire d'événement pour l'événement 'click'
redHeader.addEventListener('click', function() {
  // Modifier la couleur du texte du header (#FF0000)
  header.style.color = '#FF0000';
});
