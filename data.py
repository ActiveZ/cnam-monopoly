carte_chance_data = {
    0:["Amende pour excès de vitesse", -15],
    1:["La banque vous verse un dividende de € 50",50],
    2:["Vous êtes imposé pour les réparations de voirie à raison de : € 40 par maison et € 115 par hotel","reparationA"],
    3:["Avancez jusqu'à la case Départ","depart"],
    4:["Payez les frais de scolarité : € 150",-150],
    5:["Rendez-vous Rue de la Paix","paix"],
    6:["Rendez-vous à l'Avenue Henri-Martin. Si vous passez par Départ recevez € 200","henriMartin"],
    7:["Faites des réparations dans toutes vos maisons : € 25 et € 100 par hôtel","reparationB"],
    8:["Avancez au Bd de la Villette. Si vous passez par Départ recevez € 200","vilette"],
    9:["Allez à la gare de Lyon. Si vous passez par Départ recevez € 200","lyon"],
    10:["Votre immeuble et votre prêt rapportent. Vous devez toucher € 150",150],
    11:["Allez en prison. Ne franchissez pas la case Départ. Ne touchez pas € 200","prison"],
    12:["Reculez de 3 cases","recul"],
    13:["Amende pour ivresse : € 20",-20],
    14:["Vous avez gagné le prix de mots croisés. Recevez € 100",100],
    15:["Vous êtes libéré de prison .Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.","libere"]
}



carte_caisse_communaute_data = {

    0:["C'est votre jour anniversaire chaque joueur doit vous donner € 10","anniversaire"],
    1:["Payer l'hôpital € 100",-100],
    2:["Vous avez gagné le 2nd prix de beauté. Recevez € 10",10],
    3:["Erreur de la banque en votre faveur recevez € 200",200],
    4:["Recevez votre intérêt sur l'emprunt à 7% , € 25",25],
    5:["Payez un amende de € 10 ou bien tirez un carte 'CHANCE'","amendeChance"],
    6:["Retournez a Belleville","belleville"],
    7:["Recevez votre revenu annuel € 100",100],
    8:["Allez en prison .Avancez tout droit en prison .Ne passez pas par la case départ . Ne recevez pas € 200","prison"],
    9:["Placez-vous sur la case Départ","depart"],
    10:["Payez la note du médecin € 50",-50],
    11:["Payez votre police d'assurance s'élevant à € 50",-50],
    12:["Les contributions vous remboursent la somme de € 20",20],
    13:["Vous héritez de € 100",100],
    14:["La vente de votre stock vous rapporte € 50",50],
    15:["Vous êtes libéré de prison .Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.","libere"]
}

# coordonnées pour les pions
cases_data = {
    0:{"nom":"Case Départ", "x":650, "y":650},
    1:{"nom":"Belleville", "x":575, "y":650},
    2:{"nom":"Caisse de Communauté", "x":518, "y":650},
    3:{"nom":"Lecourbe", "x":460, "y":650},
    4:{"nom":"Impôts", "x":405, "y":650},
    5:{"nom":"Gare Montparnasse", "x":350, "y":650},
    6:{"nom":"Vaugirard", "x":292, "y":650},
    7:{"nom":"Carte Chance", "x":236, "y":650},
    8:{"nom":"Courcelles", "x":180, "y":650},
    9:{"nom":"Républiques", "x":125, "y":650},
    10:{"nom":"Simple Visite", "x":35, "y":662},
    11:{"nom":"La Villette", "x":35, "y":575},
    12:{"nom":"Cie électricité", "x":35, "y":515},
    13:{"nom":"Neuilly", "x":35, "y":458},
    14:{"nom":"Paradis", "x":35, "y":407},
    15:{"nom":"Gare de Lyon", "x":35, "y":347},
    16:{"nom":"Mozart", "x":35, "y":290},
    17:{"nom":"Caisse de Communauté", "x":35, "y":236},
    18:{"nom":"Saint-Michel", "x":35, "y":182},
    19:{"nom":"Pigalle", "x":35, "y":122},
    20:{"nom":"Parc Gratuit", "x":50, "y":35},
    21:{"nom":"Matignon", "x":122, "y":35},
    22:{"nom":"Carte Chance", "x":179, "y":35},
    23:{"nom":"Malesherbes", "x":236, "y":35},
    24:{"nom":"Henri-Martin", "x":292, "y":35},
    25:{"nom":"Gare du Nord", "x":350, "y":35},
    26:{"nom":"Saint-Honoré", "x":404, "y":35},
    27:{"nom":"La Bourse", "x":461, "y":35},
    28:{"nom":"Cie des Eaux", "x":518, "y":35},
    29:{"nom":"La Fayette", "x":575, "y":35},
    30:{"nom":"Allez en Prison", "x":655, "y":35},
    31:{"nom":"Breteuil", "x":122, "y":655},
    32:{"nom":"Foch", "x":180, "y":655},
    33:{"nom":"Caisse de Communauté", "x":235, "y":655},
    34:{"nom":"Capucines", "x":290, "y":655},
    35:{"nom":"Gare Saint-Lazare", "x":345, "y":655},
    36:{"nom":"Carte Chance", "x":404, "y":655},
    37:{"nom":"Champs-élysées", "x":460, "y":655},
    38:{"nom":"Taxe de Luxe", "x":518, "y":655},
    39:{"nom":"La Paix", "x":575, "y":655},
    40:{"nom":"Prison", "x":65, "y":632},
    41:{"nom":"Les gares", "x":0, "y":0},              # 5 + 15 + 25 + 35 (41)
    42:{"nom":"Les Cies", "x":0, "y":0},               # 12 + 28 (42)
    43:{"nom":"Brun", "x":0, "y":0},                   # 1 + 3 (43)
    44:{"nom":"Bleu clair", "x":0, "y":0},             # 6 + 8 + 9 (44)
    45:{"nom":"Violet", "x":0, "y":0},                 # 11 + 13 + 14 (45)
    46:{"nom":"Orange", "x":0, "y":0},                 # 16 + 18 + 19 (46)
    47:{"nom":"Rouge", "x":0, "y":0},                  # 21 + 23 + 24 (47)
    48:{"nom":"Jaune", "x":0, "y":0},                  # 26 + 27 + 29 (48)
    49:{"nom":"Vert", "x":0, "y":0},                   # 31 + 32 + 34 (49)
    50:{"nom":"Bleu foncé", "x":0, "y":0}              # 37 + 39 (50)
}

compagnies_data = {
    12 : {
        "nom": "Compagnie de distribution d'électricité",
        "prix": 150,
        "hypotheque":75,
        "couleur": 42,
        "proprietaire": 0, # index du joueur
        "isHypotheque": False
    },
    
    28: {
        "nom": "Compagnie de distribution des eaux",
        "prix": 150,
        "hypotheque":75,
        "couleur": 42,
        "proprietaire": 0,
        "isHypotheque": False
    }
}


gares_data = {
    5: {
        "nom": "Gare Montparnasse",
        "prix": 200,
        "loyer": [25,50,100,200],
        "hypotheque":100,
        "couleur": 41,
        "proprietaire": 0,
        "isHypotheque": False
    }, 
        
    15: {
        "nom": "Gare de Lyon",
        "prix": 200,
        "loyer": [25,50,100,200],
        "hypotheque":100,
        "couleur": 41,
        "proprietaire": 0,
        "isHypotheque": False
    },

    25: {
        "nom": "Gare du Nord",
        "prix": 200,
        "loyer": [25,50,100,200],
        "hypotheque":100,
        "couleur": 41,
        "proprietaire": 0,
        "isHypotheque": False
    },
        
    35: {
        "nom": "Gare Saint-Lazare",
        "prix": 200,
        "loyer": [25,50,100,200],
        "hypotheque":100,
        "couleur": 41,
        "proprietaire": 0,
        "isHypotheque": False
    }
}


proprietes_data = {
    1: {
        "nom": "Boulevard de Belleville",
        "prix": 60,
        "loyer": [2,10,30,90,160,250],
        "hypotheque":30,
        "prix_maison":50,
        "couleur": 43,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },

    3: {
        "nom": "Rue Lecourbe",
        "prix": 60,
        "loyer": [4,20,60,180,320,450],
        "hypotheque":30,
        "prix_maison":50,
        "couleur": 43,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },

    6: {
        "nom": "Rue Vaugirard",
        "prix": 100,
        "loyer": [6,30,90,270,400,550],
        "hypotheque":50,
        "prix_maison":50,
        "couleur": 44,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },

    8: {
        "nom": "Rue de Courcelles",
        "prix": 100,
        "loyer": [6,30,90,270,400,550],
        "hypotheque":50,
        "prix_maison":50,
        "couleur": 44,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },        
    
    9: {
        "nom": "Avenue de la République",
        "prix": 120,
        "loyer": [8,40,100,300,450,600],
        "hypotheque":60,
        "prix_maison":50,
        "couleur": 44,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },
    
    11: {
        "nom": "Boulevard de la Villette",
        "prix": 140,
        "loyer": [10,50,150,450,625,750],
        "hypotheque":70,
        "prix_maison":100,
        "couleur": 45,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },

    13: {
        "nom": "Avenue de Neuilly",
        "prix": 140,
        "loyer": [10,50,150,450,625,750],
        "hypotheque":70,
        "prix_maison":100,
        "couleur": 45,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },
    
    14: {
        "nom": "Rue de Paradis",
        "prix": 160,
        "loyer": [12,60,180,500,700,900],
        "hypotheque":80,
        "prix_maison":100,
        "couleur": 45,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },

    16: {
        "nom": "Avenue Mozart",
        "prix": 180,
        "loyer": [14,70,200,550,750,950],
        "hypotheque":90,
        "prix_maison":100,
        "couleur": 46,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },    
    
    18: {
        "nom": "Boulevard St Michel",
        "prix": 180,
        "loyer": [14,70,200,550,750,950],
        "hypotheque":90,
        "prix_maison":100,
        "couleur": 46,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },    
    
    19: {
        "nom": "Place Pigalle",
        "prix": 200,
        "loyer": [16,80,220,600,800,1000],
        "hypotheque":100,
        "prix_maison":100,
        "couleur": 46,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },    

    21: {
        "nom": "Avenue Matignon",
        "prix": 220,
        "loyer": [18,90,250,700,875,1050],
        "hypotheque":110,
        "prix_maison":150,
        "couleur": 47,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },    
    
    23: {
        "nom": "Boulevard Malesherbes",
        "prix": 220,
        "loyer": [18,90,250,700,875,1050],
        "hypotheque":110,
        "prix_maison":150,
        "couleur": 47,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },    
    
    24: {
        "nom": "Avenue Henri Martin",
        "prix": 240,
        "loyer": [20,100,300,750,925,1100],
        "hypotheque":120,
        "prix_maison":150,
        "couleur": 47,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },       

    26: {
        "nom": "Faubourg St Honoré",
        "prix": 260,
        "loyer": [22,110,330,800,975,1150],
        "hypotheque":130,
        "prix_maison":150,
        "couleur": 48,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },

    27: {
        "nom": "Place de la Bourse",
        "prix": 260,
        "loyer": [22,110,330,800,975,1150],
        "hypotheque":130,
        "prix_maison":150,
        "couleur": 48,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },
          
    29: {
        "nom": "Rue de la Fayette",
        "prix": 280,
        "loyer": [24,120,360,850,1025,1200],
        "hypotheque":140,
        "prix_maison":150,
        "couleur": 48,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },    
    
    31: {
        "nom": "Avenue de Breteuil",
        "prix": 300,
        "loyer": [26,130,390,900,1100,1275],
        "hypotheque":150,
        "prix_maison":200,
        "couleur": 49,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },    
        
    32: {
        "nom": "Avenue Foch",
        "prix": 300,
        "loyer": [26,130,390,900,1100,1275],
        "hypotheque":150,
        "prix_maison":200,
        "couleur": 49,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },    
        
    34: {
        "nom": "Boulevard des Capucines",
        "prix": 320,
        "loyer": [28,150,450,1000,1200],
        "hypotheque":160,
        "prix_maison":200,
        "couleur": 49,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },      

    37: {
        "nom": "Avenue des Champs-Elisées",
        "prix": 350,
        "loyer": [35,175,500,1100,1300,1500],
        "hypotheque":175,
        "prix_maison":200,
        "couleur": 50,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    },    
        
    39: {
        "nom": "Rue de la Paix",
        "prix": 400,
        "loyer": [50,200,600,1400,1700,2000],
        "hypotheque":200,
        "prix_maison":200,
        "couleur": 50,
        "proprietaire": 0,
        "nb_maison": 0,
        "nb_hotel": 0,
        "isHypotheque": False
    }
}    



# Une compagnie: 4 fois le montant des dés
# Deux compangnies: 10 fois le montant des dés 


# Nom des différentes cases 
# @case = ("Case Départ",            # 0
#          "Belleville",             # 1
#          "Caisse de Communauté",   # 2
#          "Lecourbe",               # 3
#          \"Impôts",                 # 4
#          "Gare Montparnasse",      # 5
#          "Vaugirard",              # 6
#          "Carte Chance",           # 7
#          "Courcelles",             # 8
#          "Républiques",            # 9
#          "Simple Visite",          # 10
#          "La Villette",            # 11
#          "Cie électricité",        # 12
#          "Neuilly",                # 13
#          "Paradis",                # 14
#          "Gare de Lyon",           # 15
#          "Mozart",                 # 16
#          "Caisse de Communauté",   # 17 
#          "Saint-Michel",           # 18
#          "Pigalle",                # 19
#          "Parc Gratuit",           # 20
#          "Matignon",               # 21
#          "Carte Chance",           # 22
#          "Malesherbes",            # 23
#          "Henri-Martin",           # 24
#          "Gare du Nord",           # 25
#          "Saint-Honoré",           # 26
#          "La Bourse",              # 27
#          "Cie des Eaux",           # 28
#          "La Fayette",             # 29
#          \"Allez en Prison",        # 30
#          "Breteuil",               # 31
#          "Foch",                   # 32
#          "Caisse de Communauté",   # 33
#          "Capucines",              # 34
#          "Gare Saint-Lazare",      # 35
#          "Carte Chance",           # 36
#          "Champs-élysées",         # 37
#          "Taxe de Luxe",           # 38
#          "La Paix",                # 39
#          "Prison",                 # 40
#          "Les gares",              # 5 + 15 + 25 + 35 (41)
#          "Les Cies",               # 12 + 28 (42)
#          "Brun",                   # 1 + 3 (43)
#          "Bleu clair",             # 6 + 8 + 9 (44)
#          "Violet",                 # 11 + 13 + 14 (45)
#          \"Orange",                 # 16 + 18 + 19 (46)
#          "Rouge",                  # 21 + 23 + 24 (47)
#          "Jaune",                  # 26 + 27 + 29 (48)
#          "Vert",                   # 31 + 32 + 34 (49)
#          "Bleu foncé"              # 37 + 39 (50)
#          );


#          Cartes Chances
# Amende pour excès de vitesse : F 1.500
# La banque vous verse un dividende de F 5.000
# Vous êtes imposé pour les réparations de voirie a raison de : F 4.000 par maison et F 11.500 par hotel
# Avancez jusqu'à la case "Départ"
# Payez les frais de scolarité : F 15.000
# Rendez-vous Rue de la Paix (nu = F 5.000 Hôtel = F 200.000)
# Rendez-vous à l'Avenue Henri-Martin (nu = F 2.000 Hôtel = F 110.000). Si vous passez par "Départ" recevez F 20.000
# Faites des réparations dans toutes vos maisons : F 2.500 et F 10.000 par hôtel
# Avancez au Bd de la Villette (nu = F 1.000 Hôtel = F 75.000). Si vous passez par "Départ" recevez F 20.000
# Allez à la gare de Lyon (1 gare = F 2.500;4 gares = F 20.000). Si vous passez par "Départ" recevez F 20.000
# Votre immeuble et votre prêt rapportent. Vous devez toucher F 15.000
# Allez en prison. Ne franchissez pas la case "Départ". Ne touchez pas F 20.000
# Reculez de 3 cases
# Amende pour ivresse : F 2.000
# Vous avez gagné le prix de mots croisés. Recevez F 10.000
# Vous êtes libéré de prison .Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.
 
# Cartes Caisses de Communauté
 
# C'est votre jour anniversaire chaque joueur doit vous donner F 1.000
# Payer l'hôpital F 10.000
# Vous avez gagné le 2nd prix de beauté. Recevez F 1.000
# Erreur de la banque en votre faveur recevez F 20.000
# Recevez votre intérêt sur l'emprunt à 7% , F 2.500
# Payez un amende de F 1.000 ou bien tirez un carte "CHANCE"
# Retournez a Belleville(nu = F 200 Hôtel = F 25.000)
# Recevez votre revenu annuel F 10.000
# Allez en prison .Avancez tout droit en prison .Ne passez pas par la case départ . Ne recevez pas F 20.000
# Placez-vous sur la case " Départ"
# Payez la note du médecin F 5.000
# Payez votre police d'assurance s'élevant à F 5.000
# Les contributions vous remboursent la somme de F 2.000
# Vous héritez de F 10.000
# La vente de votre stock vous rapporte F 5.000
# Vous êtes libéré de prison .Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.
# Boulevard de Belleville
# Terrain nu : 2€
# 1 maisons : 10€
# 2 maisons : 30€
# 3 maisons : 90€
# 4 maisons : 160€
# hotel : 250€

# Rue Lecourbe
# Terrain nu : 4€
# 1 maisons : 20€
# 2 maisons : 60€
# 3 maisons : 180€
# 4 maisons : 320€
# hotel : 450€

# Rue Vaugirard
# Terrain nu : 6€
# 1 maisons : 30€
# 2 maisons : 90€
# 3 maisons : 270€
# 4 maisons : 400€
# hotel : 550€

# Avenue de la République
# Terrain nu : 8€
# 1 maisons : 40€
# 2 maisons : 100€
# 3 maisons : 300€
# 4 maisons : 450€
# hotel : 600€

# Rue de Courcelles
# Terrain nu : 6€
# 1 maisons : 30€
# 2 maisons : 90€
# 3 maisons : 270€
# 4 maisons : 400€
# hotel : 550€

# Avenue de Neuilly
# Terrain nu : 10€
# 1 maisons : 50€
# 2 maisons : 150€
# 3 maisons : 450€
# 4 maisons : 625€
# hotel : 750€

# Rue de Paradis
# Terrain nu : 12€
# 1 maisons : 60€
# 2 maisons : 180€
# 3 maisons : 500€
# 4 maisons : 700€
# hotel : 900€

# Boulevard de la Villette
# Terrain nu : 10€
# 1 maisons : 50€
# 2 maisons : 150€
# 3 maisons : 450€
# 4 maisons : 625€
# hotel : 750€

# Avenue Mozart
# Terrain nu : 14€
# 1 maisons : 70€
# 2 maisons : 200€
# 3 maisons : 550€
# 4 maisons : 760€
# hotel : 950€

# Place Pigalle
# Terrain nu : 16€
# 1 maisons : 80€
# 2 maisons : 220€
# 3 maisons : 600€
# 4 maisons : 800€
# hotel : 1000€

# Boulevard St Michel
# Terrain nu : 14€
# 1 maisons : 70€
# 2 maisons : 200€
# 3 maisons : 550€
# 4 maisons : 750€
# hotel : 950€

# Boulevard Malesherbes
# Terrain nu : 18€
# 1 maisons : 90€
# 2 maisons : 2500€
# 3 maisons : 700€
# 4 maisons : 875€
# hotel : 1050€

# Avenue Henri Martin
# Terrain nu : 20€
# 1 maisons : 100€
# 2 maisons : 300€
# 3 maisons : 750€
# 4 maisons : 925€
# hotel : 1100€

# Avenue Matignon
# Terrain nu : 18€
# 1 maisons : 90€
# 2 maisons : 250€
# 3 maisons : 700€
# 4 maisons : 875€
# hotel : 1050€

# Place de la Bourse
# Terrain nu : 22€
# 1 maisons : 110€
# 2 maisons : 330€
# 3 maisons : 800€
# 4 maisons : 975€
# hotel : 1150€

# Faubourg St Honoré
# Terrain nu : 22€
# 1 maisons : 110€
# 2 maisons : 330€
# 3 maisons : 800€
# 4 maisons : 975€
# hotel : 1150€

# Rue de la Fayette
# Terrain nu : 24€
# 1 maisons : 120€
# 2 maisons : 360€
# 3 maisons : 850€
# 4 maisons : 1025€
# hotel : 1200€

# Avenue Foch
# Terrain nu : 26€
# 1 maisons : 130€
# 2 maisons : 390€
# 3 maisons : 900€
# 4 maisons : 1100€
# hotel : 250€ 

# Avenue de Breteuil
# Terrain nu : 26€
# 1 maisons : 130€
# 2 maisons : 390€
# 3 maisons : 900€
# 4 maisons : 1100€
# hotel : 1275€

# Boulevard des Capucines
# Terrain nu : 28€
# 1 maisons : 150€
# 2 maisons : 450€
# 3 maisons : 1000€
# 4 maisons : 1200€
# hotel : 1400€

# Avenue des Champs-Elisées
# Terrain nu : 35€
# 1 maisons : 175€
# 2 maisons : 500€
# 3 maisons : 1100€
# 4 maisons : 1300€
# hotel : 1500€

# Rue de la Paix
# Terrain nu : 50€
# 1 maisons : 200€
# 2 maisons : 600€
# 3 maisons : 1400€
# 4 maisons : 1700€
# hotel : 2000€

# Gares
# 1 gare : 25€
# 2 gare : 50€
# 3 gare : 100€
# 4 gare : 200€

# Compagnies distribution des eaux et d'électricité
# Une compagnie: 4 fois le montant des dés
# Deux compangnies: 10 fois le montant des dés 