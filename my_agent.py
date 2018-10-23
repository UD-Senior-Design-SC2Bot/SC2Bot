'''
Run using "python -m pysc2.bin.agent --map Simple64 --agent my_agent.MyAgent"
'''

from pysc2.agents import base_agent
from pysc2.lib import actions

import time
import datetime
import logger

class MyAgent(base_agent.BaseAgent):
    def __init__(self):
        super(MyAgent, self).__init__()
        self.logger = logger.Logger("Logs/Log.txt")
        self.logger.log("********** Logged on {} **********".format(datetime.datetime.now()))

    def step(self, obs):
        '''
        step() is the atomic operation that
        is called repeatedly over the course 
        of the game
        '''
        self.steps += 1
        

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
        # Log the amount of minerals
        minerals = obs.observation['player'][1]
        vespene = obs.observation['player'][2]
        idle_workers = obs.observation['player'][7]
        food_used = obs.observation['player'][8]

        self.logger.log("-- Step {}".format(self.steps))
        self.logger.log("\t Minerals:     {}".format(minerals))
        self.logger.log("\t Vespene:      {}".format(vespene))
        self.logger.log("\t Idle Workers: {}".format(idle_workers))
        self.logger.log("\t Food used:    {}".format(food_used))

        # Do nothing
        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])