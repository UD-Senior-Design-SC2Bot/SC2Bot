from pynput.keyboard import Key, Controller 
import numpy as np

class MLPongAgent():
    def __init__(self, model):
        self.keyboard = Controller()
        self.model = model
    
    def get_next_move(self, frame_tensor):
        ptensor = self.model.predict(np.array([np.array(frame_tensor)]))[0]        
        prediction = np.argmax(ptensor)
        print("{} <- {}".format(prediction, ptensor))
        return prediction
