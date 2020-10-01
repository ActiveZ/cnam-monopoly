from data import gares_data
from data import cases_data


class Gare:


    def __init__(self, index):
        # index est le numéro de case sur le plateau
        g = gares_data[index]
        self.nom = g["nom"]
        self.prix = g["prix"]
        self.loyer = g["loyer"]
        self.hypotheque = g["hypotheque"]
        self.couleur = g["couleur"]
        self.proprietaire = g["proprietaire"]
        self.isHypotheque = g["isHypotheque"]

    
    def fiche(self):
        print (
            "\nNom:", self.nom,
            "\nPrix:", self.prix,
            "\nLoyer", self.loyer,
            "\nValeur hypothèque:", self.hypotheque,
            "\nCouleur de la carte:", cases_data[self.couleur],
            "\nPropriétaire:", self.proprietaire,
            "\nHypothéquée:", self.isHypotheque,"\n"
        )


    def visite(self,j): # le joueur j arrive sur ce terrain
        if self.isHypotheque or self.proprietaire == j.index_joueur: return

        if self.proprietaire == 0: # la gare n'appartient à personne
            choix = ""
            while choix not in ["1","2"]: choix = input("terrain libre --- 1: acheter 2: mettre aux enchères\n")
            if choix == "1": 
                if j.payer(self.prix):
                    self.proprietaire = j.index_joueur
            else: # enchères
                return

        else: # la gare appartient à un autre joueur
            loyer = gares_data[5]["loyer"][gares_data["proprietaire"].count(self.proprietaire)]
            print(j.nom,"vous devez",loyer,"€ à",self.proprietaire)
            j.payer(loyer,self.proprietaire)



