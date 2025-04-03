// Sélectionner l'élément avec ID update_header
const updateHeader = document.querySelector('#update_header');

// Sélectionner l'élément header
const header = document.querySelector('header');

// Ajouter gestionnaire événement pour l'événement click
updateHeader.addEventListener('click', function() {
  // Mettre à jour texte du header
  header.textContent = 'New Header!!!';
});
