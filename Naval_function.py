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

liste_attack_bot = []

boat_liste = (2, 2, 3, 3, 3, 5)

def add_boat_player(board, boat):
    dico_boat_player = {}
    num_boat = 0
    # Direction traduit par un nombre pour une meilleur compréhension
    dico_direction = {
        "haut": -1,
        "droite": 1,
        "bas": 1,
        "gauche": -1,
    }
    # Consigne de placage pour les bateaux 
    print("Vous allez placé les bateau sur le plateau de jeux de la manière suivante:\n"
            "1. vous donneré les coordonné X et Y du premier point du bateau\n"
            "2. vous donneré la direction vers laquelle s'étant le bateau\n"
            "3. vous allez placer 2 bateaux de 2 case, 3 bateaux de 3 case et 1 bateaux de 5 case dans l'ordre\n"
            
            "Pour rappel, deux bateau ne peuvent pas se chevauché et un bateau ne peux pas s'étendre hors du plateau\n"
            "Bon Jeux à vous\n")
    # Placement des 2 bateaux de 2
    for height in boat:
        verif = 0
        while verif != height:
            x = int(input("Rentrez les coordonné x comprise entre 1 et 10 "))-1
            y = dico_coordonne[input("Rentrez une coordonné y comprise entre A et J ")]
            direction = input("Dans quelle direction voulez vous que le bateau soit dirigé: Haut, Bas, Gauche ou droite (Merci de donné votre réponse en minuscule) ")

            # Vérification que les donné rentré par le joueur rentre dans le plateau
            if 9 >= x >= 0 and 9 >= y >= 0 and direction in dico_direction:
                # Vérification que les donné du joueur ne font pas chevauché 2 bateaux sur la case de départ
                if board[y][x] == 0:
                    # Variation en fonction de si le bateaux c'étant verticalement
                    if direction in ['haut', 'bas']:
                        # Vérification que les donné du joueur ne font pas chevauché 2 bateaux sur la case vers laquelle s'étant le bateaux
                        if all(9 >= y + t >= 0 for t in range(height)):
                            if all(board[y + dico_direction[direction] * t][x] == 0 for t in range(height)):
                                one_boat = []
                                for i in range(height):
                                    board[y + dico_direction[direction] * i][x] = 1
                                    verif += 1
                                    one_boat += [[x,y + dico_direction[direction] * i]]
                                num_boat += 1
                                dico_boat_player['co_boat_' + str(num_boat)] = one_boat

                            
                            else:
                                print("ERROR, un bateau se trouve déja ici !!!")
                        else:
                            print("ERROR, Le bateaux dépasse du plateau")

                    else:
                        # Variation en fonction de si le bateaux c'étant horizontalement
                        if all(9 >= x + t >= 0 for t in range(height)):
                            if all(board[y][x + dico_direction[direction] * t] == 0 for t in range(height)):
                                one_boat = []
                                for i in range(height):
                                    board[y][x + dico_direction[direction] * i] = 1
                                    verif += 1
                                    one_boat += [[x + dico_direction[direction] * i,y]]
                                num_boat += 1
                                dico_boat_player['co_boat_' + str(num_boat)] = one_boat

                            else:
                                print("ERROR, un bateau se trouve déja ici")              
                        else:
                            print("ERROR, Le bateaux dépasse du plateau")
                else:
                    print("ERROR, un bateau se trouve déja ici")
            else:
                print("ERROR, les donné ne sont pas conforme a ce qui est demandé !!!")

        # Affichage de la grille avec des lettres pour les lignes et des chiffres pour les colonnes
        letters = 'ABCDEFGHIJ'
        # Affichage des chiffres de 1 à 10 pour les colonnes avec des séparateurs
        print('   ', end="")
        for i, number in enumerate(range(1, 10 + 1), 0):
            print('\033[94m' + " " + str(number) + " " + '\033[0m', end="")
            if i < 10 - 1:
                print('|', end="")
        print()
        print('-' * (4 * 10 + 2))  # Ligne de séparation

        # La boucle prend chaque élément de board_player (ligne) et lui donne un chiffre pour chaque ligne (i)
        for i, ligne in enumerate(board):
            # Affichage des lettres de A à J pour les lignes avec des séparateurs
            print('\033[94m' + letters[i] + '\033[0m | ' + ' | '.join(map(str, ligne)))
            print('-' * (4 * 10 + 2))  # Ligne de séparation
        print()
            
    return [dico_boat_player, board]

def add_boat_bot(board_bot, boat_liste):
    dico_boat_bot = {}
    num_boat = 0
    liste_direction = ["haut","bas","droite","gauche"]
    # Direction traduit par un nombre pour une meilleur compréhension
    dico_direction = {
        "haut": -1,
        "droite": 1,
        "bas": 1,
        "gauche": -1,
    }
    # Placement des 2 bateaux de 2
    for height in boat_liste:
        verif = 0
        while verif != height:
            x = int(randint(1, 9))
            y = int(randint(1, 9))
            direction = choice(liste_direction)

            # Vérification que les donné rentré par le joueur rentre dans le plateau
            if 9 >= x >= 0 and 9 >= y >= 0 and direction in dico_direction:
                # Vérification que les donné du joueur ne font pas chevauché 2 bateaux sur la case de départ
                if board_bot[y][x] == 0:
                    # Variation en fonction de si le bateaux c'étant verticalement
                    if direction in ['haut', 'bas']:
                        # Vérification que les donné du joueur ne font pas chevauché 2 bateaux sur la case vers laquelle s'étant le bateaux
                        if all(9 >= y + t * dico_direction[direction] >= 0 for t in range(height)):
                            if all(board_bot[y + dico_direction[direction] * t][x] == 0 for t in range(height)):
                                one_boat = []
                                for i in range(height):
                                    board_bot[y + dico_direction[direction] * i][x] = 1
                                    verif += 1
                                    one_boat += [[x,y + dico_direction[direction] * i]]
                                num_boat += 1
                                dico_boat_bot['co_boat_' + str(num_boat)] = one_boat

                    else:
                        # Variation en fonction de si le bateaux c'étant horizontalement
                        if all(9 >= x + t * dico_direction[direction] >= 0 for t in range(height)):
                            if all(board_bot[y][x + dico_direction[direction] * t] == 0 for t in range(height)):
                                one_boat = []
                                for i in range(height):
                                    board_bot[y][x + dico_direction[direction] * i] = 1
                                    verif += 1
                                    one_boat += [[x + dico_direction[direction] * i,y]]
                                num_boat += 1
                                dico_boat_bot['co_boat_' + str(num_boat)] = one_boat

    # Affichage de la grille avec des lettres pour les lignes et des chiffres pour les colonnes
    letters = 'ABCDEFGHIJ'
    # Affichage des chiffres de 1 à 10 pour les colonnes avec des séparateurs
    print('   ', end="")
    for i, number in enumerate(range(1, 10 + 1), 0):
        print('\033[94m' + " " + str(number) + " " + '\033[0m', end="")
        if i < 10 - 1:
            print('|', end="")
    print()
    print('-' * (4 * 10 + 2))  # Ligne de séparation

    # La boucle prend chaque élément de board_player (ligne) et lui donne un chiffre pour chaque ligne (i)
    for i, ligne in enumerate(board_bot):
        # Affichage des lettres de A à J pour les lignes avec des séparateurs
        print('\033[94m' + letters[i] + '\033[0m | ' + ' | '.join(map(str, ligne)))
        print('-' * (4 * 10 + 2))  # Ligne de séparation
    print()
            
    return [dico_boat_bot, board_bot]

def create_board_bot(size_board):
    # creer une matrice grâce au input
    # int --> matrice (list)
    # condition
    long_board_bot = []
    board_bot = []
    # Création d'un plateau de jeux qui correspond au information qui on été demander au joueur
    for row in range(size_board):
        board_bot.append([])
        for column in range(size_board):
            board_bot[row].append(0)

    return board_bot

def create_board_player(size_board):
    # creer une matrice grâce au input
    # int --> matrice (list)
    # condition
    long_board_player = []
    board_player = []
    # Création d'un plateau de jeux qui correspond au information qui on été demander au joueur
    for row in range(size_board):
        board_player.append([])
        for column in range(size_board):
            board_player[row].append(0)
    
    return board_player

def win(board):
    # verifier si il reste des bateaux(1) dans une matrice
    # matrice(list) --> bool
    # condition: \
        if all(1 in i for i in board):
            return False
        else:
            return True

def fire_player(board_bot, dico_boat_bot):
    # tirer sur une case sélectionné 
    # coordonné, plateau du bot, emplacement des bateaux --> plateau
    # condition: tirer sur le plateau et toucher ou toucher coulé
    x = int(input("Rentré les coordonné x comprise entre 1 et 10 "))-1
    y = dico_coordonne[input("Rentré une coordonné y comprise entre A et J ")]
    flow = True
    if board_bot[x][y] == 1:
        board_bot[x][y] = 'x'
        for boat in dico_boat_bot:
            if [x, y] in boat:
                dico_boat_bot[boat] -= [x, y]
                for i in boat:
                    if board_bot[i[0]][i[1]] == 1:
                        flow = False
    else:
        print("Vous n'avez subit aucun dégats !!")

    if flow == False:
        print("Touché !!")
    else:
        print("Touché coulé !!! Bien joué.")

    spe_print(board_bot)
    return board_bot

def fire_bot(liste_attack_bot, board_player, dico_boat_player):
    # tirer sur une case aléatoirement 
    # case déja tirer, plateau du bot, emplacement des bateaux--> plateau
    # condition: tirer sur le plateau et toucher ou toucher coulé et ne pas re-tirer sur la même case
    valid = False
    while valid == False:
        x = randint(0, 9)
        y = randint(0, 9)
        flow = True
        if (x, y) not in liste_attack_bot:
            if board_player[x][y] == 1:
                board_player[x][y] = 'x'
                for boat in dico_boat_player:
                    if [x, y] in boat:
                        dico_boat_player[boat] -= [x, y]
                        for i in boat:
                            if dico_boat_player[i [0]][i[1]] == 1:
                                flow = False
                liste_attack_bot.append((x, y))
                valid = True
            
                spe_print(board_player)
            else:
                print("Vous n'avez subit aucun dégats !!")

            if flow == False:
                print("Touché !!")
            else:
                print("Touché coulé !!! Bien joué.")
    
    return board_player


def spe_print(board):

    # Affichage de la grille avec des lettres pour les lignes et des chiffres pour les colonnes
    letters = 'ABCDEFGHIJ'
    # Affichage des chiffres de 1 à 10 pour les colonnes avec des séparateurs
    print('   ', end="")
    for i, number in enumerate(range(1, 10 + 1), 0):
        print('\033[94m' + " " + str(number) + " " + '\033[0m', end="")
        if i < 10 - 1:
            print('|', end="")
    print()
    print('-' * (4 * 10 + 2))  # Ligne de séparation

    # La boucle prend chaque élément de board_player (ligne) et lui donne un chiffre pour chaque ligne (i)
    for i, ligne in enumerate(board):
        # Affichage des lettres de A à J pour les lignes avec des séparateurs
        print('\033[94m' + letters[i] + '\033[0m | ' + ' | '.join(map(str, ligne)))
        print('-' * (4 * 10 + 2))  # Ligne de séparation
    print()







            

        
       

        
    