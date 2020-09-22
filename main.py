import os
# from donnees import *
from de import De
from joueur import Joueur


os.system('cls')
os.system('clear')

j = Joueur()

for i in range(10):
    print(j.lance_de())