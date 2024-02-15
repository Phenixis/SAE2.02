from Chemin import *
from Echiquier import *

carre = 8
result = False

tab = Echiquier(carre, carre)
# tab.dfs_path([0, 0])
print(tab)
"""
x, y = 0, 0
while(x < carre and result == False):
    y = 0
    while (y < carre and result == False):
        print(f"Test pour {x}, {y}")
        result = tab.dfs_path([x, y])
        if result:
            print(tab)
        else:
            print(f"{x*y}: Impossible")
        y += 1
    x += 1
"""
