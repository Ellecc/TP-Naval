from Naval_function import *
from math import *
from random import *

screen = True
while screen:
    game_stat = True
    info = pick_up_info()
    size_board = info[0]
    num_boat = info[1]
    while game_stat:
        board_player = create_board_player(size_board , num_boat)

