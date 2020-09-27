from data import compagnies
from data import cases


class Compagnie:


    def __init__(self, index):
        # index est le numéro de case sur le plateau
        c = compagnies[index]
        self.nom = c["nom"]
        self.prix = c["prix"]
        self.hypotheque = c["hypotheque"]
        self.couleur = c["couleur"]
        self.proprietaire = c["proprietaire"]

    
    def fiche(self):
        print (
            "\nNom:", self.nom,
            "\nPrix:", self.prix,
            "\nValeur hypothèque:", self.hypotheque,
            "\nCouleur de la carte:", cases[self.couleur],
            "\nPropriétaire:", self.proprietaire,"\n"
        )