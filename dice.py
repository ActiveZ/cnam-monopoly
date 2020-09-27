from random import randint


class Dice:


    # tirage du dé
    def lancer(self, joueur):
        d1 = randint(1,6)
        d2 = randint(1,6)
        # ajoute 1 à nb_double si tire 1 double et raz sinon
        joueur.nb_double = 0 if d1 != d2 else joueur.nb_double + 1

        print(joueur.nom, "lance les dés et fait",d1, "et", d2, "double:", joueur.nb_double)
        
        if joueur.nb_double == 3:
            print("En prison !")
            joueur.nb_double = 0
            return 40
        else:
            return d1 + d2

