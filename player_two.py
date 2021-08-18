from player import Player

class Player_Two(Player):
    def __init__(self):
        super().__init__()

    def get_name(self):
        print('Player 2, please enter your name')
        self.name = input()