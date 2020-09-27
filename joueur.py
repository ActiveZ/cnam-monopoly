# remettre carte libéré de prison à la fin du paquet (chance ou communauté) après utilisation (ttt nom du paquet)


class Joueur:
    nb_joueur = 0


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
    

    def go(self, dice): # avance de la valeur de dice
        # if self.position == 40: # joueur en prison, ttt a part
        #     self.prison()
        #     return

        self.position += dice # avance de la valeur de dice
        if self.position > 39: self.position -= 40 # case départ = 0


    def prison(self, carte_chance, carte_communaute):
        self.position = 10 # pour debug 
        return
        self.tour_prison += 1

        if self.tour_prison == 3: # sortie de prison
            self.tour_prison = 0
            self.position = 10
            self.payer(50)

        else:    
            print(self.nom, ", vous êtes en prison. Tour:", self.tour_prison, "\n")
            txt = "Choisissez: 1) payer 50 € ou 2) faire un double "
            if self.libere > 0: txt += "3) utiliser votre carte 'libéré de prison'"
            choix = ""
            while choix not in ["1","2","3"]: choix = input(txt + "\n")

            if choix == "1": # libération du 3ème tour
                self.tour_prison = 0
                self.position = 10
                self.payer(50)

            elif choix == "2": # TODO: ttt du double sans rejouer, SUR PLATEAU ?
                pass

            elif choix == "3": # libération par carte
                self.tour_prison = 0
                self.position = 10
                if self.libere == 1: # carte chance
                    self.libere == 0
                    carte_chance.libere_prison_dispo = True
                elif self.libere == 2: # carte caisse de communauté
                    self.libere == 0
                    carte_communaute.libere_prison_dispo = True
                elif self.libere == 3: # possede les 2 cartes (et en rend celle de chance)
                    self.libere == 1
                    carte_chance.libere_prison_dispo = True
                                
    
    def payer(self, montant, beneficiaire = None): # beneficiaire = none => banque, sinon => joueur
        if self.cash >= montant:
            self.cash -= montant
            if beneficiaire is not None: beneficiaire.cash += montant
        else:
            pass


    def fiche(self):
        print("-------------------\n" +
            "index:", self.index_joueur, "\n" + 
            "Joueur:", self.nom, "\n" + 
            "Argent:", self.cash, "\n" +
            "Position:", self.position)
        if self.nb_double > 0: print("Double:", self.nb_double)
        print("-------------------\n")