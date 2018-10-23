'''
Run using "python -m pysc2.bin.agent --map Simple64 --agent my_agent.MyAgent"
'''

from pysc2.agents import base_agent
from pysc2.lib import actions

import time

class MyAgent(base_agent.BaseAgent):
    def step(self, obs):
        '''
        step() is the atomic operation that
        is called repeatedly over the course 
        of the game
        '''
        super(MyAgent, self).step(obs)
        
        time.sleep(0.5)

        '''
        obs.observation['player'] returns an (11) tensor with the following data:
            - player_id
            - minerals
            - vespene
            - food used (otherwise known as supply)
            - food cap
            - food used by army
            - food used by workers
            - idle worker count
            - army count
            - warp gate count (for protoss)
            - larva count (for zerg)
        '''
        print(obs.observation['player'][1]) # Print the amount of minerals

        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])