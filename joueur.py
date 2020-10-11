import pygame
from random import shuffle
from data import cases_data, pions_data


class Joueur:
    nb_joueur = 0 # variable de classe incrémentée à chaque instanciation de joueur


    def __init__(self):
        Joueur.nb_joueur += 1
        self.index_joueur = Joueur.nb_joueur
        self.cash = 1500
        self.position = 0 # numéro de la case du joueur
        self.nb_double = 0
        self.nom = "joueur" + str(Joueur.nb_joueur)
        self.replay = False # si double ou si déplacement par carte
        self.retire_chance = False # pour le cas de l'amende ou retire une carte chance
        self.libere = 0 # carte libéré de prison: 1:chance, 2:communauté, 3: les deux
        self.tour_prison = 0 # nb de tour en prison
        self.dernier_tirage = 0 # valeur du dernier tirage de dé, utilisé pour calcul compagnie
        self.terrains = [] # tableau des cases que possède le joueur (ex: 5 -> gare montparnasse)
        # self.is_human = True
        
        # initialisation graphique du joueur
        self.image = self._attrib_pion()
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect.center = (cases_data[0]["x"], cases_data[0]["y"]) # case départ
        self.velocity = [0, 0] # [x, y]    


    def payer(self, montant, beneficiaire = None): # beneficiaire = none => banque, sinon => joueur
        # retourne true si paiement effectué, false sinon
        if self.cash >= montant:
            self.cash -= montant
            if beneficiaire is not None: beneficiaire.cash += montant
            return True

        else: # pas assez d'argent
            return False


    def fiche(self):
        txt = "-------------------------------------------\n"
        # txt += "index: " + str(self.index_joueur) + "  "
        txt += "Joueur: " + str(self.nom) + "  Argent: " + str(self.cash) + "  Position: " + str(self.position)
        if self.nb_double > 0: txt += "  Double:" + str(self.nb_double)
        txt += "\n-------------------------------------------"
        print(txt)


    # met à jour le pion du joueur sur le plateau
    def _update(self):
        self.rect.move_ip(*self.velocity)


    # attibution aléatoire d'un pion au joueur
    def _attrib_pion(self):
        shuffle(pions_data)
        return pygame.image.load("images/" + pions_data.pop() + ".png")