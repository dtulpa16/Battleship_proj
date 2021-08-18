from player import Player

class Player_One(Player):

    def __init__(self):
        super().__init__()
        self.get_name()

    def get_name(self):
        print('Player 1, please enter your name')
        self.name = input()
        


