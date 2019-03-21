import data_collect
import os

# tensorflow stuff
import tensorflow as tf
from tensorflow import keras
import numpy as np


dataset = data_collect.deserialize_data(os.path.join(os.getcwd(), "collected_data", "special", "no-move.dat"))

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
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(3, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_coords, training_correct_inputs, epochs=5)

test_data = np.array([np.array([10, 10, 10]), np.array([15, 15, 15])])
predictions = model.predict(test_data)

print(np.argmax(predictions[0]))
print(np.argmax(predictions[1]))
