[] Listage des pages web à faire
-> [-] Préparer d'abord les modèles
-> [] Préparer des données déjà initialisé

[-] Création du modèle de cours -> Deck

## App "quiz":
### Gestion des flashcards :
 Création, modification et suppression de flashcards. (forms.py)
 Chaque flashcard doit contenir un côté "question" et un côté "réponse".

### Répétition espacée :
L'algorithme de répétition espacée doit être implémenté pour gérer le planning de révision des flashcards. (views.py)
Les flashcards doivent être présentées aux utilisateurs en fonction de leur niveau de mémorisation et de leur performance lors des révisions précédentes.

### Statistiques de révision :
Les utilisateurs doivent pouvoir consulter leurs statistiques de révision, telles que le nombre de flashcards révisées, le nombre de réponses correctes, etc.

### Liste de pages à faire:
[] Page d'affichages des cartes
[-] Page pour réviser une carte (templates/quiz/carte.html/)
[] Views pour réviser plusieurs cartes (selectionner toutes les cartes avec une date de révision pour aujourd'hui-> les balancer dans un render tant que les dates de révision n'ont pas changé...)


## App "cours"
- Gestion des cours :
[] Création, modification et suppression de cours. (forms.py)
 Chaque cours doit contenir un document, et un titre
- Système de Classement des cours :
Les cours les plus valorisés seront les plus illustrés, les plus courts, et les plus télécahrgés. (views.py)

### Liste de pages à faire:
[!] Page d'ajout d'une carte
[]
[] Page d'affichage des cours
[] Page pour ajouter un cours
[-] Page pour lire un cours
