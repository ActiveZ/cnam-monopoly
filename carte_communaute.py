
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
        # print("\nNouveau jeu cartes caisse de communauté\n")


    def tirer_carte(self, j, joueurs):
        if len(self.jeu_carte) == 0: self._init_carte()

        carte = self.jeu_carte.pop(len(self.jeu_carte)-1)
        print("Tirez une carte 'Caisse de Communauté'\n", carte[0])
        if str(carte[1]).isalpha():
            if carte[1] == "anniversaire":
                for x in joueurs: 
                    if x != j: x.payer(10,j)
            elif carte[1] == "amendeChance": # le _ ne passe pas le test isalpha
                self._amende_chance(j)
            elif carte[1] == "belleville":
                j.position = 1
                j.replay = True
            elif carte[1] == "prison":
                j.position = 40
            elif carte[1] == "depart":
                j.position = 0
                j.replay = True
            elif carte[1] == "libere":
                j.libere += 2
                self.libere_prison_dispo = False

        else:
            if carte[1] > 0: # rapporte de l'argent
                j.cash += carte[1]
            elif carte[1] < 0: # perd de l'argent
                j.payer(-carte[1])
    

    def _amende_chance(self,j):
        choix = ""
        while choix not in ["1","2"]:
            choix = input("1: payer une amende de 10 € ou 2: tirez une carte chance\n")
        if choix == "1": j.payer(10)
        else: j.retire_chance = True
