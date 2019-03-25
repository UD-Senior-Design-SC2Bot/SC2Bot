import data_collect
import datasets
import os

# tensorflow stuff
import tensorflow as tf
from tensorflow import keras
import numpy as np

game_x = 640
game_y = 480

paddle_movement = ['No-Move', 'Up', 'Down']

def generate_model(dataset):
    '''
    Generates a machine-learning model for pong
    based on a given dataset
    '''
    # Convert the dataset into numpy tensors
    training_coords = []
    training_correct_inputs = []
    for frame in dataset:
        tensor = np.array(frame.to_processed_tensor()) # Convert frame to a normalized tensor
        training_coords.append(tensor)
        training_correct_inputs.append(frame.input_opcode)

    # Convert to np arrays for tf
    training_coords = np.array(training_coords)
    training_correct_inputs = np.array(training_correct_inputs)

    # Multi-layered keras model
    model = keras.Sequential([
        keras.layers.Flatten(),
        keras.layers.Dense(5, activation=tf.nn.relu),
        keras.layers.Dense(3, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam', 
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(training_coords, training_correct_inputs, epochs=5)

    return model

def test_special_model(model, expected_val):    
    print("-- Testing model for a {}-Only paddle".format(paddle_movement[expected_val]))
    # arbitrary test data - MAKE SURE IT'S NORMALIZED!!
    test_data = np.array([
        np.array([0.1, 0.1, 0.1]), 
        np.array([0.2, 0.2, 0.2]),
        np.array([0.3, 0.3, 0.3]),
        np.array([0.4, 0.4, 0.4]),
        np.array([0.5, 0.5, 0.5]), 
        np.array([0.6, 0.6, 0.6]), 
        np.array([0.7, 0.7, 0.7])])
    
    predictions = model.predict(test_data)
    for prediction in predictions:
        print("Predictions: {}. For most probable move, expected {} and got {}" \
            .format(prediction, paddle_movement[expected_val], paddle_movement[np.argmax(prediction)]))
    
'''
# model for a paddle that never moves
no_move_model = generate_model(datasets.load('no-move'))
# model for a paddle that only moves up
up_only_model = generate_model(datasets.load('up-only'))
# model for a paddle that only moves down
down_only_model = generate_model(datasets.load('down-only'))

test_special_model(no_move_model, 0)
test_special_model(up_only_model, 1)
test_special_model(down_only_model, 2)
'''