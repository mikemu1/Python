# import os
# os.environ['TERM'] = 'dumb'  # todo remove this


class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class Options(object):
    QUIT = 'quit'  # end program
    NEW = 'new'    # start new game
    GO = 'go'      # continue on with game

class Tictactoe(object):

    def __init__(self):
        self.sq_list = []
        self.players = ['X', 'O']
        self.keep = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.sq_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.q_list = ['q', 'quit']
        self.n_list = ['n', 'new']

    def reset_board(self):
        self.sq_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def show_board(self):

        def cellprint(n):
            if self.sq_list[n] == 'X' or self.sq_list[n] == 'O':
                print(Color.BOLD + ' {} '.format(self.sq_list[n]), end='')
            else:
                print(Color.GREEN + ' {} '.format(self.sq_list[n]), end='')

        # os.system('clear')
        print('\n\n')
        for i in range(0, 9):
            cellprint(i)
            if i == 2 or i == 5 or i ==8:
                print(Color.ENDC)
        print('\n')

    def get_player_input(self, current_player):
        for chances in range(3):
            square = input('Player-{} choose a square: '.format(player))
            if square.lower() in self.q_list:
                return Options.QUIT
            elif square.lower() in self.n_list:
                return Options.NEW
            elif square in self.keep:
                print(square)
                if toe.updateBoard(player, square):
                    break   # good square number and unused
        else:   # fell though for-loop without good input
            return Options.QUIT
        return Options.GO

    def updateBoard(self, xo, sq):
        if self.sq_list[int(sq)-1] in self.keep:
            self.sq_list[int(sq)-1] = xo
            return True
        else:  # something already in that square
            return False






toe = Tictactoe()

while True:  # start new game

    toe.show_board()

    for turn in range(9):   # game only has 9 squares
        # Could have chosen starting player with random,
        # but 'X' starts by convention.
        if turn % 2 == 0:
            player = toe.players[0]
        else:
            player = toe.players[1]

        option = toe.get_player_input(player)

        if option == Options.NEW:
            break  # leave for loop and start new game
        elif option == Options.QUIT:
            print('\n\n' + Color.BOLD + 'Goodbye')
            exit()
        elif option == Options.GO:
            pass
        else:
            print('\n\n' + Color.RED + 'I\'m confused, Goodbye')
            exit()

        toe.show_board()

    _ = input('New Game')

    toe.reset_board()






