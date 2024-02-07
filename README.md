# SAE 2.02

## Étape 1

Créer l'algorithme DFS de backtracking et renvoyé une instance de Chemin qui va contenir tous les déplacements

### Sous-étapes

- [ ] Créer une classe Graphe
- [ ] Créer une classe Chemin
- [ ] Créer un échiquier en console
- [ ] Créer une fonction renvoyant les cases accessibles par un mouvement de cavalier
- [ ] Créer le programme principal

### PSC

1. Regarder les cases accessibles (par un mouvement de cavalier et jamais atteinte)
2. Si matrice remplie, renvoyer vrai

3. Sinon pour toutes les cases accessibles :
   1. Prendre la première case accessible, la marquer comme parcourue et recommencer l'algo à partir de cette case
   2. Si l'algo renvoie faux, prendre la case accessible suivante, la marquer comme parcourue et recommencer l'algo à partir de cette case
4. Si le résultat de notre fonction jusqu'à maintenant est faux, renvoyer faux
5. Sinon, renvoyer vrai 

## Étape 2

Affichage de l'échiquier, et du parcours du cavalier avec pygame

