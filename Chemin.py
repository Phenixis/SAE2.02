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
            print("Le chemin n'est pas valide : la case de départ donnée n'est pas la case d'arrivée précédente.")
    
    def last_step(self):
        return self.chemin[-1]

    def remove_last_step(self):
        self.chemin.pop()

chem = Chemin()