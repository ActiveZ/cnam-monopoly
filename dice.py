from random import randint
# from joueur import Joueur


class Dice:


    # tirage du dé
    def lancer(self, joueur):
        d1 = randint(1,6)
        d2 = randint(1,6)
        # ajoute 1 à nb_double si tire 1 double et raz sinon
        joueur.nb_double = 0 if d1 != d2 else joueur.nb_double + 1

        print(joueur.nom_joueur, "lance les dés et fait",d1, "et", d2, "double:", joueur.nb_double)
        
        if joueur.nb_double == 3:
            print("En prison !")
            joueur.position = 40
            joueur.nb_double = 0
        else:
            joueur.position += d1 + d2
            if joueur.position > 39:
                joueur.position -= 40 # case départ = 0
