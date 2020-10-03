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

    def go(self, dice): # avance de la valeur de dice
        self.position += dice # avance de la valeur de dice
        if self.position > 39: self.position -= 40 # case départ = 0


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