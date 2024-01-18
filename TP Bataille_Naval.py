from Naval_function import *
from math import *
from random import *

screen = True
while screen:
    game_stat = True
    while game_stat:
        board_player = create_board_player(10)
        bot = add_boat_bot(create_board_bot(10), boat_liste)
        dico_boat_bot = bot[0]
        board_bot = bot[1]
        win = True
        while win:
            print ("Bien, allons-y.")
            print ("Vous commancez.")
            