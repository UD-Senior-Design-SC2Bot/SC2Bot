import datetime
import os
import pickle
import time


data_dir = os.path.join(os.getcwd(), "collected_data")

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

def generate_filename():
    current_time = time.strftime("%m-%d-%Y %H hr - %M m - %S s")
    computer_name = os.environ['COMPUTERNAME']
    filename = os.path.join(data_dir, "{} - {}.dat".format(computer_name, current_time))
    return filename

def serialize_data(data):
    if (not os.path.exists(data_dir)):
        os.mkdir(data_dir)
    
    f = open(generate_filename(), "wb+")
    pickled_string = pickle.dumps(data)
    f.write(pickled_string)
    f.close()

def deserialize_data(filename):
    f = open(filename, "rb")
    data = f.read
    f.close()


