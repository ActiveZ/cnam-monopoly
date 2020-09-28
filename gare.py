from data import gares
from data import cases


class Gare:


    def __init__(self, index):
        # index est le numéro de case sur le plateau
        g = gares[index]
        self.nom = g["nom"]
        self.prix = g["prix"]
        self.loyer = g["loyer"]
        self.hypotheque = g["hypotheque"]
        self.couleur = g["couleur"]
        self.proprietaire = g["proprietaire"]
        self.is_hypotheque = g["is_hypotheque"]

    
    def fiche(self):
        print (
            "\nNom:", self.nom,
            "\nPrix:", self.prix,
            "\nLoyer", self.loyer,
            "\nValeur hypothèque:", self.hypotheque,
            "\nCouleur de la carte:", cases[self.couleur],
            "\nPropriétaire:", self.proprietaire,
            "\nHypothéquée:", self.is_hypotheque,"\n"
        )


    def visite(self,j): # le joueur j arrive sur ce terrain
        if self.is_hypotheque or self.proprietaire == j.index_joueur: return

        if self.proprietaire == 0:
            

