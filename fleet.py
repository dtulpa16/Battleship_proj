class Fleet:
    def __init__(self):
        self.destroyer = [0,0]
        self.sub = [0,0,0]
        self.battleship = [0,0,0,0]
        self.carrier = [0,0,0,0,0]
        self.user_fleet = []
        self.create_fleet()
        self.show_board()
        
        

    def create_fleet(self):
        self.user_fleet.append(self.destroyer)
        self.user_fleet.append(self.sub)
        self.user_fleet.append(self.battleship)
        self.user_fleet.append(self.carrier)

    def show_board(self):
        print('             Battleship')
        print('     0  1  2  3  4  5  6  7  8  9')
        position = 0
        for x in range(10):
            row = ''
            for y in range(10):
                spot = ' _ '

                row = row + spot
                position = position + 1 
            print(x,' ',row)
        print('\033[1m' + 'Please' + '\033[0m')
        self.place_ship()

    def place_ship(self):
        for ships in self.user_fleet:
            print(f'Lets begin with placing your {len(ships)} slot ship')
            print('(Enter the top number followed by the number of the left of the board. This will be the position of the bow of the ship)')
            user_ship_placement = input()
            self.valid_placement(user_ship_placement)
        
    def valid_placement(self,placement):
        pass
