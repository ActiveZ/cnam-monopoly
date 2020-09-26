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

    
    def go(self):
        if self.position == 40: # joueur en prison
            self.prison()
            return

        # analyse de la case d'arrivée

        if self.position == 0:# case départ = 0
            self.argent += 200
            print("Vous avez reçu 200 € !")

        elif self.position in proprietes: # terrain
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
            
        elif self.position in [7,22,36,2,17,33]: pass # case caisse de communauté ou chance

        # elif self.position in [7,22,36]: self.chance(self.index_joueur) #case carte chance

        # elif self.position in [2,17,33]: self.communaute(self.index_joueur) #case caisse de communauté

        else: # pour debug
            print("Erreur de case")
            exit()



    def prison(self):
        pass


    def paye(self, montant, beneficiaire = None): # beneficiaire = none => banque, sinon => joueur
        if self.argent >= montant:
            self.argent -= montant
        else:
            pass
