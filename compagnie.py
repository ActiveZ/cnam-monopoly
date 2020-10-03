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
        self.isHypotheque = c["isHypotheque"]

    
    def fiche(self):
        print (
            "Nom:", self.nom,
            "\nPrix:", self.prix,
            "\nValeur hypothèque:", self.hypotheque,
            "\nCouleur de la carte:", cases_data[self.couleur],
            "\nPropriétaire:", self.proprietaire,"\n"
        )


    def visite(self,j, joueurs): # le joueur j arrive sur ce terrain
        if self.isHypotheque or self.proprietaire == j.index_joueur: return

        if self.proprietaire == 0: # la compagnie n'appartient à personne
            choix = ""
            while choix not in ["1","2"]: choix = input("terrain libre --- 1: acheter 2: mettre aux enchères\n")
            if choix == "1": 
                if j.payer(self.prix):
                    j.terrains.append(j.position)
                    compagnies_data[j.position]["proprietaire"] = j.index_joueur
                else:
                    print("Vous n'avez pas assez d'argent ! Vous disposez de", j.cash, "€")
                    self.visite(j, joueurs)
            else: # enchères
                return

        else: # la compagnie appartient à un autre joueur
            # recherche du propriétaire du terrain
            for x in joueurs:
                if j.position in x.terrains: beneficiaire = x

            # calcul du montant du loyer
            loyer = j.dernier_tirage * 10 if compagnies_data[12]["proprietaire"] == compagnies_data[28]["proprietaire"] else j.dernier_tirage * 4

            print(j.nom,"vous devez",loyer,"€ à",beneficiaire.nom)
            j.payer(loyer,beneficiaire)