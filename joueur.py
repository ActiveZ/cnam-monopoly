from random import randint

from data import cases
from data import proprietes
from data import compagnies
from data import gares

from propriete import Propriete
from compagnie import Compagnie
from gare import Gare
# from dice import De


class Joueur:
    nb_joueur = 0


    def __init__(self):
        Joueur.nb_joueur += 1
        self.argent = 1500
        self.position = 0 # numéro de la case du joueur
        self.nb_double = 0
        self.nom_joueur = "joueur" + str(Joueur.nb_joueur)


    # tirage du dé
    def lance_de(self):
        d1 = randint(1,6)
        d2 = randint(1,6)
        # ajoute 1 à nb_double si tire 1 double et raz sinon
        self.nb_double = 0 if d1 != d2 else self.nb_double + 1

        print(self.nom_joueur, "lance les dés et fait",d1, "et", d2, "double:", self.nb_double)
        if self.nb_double == 3:
            print("En prison !")
            self.nb_double = 0
        return d1 + d2

    
    def jouer(self):
        self.position += self.lance_de()

        if self.position > 39:
            self.position -= 40 # case départ = 0
            self.case_depart()

        # print(cases[self.position], self.position)

        if self.position in proprietes:
            p = Propriete(self.position)
            p.fiche()
        
        elif self.position in compagnies: # électricité/eau
            c = Compagnie(self.position)
            c.fiche()

        elif self.position in gares:
            g = Gare(self.position)
            g.fiche()

        else: #impots, caisses, simple visite, parc gratuit, allez en prison, taxe luxe, case départ
            pass

    def case_depart(self):
        self.argent += 200
        print("Vous avez reçu 200 € !")