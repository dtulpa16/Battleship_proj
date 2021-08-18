from game_board import Game_Board

class Fleet(Game_Board):
    def __init__(self):
        super().__init__()
        self.destroyer = [0,0]
        self.sub = [0,0,0]
        self.battleship = [0,0,0,0]
        self.carrier = [0,0,0,0,0]
        self.user_fleet = []
        self.create_fleet()
        self.show_board([])
        
        
        

    def create_fleet(self):
        self.user_fleet.append(self.destroyer)
        self.user_fleet.append(self.sub)
        self.user_fleet.append(self.battleship)
        self.user_fleet.append(self.carrier)

    def show_board(self, ship):
        print('             Battleship')
        print('     0  1  2  3  4  5  6  7  8  9')
        position = 0
        for x in range(10):
            row = ''
            for y in range(10):
                spot = ' _ '
                if position in ship:
                    spot = ' # '
                row = row + spot
                position = position + 1 
            print(x,' ',row)
        #print('\033[1m' + 'Please' + '\033[0m')
        self.place_ship()

    def place_ship(self):
        for ships in self.user_fleet:
            print(f'Lets place your {len(ships)} slot ship')
            print('(Enter the left number followed by the number of the top of the board. This will be the position of the bow of the ship)')
            user_ship_placement = int(input())
            self.valid_placement(user_ship_placement)
            self.boat.append(user_ship_placement)
            self.rotate_ship(ships)
            continue

    def rotate_ship(self, ships):
            print('which direction would you like the ship to face? Type l, r, u, or d')
            user_ship_direction = input()
            if user_ship_direction == 'l':
                final_place = range(self.boat[0], self.boat[0] - len(ships), -1)
                self.show_board(final_place)
            


        
    def valid_placement(self,placement):
        is_valid = 'no'
        while is_valid == 'no':
            if placement < 0 or placement > 99:
                print('not a valid input, try again')
                self.place_ship()
            else:
                is_valid = 'yes'
                break
        return placement

