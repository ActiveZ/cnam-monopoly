from data import proprietes
from data import gares
from data import compagnies

from dice import Dice

from propriete import Propriete
from gare import Gare
from compagnie import Compagnie

from carte_chance import Carte_chance
from carte_communaute import Carte_communaute

from joueur import Joueur


class Game_board:

    # constructeur
    def __init__(self):
        self.nb_maison_dispo = 32
        self.nb_hotel_dispo = 12

        self.dice = Dice()

        # instanciation des cartes
        self.carte_chance = Carte_chance()
        self.carte_communaute = Carte_communaute()

        # instanciation des cases terrain
        self.proprietes = proprietes
        self.gares = gares
        self.compagnies = compagnies

        # self.nb_joueur = 2
        self.joueurs = []


    def init_game(self):
        print("************************************\n" + 
             "* BIENVENUE A LA TABLE DE MONOPOLY *\n" +
             "************************************\n")

        j = Joueur()
        self.joueurs.append(j)
        j = Joueur()
        self.joueurs.append(j)
        print("Il y a", len(self.joueurs), "joueurs à la table\n")
        while len(self.joueurs) < 4 and input("Souhaitez-vous ajouter un nouveau joueur (max = 4) (o/N) ? ").lower() == "o":
            j = Joueur()
            self.joueurs.append(j)
            print("Il y a", len(self.joueurs), "joueurs à la table\n")
        print("Début de la partie\n")
        for j in self.joueurs:
            j.fiche()
        
        
    def play(self):
        for j in self.joueurs:
            if j.position == 40: j.position = 10
            if j.position != 40: # si joueur n'est pas en prison
                j.go(self.dice.lancer(j))
                self.case_arrivee(j)
            j.fiche()


    # analyse de la case d'arrivée
    def case_arrivee(self, j): # joueur j
        if j.position == 0: # case départ = 0
            j.cash += 200
            print("Vous avez reçu 200 € !")

        elif j.position in [7,22,36]:
            self.carte_chance.tirer_carte(j, self.proprietes) # case carte chance
            if j.replay:
                j.replay = False
                self.case_arrivee(j) # en cas de carte de déplacement

        elif j.position in [2,17,33]: 
            self.carte_communaute.tirer_carte(j, self.joueurs) # case caisse de communauté
            if j.replay:
                j.replay = False
                self.case_arrivee(j) # en cas de carte de déplacement
            if j.retire_chance:
                j.retire_chance = False
                self.carte_chance.tirer_carte(j, self.proprietes) # si ne paye pas l'amende et préfere tirer chance

        elif j.position in proprietes: # terrain
            p = Propriete(j.position)
            p.fiche()
        
        elif j.position in compagnies: # électricité/eau
            c = Compagnie(j.position)
            c.fiche()

        elif j.position in gares: # gare
            g = Gare(j.position)
            g.fiche()

        elif j.position in [0,10,20]: # case départ, simple visite, parc gratuit
            if j.position == 0: print("Case départ")
            elif j.position == 10: print("Simple visite")
            elif j.position == 20: print("Parc gratuit")

        elif j.position == 30: # allez en prison
            print("Allez directement en prison")
            j.position = 40

        elif j.position  == 4: # impôts
            print("Taxe sur le revenu: 200 €")
            j.payer(200) 

        elif j.position == 38: # taxe luxe
            print ("Taxe de luxe: 100 €")
            j.payer(100) 

        else: # pour debug
            print("Erreur de case")
            exit()



#############################################################################
###########################  FONCTIONS POUR DEBUG ###########################
#############################################################################

    def list_all(self):
        print("****************\nListing complet")
        for i in range(1, 40):
            print("\ncase:", i)
            if i in self.proprietes:
                p = Propriete(i)
                p.fiche()
            elif i in self.compagnies:
                c = Compagnie(i)
                c.fiche()
            elif i in self.gares:
                g = Gare(i)
                g.fiche()


    def list_proprietes(self):
        print("****************\nListing propriétés")
        for i in range(1, 40):
            if i in self.proprietes:
                print("\ncase:", i)
                p = Propriete(i)
                p.fiche()


    def list_gares(self):
        print("****************\nListing gares")
        for i in range(1, 40):
            if i in self.gares:
                print("\ncase:", i)
                g = Gare(i)
                g.fiche()


    def list_compagnies(self):
        print("****************\nListing compagnies")
        for i in range(1, 40):
            if i in self.compagnies:
                print("\ncase:", i)
                c = Compagnie(i)
                c.fiche()


    # listing des cartes chance
    def list_chance(self): 
        print("****************\nListing cartes chance")
        for i in range(len(self.carte_chance.jeu_carte)): print(self.carte_chance.jeu_carte.pop(len(self.carte_chance.jeu_carte)-1)[0])


    # listing des cartes caisse de communauté
    def list_communaute(self):
        print("****************\nListing cartes caisse de communauté")
        for i in range(len(self.carte_communaute.jeu_carte)): print(self.carte_communaute.jeu_carte.pop(len(self.carte_communaute.jeu_carte)-1)[0])