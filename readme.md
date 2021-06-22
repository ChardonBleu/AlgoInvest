# AlgoInvest&Trade

Projet 7 de la formation DA python d'Openclassrooms.

Application permettant de trouver le portefeuille d'actions le plus rentable
dans un lot d'actions du marché.
Trois lots d'actions sont disponibles:
    * Un lot de 20 actions enregistré en dur dans le fichier constant.py
    * Deux lots de 1000 actions environ contenus dans les fichiers dataset1.csv et
    dataset2.csv

Trois algorithmes sont disponibles:
    * L'algorithme de force_brute qui construit un arbre binaire de tous les portefeuilles
    possibles et qui retient le portefeuille le plus rentable.
    Le compléxité de cet algorithme est exponentielle.
    Il n'est pas raisonnablement utilisable sur les dataset csv.
    * L'algorithme dynamique construit un tableau dynamique des meilleurs gains possibles
    puis détermine le portefeuille le plus rentable par exploitaiton de ce tableau.
    Sa complexité est de l'ordre de : nombre d'actions x somme maxi à investir.
    * L'algorithme glouton est le plus rapide, mais le moins optimal en terme de rentabilité
    du portefeuille retenu.


Installation
---
Télécharger les fichiers et les copier dans un dossier de votre choix.
Dans la console aller dans ce dossier choisi.


Exécution
---

Se mettre dans le répertoire contenant les dossier *.py et taper dans la console
l'excécution du programme choisi:

```bash 
python -m force_brute
```
ou
```bash 
python -m dynamique
```
ou 
```bash 
python -m glouton
```

Ressources utilisées
---

Ressources web:

    https://dept-info.labri.fr/ENSEIGNEMENT/projet2/supports/Sac-a-dos/Le-probleme-du-sac-a-dos.pdf

    https://www.irif.fr/~francoisl/DIVERS/m1algo-progdynamique.pdf

    https://www.geeksforgeeks.org/space-optimized-dp-solution-0-1-knapsack-problem/


Remerciements
---

Un très grand merci à Thierry Chappuis pour tous ses précieux conseils et retours,
et à tous les apprenants du Discord DA Pyhton.

http://discord.pythonclassmates.org/