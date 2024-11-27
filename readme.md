# Gestion des contacts
Vous allez développer une gestion de contacts en créant 7 programmes en Python.
### 1 – Ajout de contacts

Vous permettez à l’utilisateur de créer un contact en lui demandant la saisie d’un nom, d’un
prénom et d’une adresse mail. Chaque nouveau contact créé vient s’ajouter au fichier nommé
« contacts.txt » qui contient tous les contacts créés à raison d’un contact par ligne.
Dans ce fichier, les champs nom, prénom et adresse mail sont séparés par une virgule.
Voici un exemple de fichier contact.txt avec 2 contacts :
Dupont, Pierre, pierre.dupont@exemple.fr
Durand, Louis, louis.durand@exemple.fr
### 2 – Lecture des contacts

L’utilisateur peut afficher la liste des contacts contenus dans le fichier « contacts.txt ».
L’affchage se fera sous la forme suivante :
Nom : Dupont, Prénom : Pierre, Email : pierre.dupont@exemple.fr
Nom : Durand, Prénom : Louis, Email : louis.durand@exemple.fr
### 3 – Lecture des contacts avec tri alphabétique

L’utilisateur peut trier le fichier « contacts.txt » dans l’ordre alphabétique du nom.
On réécrit donc le fichier « contact.txt ».
On peut ensuite le lire et l’afficher grâce à l’algorithme numéro 2.
### 4 – Compter les contacts

On crée un algorithme qui affiche à l’utilisateur combien il y a de contacts dans le fichier
« contact.txt ».
### 5 – Recherche d’un contact
On demande à l’utilisateur de saisir le nom qu’il recherche et on lui affche le contact
correspondant s’il existe, sinon on lui signale qu’il n’y a pas de contacts portant ce nom.
### 6 – Modification d’un contact
On demande à l’utilisateur de saisir le nom du contact qu’il veut modifier.
Si ce contact existe on permet à l’utilisateur de saisir un nouveau prénom et un nouvel email et
on les enregistre à la place des anciennes valeurs. (on ne change pas le nom).
### 7 – Suppression d’un contact
On demande à l’utilisateur de saisir le nom du contact qu’il veut supprimer.
Si ce contact existe on supprime ce contact du fichier « contacts.txt ».