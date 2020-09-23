# TODO
# mélange des cartes
#
#
#
#

import os
# from donnees import *
from joueur import Joueur

from data import proprietes
from data import gares
from data import compagnies

from propriete import Propriete
from gare import Gare
from compagnie import Compagnie


os.system('cls')
os.system('clear')

j = Joueur()

# p = Propriete(39)

# for i in range(100): print("Dés:", j.lance_de(), "n:", j.nb_double)
# for i in range(100): j.lance_de()


# p.fiche()

# for p in Propriete:
#     print(p)
def listing():
    for i in range(1, 40):
        # print("\ni:", i)
        if i in proprietes:
            p = Propriete(i)
            p.fiche()
        elif i in compagnies:
            c = Compagnie(i)
            c.fiche()
        elif i in gares:
            g = Gare(i)
            g.fiche()

#"""""""""""""""""""""""" MAIN """"""""""""""""""""""""""""""""""""""""

# listing()
while input("Souhaitez-vous quitter la partie (o/N) ? ") != "o":
    j.jouer()

    


