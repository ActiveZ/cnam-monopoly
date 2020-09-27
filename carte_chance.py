
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


    def tirer_carte(self, j, proprietes):
        if len(self.jeu_carte) == 0: self._init_carte()

        carte = self.jeu_carte.pop(len(self.jeu_carte)-1)
        print("Tirez une carte 'Chance'\n", carte[0])
        if str(carte[1]).isalpha():
            if carte[1] == "reparationA": self._reparation(j, 40, 115, proprietes) # reparation1 ne passe pas isalpha
            elif carte[1] == "reparationB": self._reparation(j, 25, 100, proprietes)
            elif carte[1] == "depart":
                j.position = 0
                j.replay = True
            elif carte[1] == "paix":
                j.position = 39
                j.replay = True
            elif carte[1] == "henriMartin": # le _ ne passe pas le test isalpha
                if j.position > 24:
                    print("Vous passez par la case départ, vous recevez 200 €")
                    j.cash += 200
                j.position = 24
                j.replay = True
            elif carte[1] == "vilette":
                if j.position > 11:
                    print("Vous passez par la case départ, vous recevez 200 €")
                    j.cash += 200
                j.position = 11
                j.replay = True
            elif carte[1] == "lyon":
                if j.position > 15:
                    print("Vous passez par la case départ, vous recevez 200 €")
                    j.cash += 200
                j.position = 15
                j.replay = True
            elif carte[1] == "prison":
                j.position = 40
            elif carte[1] == "recul":
                j.position -= 3
                j.replay = True
            elif carte[1] == "libere":
                j.libere += 1
                self.libere_prison_dispo = False
                
        else:
            if carte[1] > 0: # rapporte de l'argent
                j.cash += carte[1]
            elif carte[1] < 0: # perd de l'argent
                j.payer(-carte[1])


    def _reparation(self, j, prix_maison, prix_hotel, proprietes):
        sum_maison = 0
        sum_hotel = 0
        for p in proprietes:
            if j.index_joueur == p["proprietaire"]:
                sum_maison += p["nb_maison"] * prix_maison
                sum_hotel += p["nb_hotel"] * prix_hotel
        j.payer(sum_hotel + sum_maison)