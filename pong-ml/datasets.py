import data_collect
import os

def load(name):
    if (name == 'up-only'):
        dataset = data_collect.deserialize_data(os.path.join(os.getcwd(), "collected_data", "special", "up-only.dat"))
    elif (name == 'down-only'):
        dataset = data_collect.deserialize_data(os.path.join(os.getcwd(), "collected_data", "special", "down-only.dat"))
    elif (name == 'no-move'):
        dataset = data_collect.deserialize_data(os.path.join(os.getcwd(), "collected_data", "special", "no-move.dat"))
    elif (name == 'all'):
        dataset = data_collect.deserialize_all_data()

    return dataset