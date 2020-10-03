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
            "Nom:", self.nom,
            "\nPrix:", self.prix,
            "\nLoyer", self.loyer,
            "\nValeur hypothèque:", self.hypotheque,
            "\nCouleur de la carte:", cases_data[self.couleur],
            "\nPropriétaire:", self.proprietaire,
            "\nHypothéquée:", self.isHypotheque,"\n"
        )


    def visite(self,j, joueurs): # le joueur j arrive sur ce terrain
        if self.isHypotheque or self.proprietaire == j.index_joueur: return

        if self.proprietaire == 0: # la gare n'appartient à personne
            choix = ""
            while choix not in ["1","2"]: choix = input("terrain libre --- 1: acheter 2: mettre aux enchères ")
            if choix == "1": 
                if j.payer(self.prix):
                    j.terrains.append(j.position)
                    gares_data[j.position]["proprietaire"] = j.index_joueur
                else:
                    print("Vous n'avez pas assez d'argent ! Vous disposez de", j.cash, "€")
                    self.visite(j, joueurs)
            else: # enchères
                return

        else: # la gare appartient à un autre joueur
            # recherche du propriétaire du terrain
            for x in joueurs:
                if j.position in x.terrains: beneficiaire = x

            # calcul du montant du loyer
            count = 0
            for i in gares_data: 
                if gares_data[i]["proprietaire"] == self.proprietaire: count += 1
            loyer = gares_data[j.position]["loyer"][count - 1]

            print(j.nom,"vous devez",loyer,"€ à",beneficiaire.nom)
            j.payer(loyer,beneficiaire)



