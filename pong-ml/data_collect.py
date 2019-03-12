import datetime
import os
import pickle
import time

class FrameData():
    def __init__(self, frame_no, input_opcode, bar_y, ball_x, ball_y):
        '''
        input_opcode:
            0 = noop
            1 = move up
            2 = move down
        '''
        self.frame_no = frame_no
        self.input_opcode = input_opcode
        self.bar_y = bar_y
        self.ball_x = ball_x
        self.ball_y = ball_y
    
    def __str__(self):
        return "{} | {} | {} | {} | {} | {}".format(self.frame_no, self.input_opcode, self.bar_y, self.ball_x, self.ball_y)

def serialize_data(data):
    current_time = time.strftime("%Y%m%d-%H%M%S")
    computer_name = os.environ['COMPUTERNAME']
    filename = os.path.join(os.getcwd(), "collected_data", "{} - {}.dat".format(computer_name, current_time))
    # filename = os.path.join(os.getcwd(), "collected_data", "haha.txt")

    f = open(filename, "wb+")
    pickled_string = pickle.dumps(data)
    f.write(pickled_string)
    f.close()

def deserialize_data(filename):
    f = open(filename, "rb")
    data = f.read

