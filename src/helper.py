'''
Created on Nov 2, 2018

@author: DPain
'''

import random


def get_units_by_type(obs, unit_type):
    return [
        unit for unit in obs.observation.feature_units if unit.unit_type == unit_type]


def can_do(obs, action):
    return action in obs.observation.available_actions


def unit_type_is_selected(obs, unit_type):
    if (len(obs.observation.single_select) > 0 and
            obs.observation.single_select[0].unit_type == unit_type):
        return True

    if (len(obs.observation.multi_select) > 0 and
            obs.observation.multi_select[0].unit_type == unit_type):
        return True

    return False


def remaining_supply(obs):
    return obs.observation.player.food_cap - obs.observation.player.food_used


def random_unit(unit):
    if len(unit) > 0:
        return random.choice(unit)
