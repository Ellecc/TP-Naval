#from Naval_function import *
from math import *

dico_coordonne = {
        0:"A",
        1:"B",
        2:"C",
        3:"D",
        4:"E",
        5:"F",
        6:"G",
        7:"H",
        8:"I",
        9:"J",
        "A":0,
        "B":1,
        "C":2,
        "D":3,
        "E":4,
        "F":5,
        "G":6,
        "H":7,
        "I":8,
        "J":9,
    }


def add_boat(matrice):
# Direction traduit par un nombre pour une meilleur compréhension
    dico_direction = {
        "haut" : 1,
        "droite" : 1,
        "bas" : -1,
        "gauche" : -1,
    }
    # Consigne de placage pour les bateaux 
    print("Vous allez placé les bateau sur le plateau de jeux de la manière suivante:\n"
            "1. vous donneré les coordonné X et Y du premier point du bateau\n"
            "2. vous donneré la direction vers laquelle s'étant le bateau\n"
            "3. vous allez placer 2 bateaux de 2 case, 3 bateaux de 3 case et 1 bateaux de 5 case dans l'ordre"
            "Pour rappel, deux bateau ne peuvent pas se chevauché et un bateau ne peux pas s'étendre hors du plateau\n"
            "Si malgré cela une erreur se produit, Merci de bien vouloir relancer le jeux\n"
            "Bon Jeux à vous")
# Placement des 2 bateaux de 2
    for i in range(2):

        x = int(input("Rentré les coordonné x comprise entre 1 et 10 "))-1
        y = dico_coordonne[input("Rentré une coordonné y comprise entre A et J ")]
        direction = input("Dans quelle direction voulez vous que le bateau soit dirigé: Haut, Bas, Gauche ou droite (Merci de donné votre réponse en minuscule) ")
        
        # Vérification que les donné rentré par le joueur rentre dans le plateau ( à faire )
        if 9 >= x >= 0 and 9 >= y >= 0 and direction in dico_direction:
        # Vérification que les donné du joueur ne font pas chevauché 2 bateaux ( à faire )
            if matrice[y][x] == 0:
                if direction in ['haut', 'bas']:
                    if matrice[y + dico_direction[direction]][x] == 0:
                        matrice[y][x] = 1
                        matrice[y + dico_direction[direction]][x] = 1
                    else:
                        print("ERROR, un bateau se trouve déja ici")
            
                else:
                    if matrice[y][x + dico_direction[direction]] == 0:
                        matrice[y][x] = 1
                        matrice[y][x + dico_direction[direction]] = 1
            
            print('\n'.join([' '.join(map(str, ligne)) for ligne in matrice]))
        # Affichage du plateau avec la position du bateau ( à faire )


def create_board_player(size_board):
        # creer une matrice grâce au input 
        # int --> matrice (list)
        # condition 
    long_board_player = []
    board_player = []
    # Création d'un plateau de jeux qui correspond au information qui on été demander au joueur
    for size in range(size_board):
        long_board_player += [0]
    for size in range(size_board):
        board_player += [long_board_player]
    return board_player


add_boat(create_board_player(10))


#print('\n'.join([' '.join(map(str, ligne)) for ligne in board_player]))
# commande pour afficher le plateau de manière propre