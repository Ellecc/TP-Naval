from Naval_function import *
from math import *
from random import *

screen = True
while screen:
    game_stat = True
    while game_stat:
        board_player = create_board_player()
        board_bot = create_board_bot()
        