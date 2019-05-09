import numpy as np

class FrameData():
    '''
    A snapshot of game variables at a particular
    frame. Can be converted to a tensor for use
    in generating a predictive model that plays
    pong.
    '''
    def __init__(self, frame_no, input_opcode, pxarray):
        '''
        input_opcode:
            0 = noop
            1 = move right
            2 = move left
            3 = shoot
        '''
        self.frame_no = frame_no
        self.input_opcode = input_opcode
        self.pxarray = pxarray

    def to_tensor(self):



        #return [self.player_coord , self.player_bullet, self.enemies, self.enemy_bullets, self.barrier_particles, self.lives, self.score]

        return self.pxarray

    def to_processed_tensor(self):
        arr = []
        arr = np.array(self.pxarray)
        arr = arr/16724992
        arr = arr.tolist()
        return arr

    def __str__(self):
        return "{} | {} | {} | {} | {} | {} | {} | {} | {}".format(self.frame_no, self.input_opcode, self.player_coord, self.player_bullet, self.enemies, self.enemy_bullets, self.barrier_particles, self.lives, self.score)
