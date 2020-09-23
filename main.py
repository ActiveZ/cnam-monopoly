import os
# from donnees import *
from joueur import Joueur
from propriete import Propriete


os.system('cls')
os.system('clear')

j = Joueur()

# p = Propriete(39)

# for i in range(100): print("Dés:", j.lance_de(), "n:", j.nb_double)


# p.fiche()

# for p in Propriete:
#     print(p)

for i in range(1, 40):
    print("\ni:", i)
    try:
        p = Propriete(i)
        p.fiche()
    except:
        pass