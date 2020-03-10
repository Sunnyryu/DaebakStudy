#%%

"""
Artificial neural network
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
X = iris.data[:,(2, 3)] # petal length, petal width
Y = (iris.target == 0).astype(np.int)

per_clf = Perceptron()
per_clf.fit(X, Y)

y_pred = per_clf.predict([[2, 0.5]])

#%%

# MLP (Multi-Layer Perceptron)

'''
Application could be in classifying products automatically - 
We will use an example from MNIST dataset to classify objects 
'''
import tensorflow as tf
from tensorflow import keras
tf.__version__
keras.__version__

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

X_train_full.shape
X_train_full.dtype

X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]