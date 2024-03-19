# coding: utf-8
""" 
Une classe Python pour creer et manipuler des graphes
"""

class Chemin():

    def __init__(self):
        self.chemin = []
    
    def __str__(self):
        return str(self.chemin)
    
    def add_step(self, coor_case_dep: int, coor_case_arr: int):
        if self.chemin == [] or self.last_step()[1] == coor_case_dep:
            self.chemin.append([coor_case_dep, coor_case_arr])
        else:
            print(f"Le chemin n'est pas valide : la case de départ donnée({coor_case_dep}) n'est pas la case d'arrivée précédente({self.last_step()[1]}).")
    
    def last_step(self):
        return self.chemin[-1]

    def remove_last_step(self):
        self.chemin.pop()
    
    def debut(self):
        return self.chemin[0][0]

    def fin(self):
        return self.chemin[-1][-1]

    def isFromXToY(self, X: int, Y: int):
        return self.debut() == X and self.fin() == Y

# chem = Chemin()
# chem.add_step(0, 1)
# chem.add_step(1, 2)
# print(chem)
# chem.add_step(3, 4)
# print(chem.isFromXToY(0, 2))
# chem.remove_last_step()
# print(chem)