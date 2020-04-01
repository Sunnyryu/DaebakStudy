'''
Complex Models using Functional API
'''

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from tensorflow import keras

housing = fetch_california_housing()

# splitting into training set, validation set, and test set

X_train_full, X_test, y_train_full, y_test = train_test_split(
    housing.data, housing.target
)

X_train, X_valid, y_train, y_valid = train_test_split(
    X_train_full, y_train_full
)

# creating input object
input_ = keras.layers.Input(shape=X_train.shape[1:])
# Dense layer with 30 neurons, with ReLU activation function, then we call it like a function, passing it the input.
hidden1 = keras.layers.Dense(30, activation="relu")(input_)
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
# Concatenate layer to concat the input and the output of the second hidden layer.
concat = keras.layers.Concatenate()([input_, hidden2])
# creating output layer
output = keras.layers.Dense(1)(concat)
# now we create the model specifying which input and output to use.
model = keras.Model(inputs=[input_], outputs=[output])

model.compile(loss="mean_squared_error", optimizer="sgd")





