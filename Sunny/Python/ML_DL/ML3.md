### Tensorflow

```

Hypothesis and cost

H(x) = Wx + b 
cost(W,b)를 이용해서 이 값을 최소화 된 것이 제일 좋은 값!

제곱이므로 2차함수 같은 그래프가 나옴! (코스트와 w를 가지고 그래프를 그렸을 때)

Gradient descent algorithm => 경사가 바뀌는 알고리즘

minimize cost function => 최소값 함수 , 경사가 내려가는 것을 사용하면 많은 최소화된 문제가 있음 .

경사도를 구하는 방법은 미분을 이용한다?
W를 알파(러닝렛) 

모델 컴파일
모델을 훈련하기 전에 필요한 몇 가지 설정이 모델 컴파일 단계에서 추가됩니다:

손실 함수(Loss function)-훈련 하는 동안 모델의 오차를 측정합니다. 모델의 학습이 올바른 방향으로 향하도록 이 함수를 최소화해야 합니다.
옵티마이저(Optimizer)-데이터와 손실 함수를 바탕으로 모델의 업데이트 방법을 결정합니다.
지표(Metrics)-훈련 단계와 테스트 단계를 모니터링하기 위해 사용합니다. 다음 예에서는 올바르게 분류된 이미지의 비율인 정확도를 사용합니다.
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

```

