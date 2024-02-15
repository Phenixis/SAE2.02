from Chemin import *
from Echiquier import *
from time import time


carre = 7
result = False

tab = Echiquier(carre, carre)
dep = time()
tab.dfs_path([0, 0])
end = time()
print(f"Temps d'exécution : {end-dep}secs")
print(tab)
"""
x, y = 0, 0
while(x < carre and result == False):
    y = 0
    while (y < carre and result == False):
        print(f"Test pour {x}, {y}")
        result = tab.dfs_path([x, y])
        y += 1
    x += 1

if result:
    print(tab)
else:
    print(f"{x*y}: Impossible")
"""
