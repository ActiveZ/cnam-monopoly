# from de import De
from random import randint 


class Joueur:
    nb_joueur = 0


    def __init__(self):
        Joueur.nb_joueur += 1


    def lance_de(self):
        return randint(1,6) + randint(1,6)



