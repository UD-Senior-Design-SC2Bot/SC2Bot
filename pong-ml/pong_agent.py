from pynput.keyboard import Key, Controller 
import numpy as np

class pong_agent:  
    # Simple class that loads the model and simulates player action

    def __init__(self):
        self.keyboard = Controller()


    def make_move(self):  
        # The code for running the actual learning agent would go here with the screen_array and feeback as the inputs
        # and an output for each key in the game, activating them if they are over some threshold.
        self.keyboard.press(Key.down)  

    def get_feedback(self):  
        # import must be done here because otherwise importing would cause the game to start playing  
        from games.pong import bar1_score, bar2_score  

        # get the difference in score between this and the last run  
        score_change = (bar1_score - self.last_bar1_score) - (bar2_score - self.last_bar2_score)  
        self.last_bar1_score = bar1_score  
        self.last_bar2_score = bar2_score  
        return score_change
 

class MLPongAgent():
    def __init__(self, model):
        self.keyboard = Controller()
        self.model = model
    
    def move(self, frame_tensor):
        prediction = np.argmax(self.model.predict(np.array([np.array(frame_tensor)]))[0])
        print(prediction)
        if (prediction == 2):
            self.keyboard.press(Key.down)
        elif (prediction == 1):
            self.keyboard.press(Key.up)
