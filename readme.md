# AlgoInvest&Trade

Projet 7 de la formation DA python d'Openclassrooms.

Application permettant de trouver le portefeuille d'actions le plus rentable
dans un lot d'actions du marché.
Trois lots d'actions sont disponibles:
    * Un lot de 20 actions enregistrés en dur dans le fichier constant.
    * Deux lots de 1000 actions environ contenus dans les fichiers csv dataset1.csv et
    dataset2.csv

Trois algorithmes sont disponibles:
    * L'algorithme de force_brute qui construit un arbre binaire de tous les portefeuilles
    possible et qui retient le portefeuille le plus rentable.
    Le compléxité de cet algorithme est exponentielle.
    Il n'est pas raisonablement utilisable sur les dataset csv.
    * L'algorithme dynamique cosntruit un tableau dynamique des meilleurs gains possibles
    puis détermine le portefeuille le plus rentable par exploitaiton de ce tableau.
    Sa complexité est de l'ordre de : nombre d'actions x somme maxi à investir.
    * L'algorithme glouton est le plus rapide, mais le moins optimal en terme de rentabilité
    du portefeuille retenu


Installation
---
Télécharger les dossier et fichier et les copier dans un dossier de votre choix
Dans la console aller dans ce dossier choisi.

Environnement virtuel
---
https://docs.python.org/fr/3/library/venv.html?highlight=venv

Créer un environnement virtuel: 

```bash
python -m venv env
```

Activer cet environnement virtuel:
sur windows dans Visual Studio Code: 
```bash 
. env/Scripts/activate 
```
sur mac ou linux: 
```bash 
source env/bin/activate 
```
Packages
---

Puis installer les modules necessaires:
```bash 
python -m pip -r requirements.txt
```

Exécution
---
Se mettre dans le répertoire contenant le dossier application et taper dans la console:

```bash 
python -m application
```

Générer un rapport flake-8 html
---

Se mettre dans le répertoire application.

Dans la console excécuter:
```bash 
flake8 --format=html --htmldir=flake-report
```
Un nouveau rapport flake8 est généré. aller dans le répertoire flake-report et ouvrir le fichier index.html dans un navigateur web.

Ressources utilisées
---

Livres:
    Apprenez à programmer en Python - Vincent Le Goff - Eyrolles
    
    Python crash courses - Eric Matthes - no starch press

Ressources web:

    Write Maintainable Pyhton Code - Daniel Timms

    https://openclassrooms.com/fr/courses/6900866-write-maintainable-python-code

    Webinaires MVC jeu du Pendu parties 1 et 2 - Thierry Chappuis

    https://www.notion.so/Webinaires-Pythonclassmates-Cafes-Zoom-8223a18f53a8457d94d96887c326c652


Remerciements
---

Un très grand merci à Aurélien Massé et à Thierry Chappuis pour tous leurs précieux conseils et retours,
et à tous les apprenants du Discord DA Pyhton.

http://discord.pythonclassmates.org/