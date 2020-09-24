# gérer si la carte libéré de prison est avec un joueur lors de init carte

from data import carte_caisse_communaute
from random import shuffle

class Carte_communaute:


    def __init__(self):
        self.libere_prison_dispo = True # la carte libéré de prison n'est pas prise par un joueur 
        self._init_carte()


    def _init_carte(self):
        self.jeu_carte = carte_caisse_communaute.copy()
        if not self.libere_prison_dispo: self.jeu_carte.pop(15)
        shuffle(self.jeu_carte)
        print("\nNouveau jeu cartes caisse de communauté\n")


    def tirer_carte(self):
        if len(self.jeu_carte) == 0: self._init_carte()
        carte = self.jeu_carte.pop(len(self.jeu_carte)-1)
        print(carte[0])