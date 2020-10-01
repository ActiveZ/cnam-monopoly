from data import compagnies_data
from data import cases_data


class Compagnie:


    def __init__(self, index):
        # index est le numéro de case sur le plateau
        c = compagnies_data[index]
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
            "\nCouleur de la carte:", cases_data[self.couleur],
            "\nPropriétaire:", self.proprietaire,"\n"
        )