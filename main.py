# TODO
# 

import os
from plateau import Game_board


os.system('cls') # windows
os.system('clear') # linux


#"""""""""""""""""""""""" MAIN """"""""""""""""""""""""""""""""""""""""

# instanciation du plateau
game_board = Game_board()

# game_board.list_compagnies()
# game_board.list_gares()
# game_board.list_proprietes()
# game_board.list_all()
# game_board.list_chance()
# game_board.list_communaute()
# exit()

game_board.init_game()

while input("***************************************\n\nSouhaitez-vous quitter la partie (o/N) ? \n") != "o":
    game_board.play()
