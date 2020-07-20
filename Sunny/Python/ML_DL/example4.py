import numpy as np
import tensorflow as tf

x_train = [1, 2, 3, 4]
y_train = [1,2,3,4]

tf.model = tf.keras.Sequential()
#케라스에서는 층(layer)을 조합하여 모델(model)을 만듭니다.
# 모델은 (일반적으로) 층의 그래프입니다. 가장 흔한 모델 구조는 층을 차례대로 쌓은 tf.keras.Sequential 모델


# units == output shape, input_dim == input shape
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=1))
# Dense
#keras.layers.Dense(units, activation=None, use_bias=True, 
# kernel_initializer='glorot_uniform', bias_initializer='zeros', 
# kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
#보통의 밀집 연결 신경망 레이어.

#Dense는 다음과 같은 작업을 구현합니다: output = activation(dot(input, kernel) + bias) 
# 여기서 activation은 activation 인수로 전달되는 성분별 활성화 함수이고,
#  kernel은 레이어가 만들어낸 가중치 행렬이며, bias는 레이어가 만들어낸 편향 벡터입니다 (use_bias가 True인 경우만 적용 가능합니다).

sgd = tf.keras.optimizers.SGD(lr=0.1)  # SGD == standard gradient descendent, lr == learning rate
tf.model.compile(loss='mse', optimizer=sgd)  # mse == mean_squared_error, 1/m * sig (y'-y)^2
#optimizer: 훈련 과정을 설정합니다. tf.keras.optimizers.Adam이나
#tf.keras.optimizers.SGD와 같은 tf.keras.optimizers 아래의 옵티마이저 객체를 전달합니다. 기본 매개변수를 사용할 경우 'adam'이나 'sgd'와 같이 문자열로 지정할 수도 있습니다.
#loss: 최적화 과정에서 최소화될 손실 함수(loss function)를 설정합니다. 평균 제곱 오차(mse)와 categorical_crossentropy, binary_crossentropy 등이 자주 사용됩니다. 손실 함수의 이름을 지정하거나 tf.keras.losses 모듈 아래의 호출 가능한 객체를 전달할 수 있습니다.
#metrics: 훈련을 모니터링하기 위해 사용됩니다. 이름이나 tf.keras.metrics 모듈 아래의 호출 가능한 객체입니다.
# prints summary of the model to the terminal
tf.model.summary()

# fit() executes training
tf.model.fit(x_train, y_train, epochs=200)

# predict() returns predicted value
y_predict = tf.model.predict(np.array([5, 4]))
print(y_predict)
