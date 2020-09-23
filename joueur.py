from random import randint
# from dice import De


class Joueur:
    nb_joueur = 0


    def __init__(self):
        Joueur.nb_joueur += 1
        self.nb_double = 0


    def lance_de(self):
        d1 = randint(1,6)
        d2 = randint(1,6)
        self.nb_double = 0 if d1 != d2 else self.nb_double + 1
        # print("d1: {}".format(d1) + ", d2: {}".format(d2) + ", n: {}".format(self.nb_double))
        return d1 + d2



