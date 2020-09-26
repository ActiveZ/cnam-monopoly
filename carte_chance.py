# gérer si la carte libéré de prison est avec un joueur lors de init carte

from data import carte_chance
from random import shuffle

class Carte_chance:


    def __init__(self):
        self.libere_prison_dispo = True # la carte libéré de prison n'est pas prise par un joueur 
        self._init_carte()


    def _init_carte(self):
        self.jeu_carte = carte_chance.copy() # vérifier si copy est utile
        if not self.libere_prison_dispo: self.jeu_carte.pop(15)
        shuffle(self.jeu_carte)
        # print("\nNouveau jeu cartes chance\n")


    def tirer_carte(self, joueur):
        if len(self.jeu_carte) == 0: self._init_carte()

        carte = self.jeu_carte.pop(len(self.jeu_carte)-1)
        print("Tirez une carte 'Chance'\n", carte[0])
        # print(carte[0])
        if int(carte[1]) > 0: # rapporte de l'argent
            joueur.argent += carte[1]
        if int(carte[1] < 0): # perd de l'argent
            joueur.paye(-carte[1])