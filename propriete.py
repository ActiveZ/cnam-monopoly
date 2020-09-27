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
        self.prix_maison = p["prix_maison"]
        self.couleur = p["couleur"]
        self.proprietaire = p["proprietaire"]
        self.nb_maison = p["nb_maison"]
        self.nb_hotel = p["nb_hotel"]

    
    def fiche(self):
        print (
            "Nom:", self.nom,
            "\nPrix:", self.prix,
            "\nLoyers:", self.loyer,
            "\nValeur hypothèque:", self.hypotheque,
            "\nPrix d'une maison:", str(self.prix_maison),
            "\nCouleur de la carte:", cases[self.couleur],
            "\nPropriétaire:", self.proprietaire,
            "\nNombre de maison:", self.nb_maison,
            "\nNombre d'hôtel:", self.nb_hotel,"\n"
        )

