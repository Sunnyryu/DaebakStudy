"""
Artificial neural network
Using Python 3.6.2 64-bit
"""

# Perceptron (Threshold Logic Unit)

'''
Example of training a single TLU  -
Taking iris preset from scikit package 
'''
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron

iris = load_iris()
X = iris.data[:, (2, 3)]  # petal length, petal width
Y = (iris.target == 0).astype(np.int)

per_clf = Perceptron()
per_clf.fit(X, Y)

y_pred = per_clf.predict([[2, 0.5]])


# MLP (Multi-Layer Perceptron)

'''
Application could be in classifying products automatically - 
We will use an example from MNIST dataset to classify objects 
'''

import tensorflow as tf
from tensorflow import keras

print(tf.__version__)
print(keras.__version__)

'''
using keras to load the dataset.
every image is represented as a 28x28 array
pixel intensities are represented as integers from 0 to 255
'''

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

X_train_full.shape
X_train_full.dtype

'''
we must scale the input features first by
splitting the dataset in to validation/train set, and scale the pixel intensity.
'''

X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

class_names[y_train[0]]

'''
building the neural network
'''

model = keras.models.Sequential() #creating sequential model
model.add(keras.layers.Flatten(input_shape=[28, 28])) # flatten layer to convert each input image into 1D array
model.add(keras.layers.Dense(300, activation="relu")) # dense layer with 300 neurons with ReLU activation function
model.add(keras.layers.Dense(100, activation="relu")) # 100
model.add(keras.layers.Dense(10, activation="softmax")) # 10 with softmax activation function (because classes are exclusive)

# checking out the model details
print(model.summary())
print(model.layers)
hidden1 = model.layers[1]
print(hidden1.name)
print(model.get_layer('dense') is hidden1)

# checking the weights and the biases within
weights, biases = hidden1.get_weights()
print(weights)
print(weights.shape)
print(biases)
print(biases.shape)

'''
compiling the model - 
sparse_categorical_crossentropy because we have sparse labels (for each instance, there is just a target class index, 0 to 9)
sgd because we will train the model using simple Stochastic Gradient Descent
and since this is a classifier, we will measure the accuracy during train/eval.
'''

model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

history = model.fit(X_train, y_train, epochs=30, validation_data=(X_valid, y_valid))

model.evaluate(X_test, y_test)

'''
using the model to make the predictions
'''

X_new = X_test[:3]
y_proba = model.predict(X_new)
print(y_proba.round(2))

y_pred = model.predict_classes(X_new)
print(y_pred)
print(np.array(class_names)[y_pred])

y_new = y_test[:3]
print(y_new)
