from random import randint


class Prison:


        def libere(self,j,carte_chance,carte_communaute):       
            j.tour_prison += 1

            if j.tour_prison == 3: # sortie de prison au 3ème tour
                print(j.nom,": 3ème tour, vous êtes libéré de prison")
                self._lance_de(j)
                j.payer(50)


            else:    
                print(j.nom, ", vous êtes en prison. Tour:", j.tour_prison, "\n")
                txt = "Choisissez: 1: payer 50 € ou 2: faire un double "
                if j.libere > 0: txt += "3: utiliser votre carte 'libéré de prison'"
                choix = ""
                liste = ["1","2"]
                if j.libere > 0: liste.append("3")
                while choix not in liste: choix = input(txt + "\n")

                if choix == "1": # libération par paiement
                    print("Vous avez payé 50 €, vous êtes libéré de prison") # todo rejouer ?
                    self._lance_de(j)
                    j.payer(50)

                elif choix == "2": # tentative de libération par double
                    d1 = randint(1,6)
                    d2 = randint(1,6)
                    if d1 == d2:
                        print("Vous avez fait un double", d1, ". Vous êtes libéré de prison")
                        j.position = 10 + d1 + d2
                    else:
                        print(j.nom,"lance les dés et fait", d1, "et", d2)


                elif choix == "3": # libération par carte
                    print("Vous avez utilisé votre carte, vous êtes libéré de prison")
                    self._lance_de(j)
                    if j.libere == 1: # carte chance
                        j.libere = 0
                        carte_chance.libere_prison_dispo = True
                    elif j.libere == 2: # carte caisse de communauté
                        j.libere = 0
                        carte_communaute.libere_prison_dispo = True
                    elif j.libere == 3: # possede les 2 cartes (et rend celle de chance)
                        j.libere = 2
                        carte_chance.libere_prison_dispo = True
                    

        def _lance_de(self, j):
            j.tour_prison = 0
            d1 = randint(1,6)
            d2 = randint(1,6)
            j.position = 10 + d1 + d2
            print(j.nom,"lance les dés et fait", d1, "et", d2)
