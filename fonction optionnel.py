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