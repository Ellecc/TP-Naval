from Naval_function import *
from math import *
from random import *

screen = True
while screen:
    nb_partie_gagner = 0
    game = True
    while game:
        info_bot = add_boat_bot(create_board_bot(10), boat_liste)
        board_bot = info_bot[1]
        boat_dico_bot = info_bot[0] 
        info_player = add_boat_bot(create_board_player(10),boat_liste)
        board_player = info_player[1]
        boat_dico_player = info_player[0]
        win = True
        while win:
            fire_player(board_bot, boat_dico_bot)
            fire_bot(board_player, boat_dico_player)
            if win(board_bot) == True:
                print("Vous avez gagner !!!")
                nb_partie_gagner += 1
                win = False
            elif win(board_player) == True:
                print("Vous avez perdu !!")
                win = False

        stat = input("voulez-vous rejouer oui/non ?")
        if stat == "non":
            game = False
            print(nb_partie_gagner)
            screen = False
        elif stat == "oui":
            print(nb_partie_gagner)
        else:
            print("votre réponse n'est pas valide.\n"
                  "Le jeux s'arrète automatiquement")
            screen = False
        




         
      
        
            