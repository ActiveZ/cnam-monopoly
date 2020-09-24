# remettre carte libéré de prison à la fin du paquet (chance ou communauté) après utilisation (ttt nom du paquet)

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
        self.index_joueur = Joueur.nb_joueur
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
        if self.position == 40: # joueur en prison
            self.prison()
            return


        self.position += self.lance_de()

        if self.position > 39:
            self.position -= 40 # case départ = 0
            self.case_depart()


        # analyse de la case d'arrivée
        if self.position in proprietes: # terrain
            p = Propriete(self.position)
            p.fiche()
        
        elif self.position in compagnies: # électricité/eau
            c = Compagnie(self.position)
            c.fiche()

        elif self.position in gares: # gare
            g = Gare(self.position)
            g.fiche()

        elif self.position in [0,10,20]: # case départ, simple visite, parc gratuit
            pass

        elif self.position == 30: # allez en prison
            print("Allez directement en prison")
            self.position = 40

        elif self.position  == 4: # impôts
            print("Taxe sur le revenu: 200 €")
            self.paye(200,-1) 

        elif self.position == 38: # taxe luxe
            print ("Taxe de luxe: 100 €")
            self.paye(100,-1) 

        elif self.position in [7,22,36]: self.chance(self.index_joueur)

        elif self.position in [2,17,23]: self.communaute(self.index_joueur)

        else: # pour debug
            print("Erreur de case")
            exit()


    def case_depart(self):
        self.argent += 200
        print("Vous avez reçu 200 € !")


    def prison(self):
        pass

    def paye(self, montant, beneficiaire): # beneficiaire -1 => banque, sinon, index joueur
        if self.argent >= montant:
            self.argent -= montant
        else:
            pass


    def chance(self, index_joueur):
        # carte_chance.tirer_carte()
        print("Tirez une carte 'Chance'")


    def communaute(self, index_joueur):
        print("Tirez une carte 'Caisse de Communauté")