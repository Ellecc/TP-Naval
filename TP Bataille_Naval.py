from Naval_function import *
from math import *
from random import *

screen = True
while screen:
    game_stat = True
    while game_stat:
        board_player = add_boat_bot(create_board_bot(10), boat_liste)
        board_bot = add_boat_bot(create_board_bot(10), boat_liste)
        fire_player(board_bot[1])
        

        