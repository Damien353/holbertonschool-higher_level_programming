// Sélectionner l'élément avec ID add_item
const addItem = document.querySelector('#add_item');

// Sélectionner l'élément ul avec la classe my_list
const myList = document.querySelector('.my_list');

// Ajouter un gestionnaire d'événements pour événement click
addItem.addEventListener('click', function() {
  // Créer un nouvel élément li
  const newItem = document.createElement('li');
  
  // Ajouter du texte à élément li
  newItem.textContent = 'Item';
  
  // Ajouter nouvel élément li à la liste ul
  myList.appendChild(newItem);
});
