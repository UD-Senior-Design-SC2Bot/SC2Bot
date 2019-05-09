import data_collect
import datasets
import os

# tensorflow stuff
import tensorflow as tf
from tensorflow import keras
import numpy as np

game_x = 640
game_y = 480

paddle_movement = ['No-Move', 'Right', 'Left', 'Shoot']

class SpaceInvadersModel():
    '''
    A machine learning model that predicts the next
    move to take in the game.
    '''
    def __init__(self, dataset):
        self.model = self.__generate_model(dataset)

    def get_next_move(self, frame_tensor):
        ptensor = self.model.predict(np.array([np.array(frame_tensor)]))[0]
        prediction = np.argmax(ptensor)
        print("{} <- {}".format(prediction, ptensor))
        return prediction

    def __generate_model(self, dataset):
        '''
        Generates a machine-learning model for pong
        based on a given dataset
        '''
        # Convert the dataset into numpy tensors
        training_coords = []
        training_correct_inputs = []
        for frame in dataset:
            #print(frame.to_processed_tensor())
            #break
            tensor = np.array(frame.to_processed_tensor(), dtype=float) # Convert frame to a normalized tensor
            training_coords.append(tensor)
            training_correct_inputs.append(frame.input_opcode)

        # Convert to np arrays for tf
        training_coords = np.array(training_coords)
        training_correct_inputs = np.array(training_correct_inputs)

        # Multi-layered keras model
        model = keras.Sequential([
            keras.layers.Flatten(),#input_shape=(800, 600)
            keras.layers.Dense(12, activation=tf.nn.relu),
            keras.layers.Dense(4, activation=tf.nn.softmax)
        ])
        model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

        model.fit(training_coords, training_correct_inputs, epochs=5)

        return model

    def __test_special_model(model, expected_val):
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
