from random import *
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

liste_atack_bot = []

def create_board_player():
        # creer une matrice grâce au input 
        # int --> matrice (list)
        # condition 
    size_board = 10
    num_boat = 6
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

def create_board_player(size_board):
        # creer une matrice grâce au input 
        # int --> matrice (list)
        # condition 
    num_boat = num_boat
    long_board_player = []
    board_player = []
    # Création d'un plateau de jeux qui correspond au information qui on été demander au joueur
    for size in range(size_board):
        long_board_player += [0]
    for size in range(size_board):
        board_player += [long_board_player]
    return board_player

def add_boat(matrice, num_boat, size_board):
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
                if direction == 'haut' or 'bas':
                    if matrice[y + direction][x] == 0:
                        matrice[y][x] = 1
                        matrice[y + direction][x] = 1

                else:
                    if matrice[y][x + direction] == 0:
                        matrice[y][x] = 1
                        matrice[y][x + direction] = 1
        # Affichage du plateau avec la position du bateau ( à faire )

# Placement des 3 bateau de 3
    for i in range(3):

        x = int(input("Rentré les coordonné x comprise entre 1 et 10 "))-1
        y = dico_coordonne[input("Rentré une coordonné y comprise entre A et J ")]
        direction = dico_direction[input("Dans quelle direction voulez vous que le bateau soit dirigé: Haut, Bas, Gauche ou droite (Merci de donné votre réponse en minuscule) ")]
        # Vérification que les donné rentré par le joueur rentre dans le plateau ( à faire )
        # Vérification que les donné du joueur ne font pas chevauché 2 bateaux ( à faire )
        # Affichage du plateau avec la position du bateau ( à faire )

# Placement du bateau de 5
    for i in range(1):

        x = int(input("Rentré les coordonné x comprise entre 1 et 10 "))-1
        y = dico_coordonne[input("Rentré une coordonné y comprise entre A et J ")]
        direction = dico_direction[input("Dans quelle direction voulez vous que le bateau soit dirigé: Haut, Bas, Gauche ou droite (Merci de donné votre réponse en minuscule) ")]
        # Vérification que les donné rentré par le joueur rentre dans le plateau ( à faire )
        # Vérification que les donné du joueur ne font pas chevauché 2 bateaux ( à faire )
        # Affichage du plateau avec la position du bateau ( à faire )
    
def create_board_bot(size_board, num_boat):
    # creer une matrice grâce au input 
    # int --> matrice (list)
    # condition 
    long_board_player = []
    board_bot = []
    # création du plateau du bot en accord avec les paramètres que le joueur à choisi au début
    for size in range(int(sqrt(size_board))):
        long_board_player += [0]
    for size in range(int(sqrt(size_board))):
        board_player += [long_board_player]
    add_boat_bot(board_bot, num_boat)
    return board_player

def add_boat_bot(matrice, num_boat):
    pass

def win(board):
    # verifier si il reste des bateaux(1) dans une matrice
    # matrice(list) --> bool
    # condition: \
    if 1 in board:
        return False
    else:
        return True
    

def fire_player(dico_coordonne, board_bot ):
    x = int(input("Rentré les coordonné x comprise entre 1 et 10 "))-1
    y = dico_coordonne[input("Rentré une coordonné y comprise entre A et J ")]
    if board_bot[x][y] == 1:
        board_bot[x][y] = 0
        print("Touché !!")
    else:
        print("Il n'y a pas de bateau ici. Désoler. ")

    print(board_bot)
    return board_bot

def fire_bot(liste_atack_bot, board_player):
    valid = False
    while valid == False:
        x = randint(0, 9)
        y = randint(0, 9)
        if (x, y) not in liste_atack_bot:
            if board_player[x][y] == 1:
                board_player[x][y] = 0
                print("Touché !!")
                liste_atack_bot.append((x, y))
                valid = True
            else:
                print("Vous n'avez subit aucun dégats !!")









            

        
       

        
    