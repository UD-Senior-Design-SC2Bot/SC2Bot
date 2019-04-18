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

    def to_tensor(self):
        return [self.bar_y, self.ball_x, self.ball_y]

    def to_processed_tensor(self):
        # The game field is 640x480
        return [self.bar_y/480, self.ball_x/640, self.ball_y/480]

    def __str__(self):
        return "{} | {} | {} | {} | {}".format(self.frame_no, self.input_opcode, self.bar_y, self.ball_x, self.ball_y)