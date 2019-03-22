from pygame.constants import K_DOWN  
from pygame_player import PyGamePlayer  

class PongPlayer(PyGamePlayer):  
    def __init__(self):  
        """  
        Example class for playing Pong  
        """  
        super(PongPlayer, self).__init__(force_game_fps=10) # we want to run at 10 frames per second
        self.last_bar1_score = 0.0  
        self.last_bar2_score = 0.0  

    def get_keys_pressed(self, screen_array, feedback):  
        # The code for running the actual learning agent would go here with the screen_array and feeback as the inputs
        # and an output for each key in the game, activating them if they are over some threshold.
        return [K_DOWN]  

    def get_feedback(self):  
        # import must be done here because otherwise importing would cause the game to start playing  
        from games.pong import bar1_score, bar2_score  

        # get the difference in score between this and the last run  
        score_change = (bar1_score - self.last_bar1_score) - (bar2_score - self.last_bar2_score)  
        self.last_bar1_score = bar1_score  
        self.last_bar2_score = bar2_score  
        return score_change

if __name__ == '__main__':  
    player = PongPlayer()  
    player.start()
    # importing pong will start the game playing  
    import games.pong 