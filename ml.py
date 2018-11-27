import random

def next_move(suggested_move, epsilon):
    '''
    The next move as a function of the
    "Correct" suggested move and epsilon.
    Epsilon should be between 0.0 and 1.0
    '''

    rand = random.random()

    if(rand > epsilon):
        # follow the suggested move
        return suggested_move
    else:
        # try a new move
        suggested_direction = suggested_move.direction
        new_direction = random.randint(1, 4)

        while (new_direction != suggested_direction):
            new_direction = random.randint(1, 4)
        
        # TODO
        new_move = None
        # new_move = move(new_direction)

        return new_move