from random import *
from math import *


def pick_up_info():
        # récupère les paramètres du jeu au près du joueur
        # / --> list
        # condition : type_input = int  and size_board > num_boat
    size_board = int(input("Quelle taille de plateau souhaitez-vous ? 16, 25 ou 36 cases ?"))
    num_boat = int(input("Combien de case voulez vous remplir"
                         "avec des bateaux ? (Moins que le nombre de cases)"))
    # Vérification de size_board et num_boat pour être sur qu'il réponde au attente
    if size_board > num_boat and size_board == int and num_boat == int: 
        return [size_board, num_boat]
    else:
        print("error_type : input",
              "Veuillez mettre une réponse valide, votre réponse doit être un nombre"
              "et votre nombre de bateaux ne doit pas etre plus grand que votre nombre de case"
              )
        pick_up_info()

        

def create_board_player(size_board , num_boat):
        # creer une matrice grâce au input 
        # int --> matrice (list)
        # condition 
    num_boat = num_boat
    dico_coordone = {
        0:"A",
        1:"B",
        2:"C",
        3:"D",
        4:"E",
        5:"F",
        "A":0,
        "B":1,
        "C":2,
        "D":3,
        "E":4,
        "F":5,
    }
    long_board_player = []
    board_player = []
    # Création d'un plateau de jeux qui correspond au information qui on été demander au joueur
    for size in range(int(sqrt(size_board))):
        long_board_player += [0]
    for size in range(int(sqrt(size_board))):
        board_player += [long_board_player]
    add_boat(board_player, dico_coordone, num_boat, size_board)
    return board_player

def add_boat(matrice, coordone_dico, num_boat, size_board):
    while num_boat > 0:
    # Demande fait au joueur pour connaitre la taille et la position des bateaux
        size_boat = int(input("quelle taille de bateau"
                              "voulez vous choisisr entre 1 case, 2 cases et 3 case"))
        if 0 < size_boat < 4 and (num_boat - size_boat) >= 0:
            num_boat -= size_boat
            for i in range(size_boat):
                x = int(input("Rentré les coordonné x comprise entre 0 et {} ".format(int(sqrt(size_board))-1)))
                y = input("Rentré une coordonné y comprise entre A et {} ".format(dico_coordone[sqrt(int(size_board))-1]))
                # Vérification que les donné rentré par le joueur soit valide
                if x == int and 0 <= x < int(sqrt(size_board)) and y in dico_coordonne:
                    
        else:
            print("error_type: input"
                "Le nombre de case choisis n'est pas valide.")  
          

            

        
        
    
    

    
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
    
