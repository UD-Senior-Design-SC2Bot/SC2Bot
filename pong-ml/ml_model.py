import data_collect
import os

# tensorflow stuff
import tensorflow as tf
from tensorflow import keras
import numpy as np

def generate_model():
    # TODO - add parameters
    dataset = data_collect.deserialize_data(os.path.join(os.getcwd(), "collected_data", "special", "up-only.dat"))

    training_coords = []
    training_correct_inputs = []

    for frame in dataset:
        tensor = np.array(frame.to_tensor())
        training_coords.append(tensor)
        training_correct_inputs.append(frame.input_opcode)

    # Convert to np arrays for tf
    training_coords = np.array(training_coords)
    training_correct_inputs = np.array(training_correct_inputs)


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

model = generate_model()

test_data = np.array([np.array([215.0, 341.5, 266.5]), np.array([10.0, 73.25, 440.75]), np.array([10.0, 81.5, 449.0])])
predictions = model.predict(test_data)

print(predictions[0])
print(predictions[1])
print(predictions[2])

print(np.argmax(predictions[0])) # Expect 1
print(np.argmax(predictions[1])) # Expect 1
print(np.argmax(predictions[2])) # Expect 1