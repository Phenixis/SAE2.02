# coding: utf-8
""" 
Une classe Python pour creer et manipuler des graphes
"""

[5, 6] -> 'e6'

class Graphe(object):

    def __init__(self, graphe_dict=None):
        """ initialise un objet graphe.
	    Si aucun dictionnaire n'est
	    créé ou donné, on en utilisera un 
	    vide
        """
        if graphe_dict == None:
            graphe_dict = dict()
        self._graphe_dict = graphe_dict

    def __iter__(self):
        self._iter_obj = iter(self._graphe_dict)
        return self._iter_obj

    def __next__(self):
        """ Pour itérer sur les sommets du graphe """
        return next(self._iter_obj)

    def __str__(self):
        res = "sommets: "
        for k in self._graphe_dict.keys():
            res += str(k) + " "
        res += "\naretes: "
        for arete in self.__list_aretes():
            res += str(arete) + " "
        return res
    
    def aretes(self, sommet):
        """ retourne une liste de toutes les aretes d'un sommet"""
        return self._graphe_dict[sommet]

    def all_sommets(self):
        """ retourne tous les sommets du graphe """
        return self._graphe_dict.keys()

    def all_aretes(self):
        """ retourne toutes les aretes du graphe """
        return self.__list_aretes()

    def add_sommet(self, sommet):
        """
        Si le "sommet" n'set pas déjà présent
        dans le graphe, on rajoute au dictionnaire 
        une clé "sommet" avec une liste vide pour valeur. 
        Sinon on ne fait rien.
        """
        if sommet not in self.all_sommets():
            self._graphe_dict[sommet] = []

    def add_arete(self, arete):
        """
        l'arete est de  type set, tuple ou list;
        Entre deux sommets il peut y avoir plus
	    d'une arete (multi-graphe)
        """
        dep, arr = arete

        if dep in self.all_sommets():
            if arr not in self.aretes(dep):
                self._graphe_dict[dep].append(arr)
                self.add_arete([arr, dep])

    def __list_aretes(self):
        """
        Methode privée pour récupérer les aretes. 
	    Une arete est un ensemble (set)
        avec un (boucle) ou deux sommets.
        """
        # res = []
        # for sommet in self.all_sommets():
        #     for arete in self.aretes(sommet):
        #         res.append([sommet, arete])
        # return res
        return [[[sommet, arete] for arete in self.aretes(sommet)] for sommet in self.all_sommets()]

    def trouve_chaine(self, sommet_dep, sommet_arr, chain=None):
        chain = [sommet_dep] if chain is None else chain
        res = chain

        # print(chain)

        voisins = self.aretes(sommet_dep)
        i = 0
        while (i < len(voisins) and res[-1] != sommet_arr):
            voisin = voisins[i]
            if voisin not in chain:
                print(voisin)
                res = self.trouve_chaine(voisin, sommet_arr, chain + [voisin])
            i+=1
        
        return res


    def trouve_toutes_chaines(self, sommet_dep, sommet_arr, sommets=[]):
        res = []

        if (sommet_dep == sommet_arr):
            return [[sommet_dep]]
        else:
            for voisin in self.aretes(sommet_dep):
                if voisin not in sommets:
                    chemins = self.trouve_toutes_chaines(voisin, sommet_arr, sommets + [sommet_dep])
                    for chemin in chemins:
                        res.append([sommet_dep] + chemin)

        return res

    

graphe = {"A" :["C"],"B" : ["C", "E"],"C" : ["A", "B", "D", "E"],"D" : ["C"],"E" : ["C", "B"],"F" : []}
mygraph = Graphe(graphe)

# print(mygraph.aretes("A"))
# print(mygraph.all_sommets())
# print(mygraph.all_aretes())
# print(mygraph)

# print(mygraph.trouve_chaine("A", "D"))
mygraph.add_arete(["D", "E"])
print(mygraph.trouve_toutes_chaines("E", "A"))