# SAE 2.02

## Premier méthode

### Étape 1

Créer l'algorithme DFS de backtracking et renvoyé une instance de Chemin qui va contenir tous les déplacements

#### Sous-étapes

- [ ] Créer une classe Case (Cyprien)
  - x (int) : coordonnée x
  - y (int) : coordonnée y
  - parcourue (bool) : True si parcourue, sinon False
  - [x] getCoordonnéesEchec : renvoie les coordonnées de la case en format échiquier ([1, 6] -> 'a6')
  - [ ] ...
- [ ] Créer une classe Échiquier (Cyprien)
  - un dictionnaire {case (Instance de Case) : list[Case] (liste de Case)}
  - [ ] Func : Pour chaque sommet, liste de liens vers un sommet joignable grâce à un mouvement de cavalier
  - [ ] ...
- [x] Créer une classe Chemin (Maxime)
  - [x] C'est un graphe
- [ ] Créer une classe AllChemins (Maxime)
  - [ ] Tous les Chemin possibles à partir d'une case
  - [ ] nécessaire ?
- [ ] Créer un échiquier en console
- [ ] Créer une fonction renvoyant les cases accessibles par un mouvement de cavalier
- [ ] Créer le programme principal

#### PSC

1. Regarder les cases accessibles (par un mouvement de cavalier et jamais atteinte)
2. Si matrice remplie, renvoyer vrai

3. Sinon pour toutes les cases accessibles :
   1. Prendre la première case accessible, la marquer comme parcourue et recommencer l'algo à partir de cette case
   2. Si l'algo renvoie faux, prendre la case accessible suivante, la marquer comme parcourue et recommencer l'algo à partir de cette case
4. Si le résultat de notre fonction jusqu'à maintenant est faux, renvoyer faux
5. Sinon, renvoyer vrai 

### Étape 2

Affichage de l'échiquier, et du parcours du cavalier avec pygame

## Deuxième méthode

Simple algorithme de backtracking dans [test.py](test.py) permettant de trouver tous les chemins à partir d'une case.
Utilisation de symétrie axiale pour optimiser les calculs : les chemins à partir du coin en haut à gauche sont les mêmes que ceux du coin en haut à droite après une symétrie axiale verticale. Ce principe fonctionne aussi avec une symétrie axiale horizontale et une symétrie centrale.
Ainsi, il est possible de remplir l'entièreté de l'échiquier avec uniquement le quart supérieur droit.

Le gain en calcul est représenté par ce système, avec `L` la longueur et `H` la hauteur :

```math
\begin{cases}
"Si L et H sont pairs :" \frac{(L/2)*(H/2)}{L*H}\\
"Si L est pair et H impair :" \frac{(L/2)*((H/2)+1)}{L*H}\\
"Si L est impair et H pair :" \frac{((L/2)+1)*(H/2)}{L*H}\\
"Si L et H sont impairs :" \frac{\lfloor L/2 \rfloor * \lfloor H/2 \rfloor + \lfloor L/2 \rfloor + \lfloor H/2 \rfloor + 1}{L*H}
\end{cases}
```


Lorsque l'échiquier est de côté paire, cela représente une division par 4 dans le nombre de calcul (les calculs de symétrie étant négligeables).

Calculer le gain en nombres de calculs pour un échiquier de côté impaire est différent :
Nous nous retrouvons obligé de calculer 

(|L/2|*|H/2| + |L/2| + |H/2| + 1)/L*H
