from data import proprietes
from data import cases


class Propriete:


    def __init__(self, index):
        # index est le numéro de case sur le plateau
        p = proprietes[index]
        self.nom = p["nom"]
        self.prix = p["prix"]
        self.loyer = p["loyer"]
        self.hypotheque = p["hypotheque"]
        self.maison = p["maison"]
        self.couleur = p["couleur"]
        self.proprietaire = p["proprietaire"]

    
    def fiche(self):
        print (
            "\nNom:", self.nom,
            "\nPrix:", self.prix,
            "\nLoyers:", self.loyer,
            "\nValeur hypothèque:", self.hypotheque,
            "\nPrix d'une maison:", str(self.maison),
            "\nCouleur de la carte:", cases[self.couleur],
            "\nPropriétaire:", self.proprietaire
        )

