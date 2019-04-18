'''
datasets.py

An access point for reading in datasets.
'''

import data_collect
import projdirs
import os

def load(name):
    return loadn(name, -1)

def loadn(name, n):
    '''
    Loads n frames from a dataset.
    Loads all frames if n = -1.
    '''
    if (name == 'up-only'):
        dataset = data_collect.deserialize_data(os.path.join(projdirs.data_special, "up-only.dat"))
    elif (name == 'down-only'):
        dataset = data_collect.deserialize_data(os.path.join(projdirs.data_special, "down-only.dat"))
    elif (name == 'no-move'):
        dataset = data_collect.deserialize_data(os.path.join(projdirs.data_special, "no-move.dat"))
    elif (name == 'all'):
        dataset = data_collect.deserialize_all_data(projdirs.data)
    elif (name == 'ideal'):
        dataset = data_collect.deserialize_all_data(projdirs.data_special_ideal)

    if (n == -1):
        return dataset
    else:
        return dataset[0:min(n, len(dataset))]