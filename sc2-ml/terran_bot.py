'''
Run using "python terran_bot.py"
'''

from pysc2.agents import base_agent
from pysc2.lib import actions, features, units
from pysc2.lib.features import Player
from pysc2.env import sc2_env

from absl import app

from src.helper import get_units_by_type, can_do, unit_type_is_selected, remaining_supply, random_unit

import random

# Parameters
MAX_WORKERS = 15


class TerranAgent(base_agent.BaseAgent):
    def __init__(self):
        super(TerranAgent, self).__init__()
        self.attack_coordinates = None
        self.selected_idle_worker = False

    def init_atk_coordinates(self, obs):
        player_y, player_x = (
            obs.observation.feature_minimap.player_relative == features.PlayerRelative.SELF).nonzero()
        xmean = player_x.mean()
        ymean = player_y.mean()

        if xmean <= 31 and ymean <= 31:
            self.attack_coordinates = (49, 49)
        else:
            self.attack_coordinates = (13, 17)

    def step(self, obs):
        super(TerranAgent, self).step(obs)

        # Setting initial attack coordinates at the start of the game.
        if obs.first():
            self.init_atk_coordinates(obs)

        if remaining_supply(obs) <= 0:
            if not unit_type_is_selected(obs, units.Terran.SCV):
                scvs = get_units_by_type(obs, units.Terran.SCV)
                if len(scvs) > 0:
                    scv = random.choice(scvs)

                    return actions.FUNCTIONS.select_point("select_all_type", (scv.x,
                                                                              scv.y))
            else:
                if can_do(obs, actions.FUNCTIONS.Build_SupplyDepot_screen.id):
                    x = random.randint(0, 83)
                    y = random.randint(0, 83)

                    #actions.FUNCTIONS.Move_minimap("queued", (31, 31))
                    return actions.FUNCTIONS.Build_SupplyDepot_screen(
                        "now", (x, y))
        else:
            scvs = get_units_by_type(obs, units.Terran.SCV)
            if self.selected_idle_worker:
                minerals = get_units_by_type(obs, units.Neutral.MineralField)
                if len(minerals) > 0:
                    mineral = random_unit(minerals)

                    self.selected_idle_worker = False
                    return actions.FUNCTIONS.Harvest_Gather_screen(
                        "now", (mineral.x, mineral.y))
            if obs.observation.player[Player.idle_worker_count] > 0:
                self.selected_idle_worker = True
                return actions.FUNCTIONS.select_idle_worker("select")

            if len(scvs) < MAX_WORKERS:
                if not unit_type_is_selected(obs, units.Terran.CommandCenter):
                    command_centers = get_units_by_type(
                        obs, units.Terran.CommandCenter)
                    command_center = random_unit(command_centers)

                    return actions.FUNCTIONS.select_point("select_all_type", (command_center.x,
                                                                              command_center.y))
                else:
                    if can_do(obs, actions.FUNCTIONS.Train_SCV_quick.id):
                        return actions.FUNCTIONS.Train_SCV_quick("now")

            barracks = get_units_by_type(obs, units.Terran.Barracks)
            if len(barracks) < 2:
                if unit_type_is_selected(obs, units.Terran.SCV):
                    if can_do(obs, actions.FUNCTIONS.Build_Barracks_screen.id):
                        x = random.randint(0, 83)
                        y = random.randint(0, 83)

                        return actions.FUNCTIONS.Build_Barracks_screen(
                            "now", (x, y))
                else:
                    scvs = get_units_by_type(obs, units.Terran.SCV)
                    if len(scvs) > 0:
                        scv = random_unit(scvs)

                    return actions.FUNCTIONS.select_point(
                        "select_all_type", (scv.x, scv.y))

            marines = get_units_by_type(obs, units.Terran.Marine)
            print("before marines size: %d" % len(marines))
            if len(marines) >= 5:
                print("marines size: %d" % len(marines))
                if unit_type_is_selected(obs, units.Terran.Marine):
                    print("TRUE")
                    if can_do(obs, actions.FUNCTIONS.Attack_minimap.id):
                        return actions.FUNCTIONS.Attack_minimap("now",
                                                                self.attack_coordinates)
                else:
                    print("FALSE")
                    if can_do(obs, actions.FUNCTIONS.select_army.id):
                        return actions.FUNCTIONS.select_army("select")

            barracks = get_units_by_type(obs, units.Terran.Barracks)
            if len(barracks) > 0:
                print("barracks size %d" % len(barracks))
                if not unit_type_is_selected(obs, units.Terran.Barracks):
                    barrack = random_unit(barracks)

                    return actions.FUNCTIONS.select_point("select_all_type", (barrack.x,
                                                                              barrack.y))
                else:
                    if can_do(obs, actions.FUNCTIONS.Train_Marine_quick.id):
                        return actions.FUNCTIONS.Train_Marine_quick("queued")

        return actions.FUNCTIONS.no_op()


def main(argv):
    agent = TerranAgent()
    try:
        while True:
            with sc2_env.SC2Env(
                    map_name="Simple64",
                    players=[sc2_env.Agent(sc2_env.Race.terran),
                             sc2_env.Bot(sc2_env.Race.terran,
                                         sc2_env.Difficulty.very_easy)],
                    agent_interface_format=features.AgentInterfaceFormat(
                        feature_dimensions=features.Dimensions(
                            screen=84, minimap=64),
                        use_feature_units=True),
                    step_mul=16,
                    game_steps_per_episode=0,
                    visualize=True) as env:

                agent.setup(env.observation_spec(), env.action_spec())

                timesteps = env.reset()
                agent.reset()

                while True:
                    step_actions = [agent.step(timesteps[0])]
                    if timesteps[0].last():
                        break
                    timesteps = env.step(step_actions)

    except KeyboardInterrupt:
        pass


app.run(main)
