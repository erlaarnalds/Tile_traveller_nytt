import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")

def lever(prevcoins):
    yesorno = ['y', 'n']
    leverpull = random.choice(yesorno)
    print('Pull a lever (y/n): {}'.format(leverpull))

    if leverpull == 'y':
        print('You received 1 coin, your total is now {}.'.format(prevcoins+1))
        coins = prevcoins +1
    else:
        coins = prevcoins
    
    return coins

def islever(col, row, coins):
    if col == 1 and row == 2:
        newcoins = lever(coins)
    elif col == 2 and row == 2:
        newcoins = lever(coins)
    elif col == 2 and row == 3:
        newcoins = lever(coins)
    elif col == 3 and row == 2:
        newcoins = lever(coins)
    else:
        newcoins = coins
    
    return newcoins

        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions, coins):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row ''' 
    victory = False
    pickone = [NORTH, EAST, SOUTH, WEST]
    direction = random.choice(pickone)
    print("Direction: {}".format(direction))
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        coins = islever(col, row, coins)
    return victory, col, row, coins

# The main program starts here
play = True

while play == True:
    seed = int(input('Input seed: '))
    random.seed(seed)

    victory = False
    row = 1
    col = 1
    coins = 0
    moves = 0

    valid_directions = NORTH
    print_directions(valid_directions)

    while not victory:
        victory, col, row, coins = play_one_move(col, row, valid_directions, coins)
        moves += 1
        if victory:
            print("Victory! Total coins {}. Moves {}.".format(coins, moves))
            answer = input('Play again (y/n): ').lower()

            if answer == 'y':
                continue
            else:
                play = False
        else:
            valid_directions = find_directions(col, row)
            print_directions(valid_directions)
