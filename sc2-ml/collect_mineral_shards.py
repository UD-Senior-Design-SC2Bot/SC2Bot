'''
Run using "python3 -m pysc2.bin.agent --map CollectMineralShards --agent collect_mineral_shards.MyAgent"
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

import time
import datetime
import logger
import random

_PLAYER_SELF = features.PlayerRelative.SELF
_PLAYER_NEUTRAL = features.PlayerRelative.NEUTRAL  # beacon/minerals
_PLAYER_ENEMY = features.PlayerRelative.ENEMY

FUNCTIONS = actions.FUNCTIONS

log_filename = "Logs/Minerals/Log" + datetime.datetime.now().isoformat() + ".txt"
log_filename = log_filename.replace(":", "-")

def _xy_locs(mask):
    """Mask should be a set of bools from comparison with a feature layer."""
    y, x = mask.nonzero()
    return list(zip(x, y))

def _mineral_log(minerals):
    f = open(log_filename, "a")
    f.write("********** Logged on {} **********\n".format(datetime.datetime.now()))
    f.write(str(minerals)+ "\n\n")
    f.close()

def _move(xy_coord, direction):
    x_coord = int(xy_coord[0])
    y_coord = int(xy_coord[1])
    #right
    if direction == 0:
        x_coord = x_coord + 5
    #left
    elif direction == 1:
        x_coord = x_coord - 5
    #up
    elif direction == 2:
        y_coord = y_coord + 5
    #down
    else:
        y_coord = y_coord - 5

    new_coord = (x_coord,y_coord)
    return new_coord

class MyAgent(base_agent.BaseAgent):

    def __init__(self):
        f = open(log_filename, "w")
        f.close()
        print("Starting")
        filename = "Logs/Minerals/Log" + datetime.datetime.now().isoformat() + ".txt"
        super(MyAgent, self).__init__()

    def step(self, obs):
        super(MyAgent, self).step(obs)

        if FUNCTIONS.Move_screen.id in obs.observation.available_actions:
            player_relative = obs.observation.feature_screen.player_relative
            minerals = _xy_locs(player_relative == _PLAYER_NEUTRAL)
            if not minerals:
                return FUNCTIONS.no_op()
            _mineral_log(minerals)
            marines = _xy_locs(player_relative == _PLAYER_SELF)
            marine_xy = numpy.mean(marines, axis=0).round()  # Average location.
            distances = numpy.linalg.norm(numpy.array(minerals) - marine_xy, axis=1)
            closest_mineral_xy = minerals[numpy.argmin(distances)]

            direction = random.randint(0,3)
            print(marine_xy)
            new_coord = _move(marine_xy, direction)
            time.sleep(0.05)
            #return FUNCTIONS.Move_screen("now", closest_mineral_xy)
            return FUNCTIONS.Move_screen("now", new_coord)
        else:
            return FUNCTIONS.select_army("select")
