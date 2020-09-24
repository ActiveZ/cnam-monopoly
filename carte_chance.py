from data import carte_chance
from random import shuffle

class Carte_chance:


    def __init__(self):
        self._init_carte()


    def _init_carte(self):
        self.jeu_carte = carte_chance.copy()
        shuffle(self.jeu_carte)
        print("\nNouveau jeu cartes chance\n")


    def tirer_carte(self):
        if len(self.jeu_carte) == 0: self._init_carte()
        carte = self.jeu_carte.pop(len(self.jeu_carte)-1)
        print(carte[0])