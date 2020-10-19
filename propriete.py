from data import proprietes_data
from data import cases_data


class Propriete:


    def __init__(self, index):
        # index est le numéro de case sur le plateau
        p = proprietes_data[index]
        self.nom = p["nom"]
        self.prix = p["prix"]
        self.loyer = p["loyer"]
        self.hypotheque = p["hypotheque"]
        self.prix_maison = p["prix_maison"]
        self.couleur = p["couleur"]
        self.proprietaire = p["proprietaire"]
        self.nb_maison = p["nb_maison"]
        self.nb_hotel = p["nb_hotel"]
        self.isHypotheque = p["isHypotheque"]

    
    def fiche(self):
        print (
            "Nom:", self.nom,
            "\nPrix:", self.prix,
            "\nLoyers:", self.loyer,
            "\nValeur hypothèque:", self.hypotheque,
            "\nPrix d'une maison:", str(self.prix_maison),
            "\nCouleur de la carte:", cases_data[self.couleur],
            "\nPropriétaire:", self.proprietaire,
            "\nNombre de maison:", self.nb_maison,
            "\nNombre d'hôtel:", self.nb_hotel,"\n"
        )
        

    def visite(self,j, joueurs): # le joueur j arrive sur ce terrain
        if self.isHypotheque or self.proprietaire == j.index_joueur: return

        if self.proprietaire == 0: # le terrain n'appartient à personne
            choix = ""
            while choix not in ["1","2"]: choix = input("terrain libre --- 1: acheter 2: mettre aux enchères ")
            if choix == "1": 
                if j.payer(self.prix):
                    j.terrains.append(j.position)
                    proprietes_data[j.position]["proprietaire"] = j.index_joueur
                else:
                    print("Vous n'avez pas assez d'argent ! Vous disposez de", j.cash, "€")
                    self.visite(j, joueurs)
            else: # enchères
                return

        else: # le terrain appartient à un autre joueur
            # recherche du propriétaire du terrain
            for x in joueurs:
                if j.position in x.terrains: beneficiaire = x

            # calcul du montant du loyer

            # terrain nu
            if self.nb_maison == 0 and self.nb_hotel == 0: 
                loyer = self.loyer[0]
                # double si joueur possède toute la couleur
                count_color = 0 # compte les cartes de la même couleur
                count_owner = 0 # compte le nb carte de cette couleur qui appartiennent au joueur de la case visitée
                for i in proprietes_data:
                    if proprietes_data[i]["couleur"] == self.couleur: count_color += 1
                    if proprietes_data[i]["couleur"] == self.couleur and proprietes_data[i]["proprietaire"] == self.proprietaire: count_owner += 1
                if count_owner == count_color: loyer *= 2

            # avec maisons
            elif self.nb_maison > 0: loyer = self.loyer[self.nb_maison]

            # avec un hôtel
            elif self.nb_hotel > 0: loyer = self.loyer[5]

            print(j.nom,"vous devez",loyer,"€ à",beneficiaire.nom)
            j.payer(loyer,beneficiaire)

        
