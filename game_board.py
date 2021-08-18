from random import randint

def the_shot(guesses):
    is_valid = 'no'
    while is_valid == 'no':
        try:
            shot = input('enter in where youd like to shoot!')
            shot = int(shot)
            if shot < 0 or shot > 99:
                print('not a valid input, try again')
            elif shot in guesses:
                print('That shot has been already been taken')
            else:
                is_valid = 'yes'
                break
        except:
            print('invalid. please enter again')
    return shot
        
def check_shot(shot, boat_one,hit,miss,final_hit):
    if shot in boat_one:
        boat_one.remove(shot)
        if len(boat_one) > 0:
            hit.append(shot)
        else:
            final_hit.append(shot)
    else:
        miss.append(shot)
    return boat_one,hit,miss,final_hit

def the_board(hit,miss, final_hit ):
    print('             Battleship')
    print('     0  1  2  3  4  5  6  7  8  9')


    position = 0

    for x in range(10):
        row = ''
        for y in range(10):
            spot = ' _ '
            if position in hit:
                spot = ' o '
            elif position in miss:
                spot = " x "
            elif position in final_hit:
                spot = ' O '
            row = row + spot
            position = position + 1 
        print(x,' ',row)

boat_one = []            
hit = []
miss = []    
final_hit = []

for i in range(10):
    already_guessed = hit + miss + final_hit
    shot = the_shot(already_guessed)
    boat_one,hit,miss,final_hit = check_shot(shot,boat_one, hit,miss,final_hit)
    the_board(hit,miss,final_hit)




