import pygame
from display import Display

from data import proprietes_data, gares_data, compagnies_data

from dice import Dice

from propriete import Propriete
from gare import Gare
from compagnie import Compagnie

from carte_chance import Carte_chance
from carte_communaute import Carte_communaute

from prison import Prison

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

        # instanciation des cases propriété
        self.proprietes = []
        for i in proprietes_data: self.proprietes.append(Propriete(i))
        # for p in self.proprietes: p.fiche()

        # instanciation des cases gare
        self.gares = []
        for i in gares_data: self.gares.append(Gare(i))
        # for g in self.gares: g.fiche()

        # instanciation des cases compagnie
        self.compagnies = []
        for i in compagnies_data: self.compagnies.append(Compagnie(i))
        # for c in self.compagnies: c.fiche()

        # instanciation de la prison
        self.prison = Prison()

        # tableau des joueurs
        self.joueurs = []

        # initialisation graphique du plateau
        self.display = Display()


    def init_game(self):
        print("************************************\n" + 
             "* BIENVENUE A LA TABLE DE MONOPOLY *\n" +
             "************************************\n")
        j = Joueur()
        self.joueurs.append(j)
        j = Joueur()
        self.joueurs.append(j)
        print("Il y a", len(self.joueurs), "joueurs à la table\n")
        while len(self.joueurs) < 5 and input("Souhaitez-vous ajouter un nouveau joueur (max = 5) (o/N) ? ").lower() == "o":
            j = Joueur()
            self.joueurs.append(j)
            print("Il y a", len(self.joueurs), "joueurs à la table\n")
        print("\nDébut de la partie\n")
        # affichage des pions des joueurs sur le plateau
        self.display.display_players(self.joueurs)
        
        
    def play(self):
        for j in self.joueurs:
            j.fiche()
            if j.position == 40: #joueur en prison
                self.prison.libere(j,self.carte_chance,self.carte_communaute)
                if j.position != 40: self.case_arrivee(j) # le joueur a été libéré
            else: # si joueur n'est pas en prison
                self.go(j, self.dice.lancer(j))
                self.case_arrivee(j)
                while j.nb_double > 0:  # tant le joueur a fait un double, il rejoue
                    print(j.nom, "rejoue")
                    self.go(j, self.dice.lancer(j))
                    self.case_arrivee(j)


    # analyse de la case d'arrivée
    def case_arrivee(self, j): # joueur j
        if j.position == 0: # case départ = 0
            j.cash += 200
            print("Vous avez reçu 200 € !")

        elif j.position in [7,22,36]:
            self.carte_chance.tirer_carte(j) # carte chance
            if j.replay:
                j.replay = False
                self.case_arrivee(j) # en cas de carte de déplacement

        elif j.position in [2,17,33]: 
            self.carte_communaute.tirer_carte(j, self.joueurs) # carte caisse de communauté
            if j.replay:
                j.replay = False
                self.case_arrivee(j) # en cas de carte de déplacement
            if j.retire_chance:
                j.retire_chance = False
                self.carte_chance.tirer_carte(j) # si ne paye pas l'amende et préfere tirer chance

        elif j.position in proprietes_data: # terrain
            p = Propriete(j.position)
            p.fiche()
            p.visite(j, self.joueurs)
        
        elif j.position in compagnies_data: # électricité/eau
            c = Compagnie(j.position)
            c.fiche()
            c.visite(j, self.joueurs)

        elif j.position in gares_data: # gare
            g = Gare(j.position)
            g.fiche()
            g.visite(j, self.joueurs)

        elif j.position in [0,10,20]: # case départ, simple visite, parc gratuit
            if j.position == 0: print("Case départ")
            elif j.position == 10: print("Simple visite")
            elif j.position == 20: print("Parc gratuit")

        elif j.position == 30: # allez en prison
            print("Allez directement en prison")
            j.position = 40
            j.nb_double = 0 # cas du joueur qui arrive ici par un double => ne rejoue pas

        elif j.position  == 4: # impôts
            print("Taxe sur le revenu: 200 €")
            j.payer(200) 

        elif j.position == 38: # taxe luxe
            print ("Taxe de luxe: 100 €")
            j.payer(100) 

        else: # pour debug
            print("Erreur de case")
            exit()


    # déplacement du joueur j et maj graphique du plateau
    def go(self, j, dice):
        progress = dice # le joueur progresse de la valeur du lancé de dés
        self.display.update_board(j, progress, self.joueurs) # visualisation du déplacement sur le plateau

        j.position += progress # avance de la valeur de dice
        if j.position > 39: j.position -= 40 # case départ = 0




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
        # for i in range(len(self.carte_chance.jeu_carte)): print(self.carte_chance.jeu_carte.pop(len(self.carte_chance.jeu_carte)-1)[0])
        for c in self.carte_chance.jeu_carte: print(self.carte_chance.jeu_carte[c])


    # listing des cartes caisse de communauté
    def list_communaute(self):
        print("****************\nListing cartes caisse de communauté")
        # for i in range(len(self.carte_communaute.jeu_carte)): print(self.carte_communaute.jeu_carte.pop(len(self.carte_communaute.jeu_carte)-1)[0])
        for c in self.carte_communaute.jeu_carte: print(self.carte_communaute.jeu_carte[c])
