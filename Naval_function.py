from TP_Bataille_Naval import *
from random import *
def pick_up_info():
        # récupère les paramètres du jeu au près du joueur
        # / --> list
        # condition : type_input = int  and size_board > num_boat
    size_board = int(input("Quelle taille de plateau souhaitez-vous ? 9, 16 ou 25 cases ?"))
    num_boat = int(input("Avec combien de bateaux souhaitez-vous jouer ? (Moins que le nombre de cases)"))
    if size_board > num_boat and size_board == int and num_boat == int:
        return [size_board, num_boat]
    else:
        return False

def create_board_player(size_board , num_boat):
        # creer une matrice grâce au input 
        # int --> matrice (list)
        # condition 
    

    pass 

def create_board_bot():
    pass

def win(board):
    liste = 