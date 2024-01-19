from Naval_function import *
from math import *
from random import *

screen = True
while screen:
    board_bot = [0]
    board_player = [0]
    while win(board_player) or win(board_bot):
        player = add_boat_player(create_board_player(10), boat_liste)
        bot = add_boat_bot(create_board_bot(10), boat_liste)
        dico_boat_player = player[0]
        board_player = player[1]
        dico_boat_bot = bot[0]
        board_bot = bot[1]

        
            