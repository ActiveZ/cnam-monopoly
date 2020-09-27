from random import randint


class Dice:


    # tirage du dé
    def lancer(self, joueur):
        d1 = randint(1,6)
        d2 = randint(1,6)
        txt = joueur.nom + " lance les dés et fait " + str(d1) + " et " + str(d2)

        # ajoute 1 à nb_double si tire 1 double et raz sinon
        joueur.nb_double = 0 if d1 != d2 else joueur.nb_double + 1

        if d1 == d2: txt += " double: " + str(joueur.nb_double)
        print(txt,"\n")
        
        if joueur.nb_double == 3:
            print("En prison !\n")
            joueur.nb_double = 0
            return 40
        else:
            return d1 + d2

