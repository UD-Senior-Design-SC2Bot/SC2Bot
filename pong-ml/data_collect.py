'''
data_collect.py

Contains various functions that serialize/deserialize
frame data.
'''

import datetime
import os
import pickle
import time
import socket
import projdirs
from frame_data import FrameData

def generate_unique_filename():
    current_time = time.strftime("%m-%d-%Y %H hr - %M m - %S s")
    computer_name = socket.gethostname()
    filename = os.path.join(projdirs.data, "{} - {}.dat".format(computer_name, current_time))
    return filename

def serialize_data(data):
    if (not os.path.exists(projdirs.data)):
        os.mkdir(projdirs.data)

    with open(generate_unique_filename(), "wb+") as session_data_file:
        pickle.dump(data, session_data_file)

def deserialize_data(filename):
    data = None
    with open(filename, "rb") as data_file:
        data = pickle.load(data_file)
    return data

def deserialize_all_data(directory):
    all_data = []

    if (not os.path.exists(directory)):
        raise Exception("Data directory does not exist " +
            "- there is no data to read.")

    for data_filename in os.listdir(directory):
        if data_filename.endswith(".dat"):
            data = deserialize_data(os.path.join(directory, data_filename))
            for frame in data:
                all_data.append(frame)

    if (len(all_data) == 0):
        raise Exception("No data found")

    return all_data

def print_dataset(dataset):
    for frame in dataset:
        print(frame)
