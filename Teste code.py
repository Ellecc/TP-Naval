#from Naval_function import *
from math import *

#print(create_board_player(36, 0))
dico_coordone = {
        0:"A",
        1:"B",
        2:"C",
        3:"D",
        4:"E",
        5:"F",
    }
size_board = 36
x = int(input("Rentré les coordonné x comprise entre 0 et {} ".format(int(sqrt(size_board))-1)))
y = input("Rentré une coordonné y comprise entre A et {}".format(dico_coordone[sqrt(int(size_board))-1]))
print(y)