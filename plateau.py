from data import proprietes
from data import gares
from data import compagnies

from dice import Dice

from propriete import Propriete
from gare import Gare
from compagnie import Compagnie

from carte_chance import Carte_chance
from carte_communaute import Carte_communaute

from joueur import Joueur


class Game_board:

    # constructeur
    def __init__(self):
        self.dice = Dice()

        # instanciation des cartes
        self.carte_chance = Carte_chance()
        self.carte_communaute = Carte_communaute()

        # instanciation des cases terrain
        self.proprietes = proprietes
        self.gares = gares
        self.compagnies = compagnies

        self.j1 = Joueur()
        print("Début du jeu")


    def play(self):
        print("j1:", self.j1.nom_joueur, "argent:", self.j1.argent, "position:", self.j1.position)
        if self.j1.position != 40: # joueur est en prison
            self.dice.lancer(self.j1)
            if self.j1.position in [7,22,36]: self.carte_chance.tirer_carte(self.j1) #case carte chance
            if self.j1.position in [2,17,33]: self.carte_communaute.tirer_carte(self.j1) #case caisse de communauté

        self.j1.go()
        print("j1:", self.j1.nom_joueur, "argent:", self.j1.argent, "position:", self.j1.position)





#############################################################################
###########################  FONCTIONS POUR DEBUG ###########################
#############################################################################

    def list_all(self):
        print("****************\nListing complet")
        for i in range(1, 40):
            print("\ncase:", i)
            if i in self.proprietes:
                p = Propriete(i)
                p.fiche()
            elif i in self.compagnies:
                c = Compagnie(i)
                c.fiche()
            elif i in self.gares:
                g = Gare(i)
                g.fiche()


    def list_proprietes(self):
        print("****************\nListing propriétés")
        for i in range(1, 40):
            if i in self.proprietes:
                print("\ncase:", i)
                p = Propriete(i)
                p.fiche()


    def list_gares(self):
        print("****************\nListing gares")
        for i in range(1, 40):
            if i in self.gares:
                print("\ncase:", i)
                g = Gare(i)
                g.fiche()


    def list_compagnies(self):
        print("****************\nListing compagnies")
        for i in range(1, 40):
            if i in self.compagnies:
                print("\ncase:", i)
                c = Compagnie(i)
                c.fiche()


    # listing des cartes chance
    def list_chance(self): 
        print("****************\nListing cartes chance")
        for i in range(len(self.carte_chance.jeu_carte)): print(self.carte_chance.jeu_carte.pop(len(self.carte_chance.jeu_carte)-1)[0])


    # listing des cartes caisse de communauté
    def list_communaute(self):
        print("****************\nListing cartes caisse de communauté")
        for i in range(len(self.carte_communaute.jeu_carte)): print(self.carte_communaute.jeu_carte.pop(len(self.carte_communaute.jeu_carte)-1)[0])