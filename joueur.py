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
        if self.position == 40: # joueur en prison, ttt a part
            self.prison()
            return

        self.position += dice # avance de la valeur de dice
        if self.position > 39: self.position -= 40 # case départ = 0


    def prison(self):
        # self.position = 10
        self.tour_prison += 1
        if self.tour_prison == 3:
            self.tour_prison = 0
            
        else:    
            print(self.nom, ", vous êtes en prison. Tour:", self.tour_prison, "\n")
            txt = "Choisissez: 1) payer 50 € ou 2) faire un double "
            if self.libere: txt += "3) utiliser vortre carte 'libéré de prison'\n"

        # pass


    def payer(self, montant, beneficiaire = None): # beneficiaire = none => banque, sinon => joueur
        if self.cash >= montant:
            self.cash -= montant
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