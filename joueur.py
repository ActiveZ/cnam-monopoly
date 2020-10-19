import pygame
from random import shuffle
from data import cases_data, pions_data
from data import proprietes_data
from data import gares_data
from data import compagnies_data


class Joueur:
    nb_joueur = 0 # variable de classe incrémentée à chaque instanciation de joueur


    def __init__(self):
        Joueur.nb_joueur += 1
        self.index_joueur = Joueur.nb_joueur
        self.cash = 15000
        self.position = 0 # numéro de la case du joueur
        self.nb_double = 0
        self.nom = "joueur" + str(Joueur.nb_joueur)
        self.replay = False # si double ou si déplacement par carte
        self.retire_chance = False # pour le cas de l'amende ou retire une carte chance
        self.libere = 0 # carte libéré de prison: 1:chance, 2:communauté, 3: les deux
        self.tour_prison = 0 # nb de tour en prison
        self.dernier_tirage = 0 # valeur du dernier tirage de dé, utilisé pour calcul compagnie
        self.terrains = [] # tableau des cases que possède le joueur (ex: 5 -> gare montparnasse) => faire un tableau d'objet ?
        # self.is_human = True
        
        # initialisation graphique du joueur
        self.image = self._attrib_pion()
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect.center = (cases_data[0]["x"], cases_data[0]["y"]) # case départ
        self.velocity = [0, 0] # [x, y]    


    def payer(self, montant, beneficiaire = None): # beneficiaire = none => banque, sinon => joueur
        # retourne true si paiement effectué, false sinon
        if self.patrimoine() - montant <=0:
            print('Fin de partie, vous avez perdu, gros looser !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            # TODO fin de partie varie selon la personne a payer (donner le reste a la banque ou a un autre joueur)
        else:        
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


    def patrimoine(self):
        terrain_hypo = []
        montant_maison = []
        montant_hotel = []
        pat = 0
        for t in self.terrains:
            if proprietes_data[t]["isHypotheque"] is not None:
                if proprietes_data[t]["isHypotheque"]==False:
                    terrain_hypo.append(proprietes_data[t]["hypotheque"])
                    montant_maison.append(proprietes_data[t]['nb_maison'] * (proprietes_data[t]['prix_maison']/2)  )
                    montant_hotel.append(proprietes_data[t]['nb_hotel'] * (proprietes_data[t]['prix_maison']*2.5)  ) # 5 maison / 2 = 2.5
                break
            elif gares_data[t]["isHypotheque"]is not None:
                if gares_data[t]["isHypotheque"]==False:
                    terrain_hypo.append(gares_data[t]["hypotheque"])
                break
            elif compagnies_data[t]["isHypotheque"]is not None:
                if compagnies_data[t]["isHypotheque"]==False:
                    terrain_hypo.append(compagnies_data[t]["hypotheque"])
                break
        pat = sum(terrain_hypo)   + sum(montant_maison) + sum(montant_hotel) + self.cash
        # print(terrain_hypo)
        # print(montant_maison)
        # print(montant_hotel)
        # print(pat)
        return pat


    def construire(self):
        couleur_terrain = 0
        tab_couleur_terrain = []
        brun = 0
        bleu_clair = 0
        violet = 0
        orange = 0
        rouge = 0
        jaune = 0
        vert = 0
        bleu_fonce = 0
        for t in self.terrains:
            if compagnies_data[t] is not None:
                break
            elif gares_data[t] is not None:
                break
            elif proprietes_data[t] is not None:
                couleur_terrain = proprietes_data[t]['couleur']
                #print(couleur_terrain)
                tab_couleur_terrain.append(couleur_terrain)
                #print(tab_couleur_terrain)
            else:
                break
        brun =tab_couleur_terrain.count(43)
        bleu_clair = tab_couleur_terrain.count(44)
        violet =tab_couleur_terrain.count(45)
        orange = tab_couleur_terrain.count(46)
        rouge = tab_couleur_terrain.count(47)
        jaune = tab_couleur_terrain.count(48)
        vert = tab_couleur_terrain.count(49)
        bleu_fonce = tab_couleur_terrain.count(50)
        print('brun:',brun)
        print('bc:',bleu_clair)
        print('violet:',violet)
        print('orange:',orange)
        print('rouge:',rouge)
        print('jaune:',jaune)
        print('vert',vert)
        print('bf:',bleu_fonce)
            # if brun == 2 or bleu_fonce == 2: 
            #     print("Voulez vous construire ?")
            # elif bleu_clair == 3 or violet == 3 or rouge ==3 or orange == 3 or jaune == 3 or vert == 3:
            #     print("voulez vous construire ? ")
            # else :
            #     print ("Vous ne pouvez pas construire.")



            
            
