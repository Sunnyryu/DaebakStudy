### Machine Learning 

```
Machine Learning

머신러닝
일종의 소프트웨어 프로그램과 비슷하며, explicit programming의 제한..
(ex) 스팸필터 -> 규칙이 많아서 개발자들이 일일이 이런경우 저런경우를 잡기가 어려움!)
(자동제어 같이 규칙이 너무 많아... )

1959년에 아트라는 사람이 우리가 아닌 자료에서 현상에서 자종적으로 배우면 어떨까... 프로 랙인데 이것을 개발자가 일일이 어떻게 하는 지를 정하지 않고 프로그램 자체가 어떤 데이터를 보고 학습해서 뭔가를 배우는 능력을 갖는 프로그램이 머신러닝

- 데이터가 미리 주어쟈하며 학습하는 방법에 따라 supervised learning 나 unsupervised learning으로 나눠짐

supervised learning 
어떤 하나의 정해져 있는 데이터 그리고 데이터는 이미 레이블 들이 정해져 있음.. 레이블이 정해져 있는 데이터. 다른말로는 트레이닝 셋이라고 하며, 이 데이터를 가지고 학습을 하는 것!
ex) 이미지를 줘서 4가지 단어로 구분하는 알아내는 프로그램들이 supervised learning의 예임!

이런 경우에 학습이 이미 레이블이 달려있는 자료를 학습을 하기 떄문에 이런 학습을 supervised learning이라고 함!

unsupervised learning 
구글뉴스의 경우 자동적으로 유사한 뉴스들을 그룹핑을 하며, 이런 경우. 미리 레이블을 나열하기 어렵기에 .. 자기가 보고 유사한 것끼리 모으며, 단어들 가운데도 비슷한 단어들을 모아보면 .. => 레이블을 직접 만들어주는 것이 아닌 데이터를 스스로 학습함 => 이것은 unsupervised learning이라고 할 수 있음(unlabeled data)


Supervised learning

대부분의 머신러닝 안에 일반적인 문제 유형

lmage labeling (이미지 레이블 한다든가), email spam filter(스팸 필터의 경우 이런 이메일이 스팸이고 아닌 것은 아닌지에 대해서 그런 것들을 레이블을 매겨놓은 것을 가지고 학습을 함!)

Predicting exam score(어떤 시험을 치는데 점수가 얼마나 나올까.. 얼마나 준비했는데 상대적으로 점수가 얼마다라는 데이터가 있다면 이 것을 가지고 머신러닝을 할 수 있음!)

Training data set
슈퍼바이저드 러닝에서 사용되는 머신러닝은 머신러닝이라는 모델이 있고.. 이미 답이 정해져있는 (레이블이 정해져 있는 ) 레이블이 정해져있는 그 값을 y라고 많이하며, x는 이 값을  특정이라고하며 피치라고 하는데.. 데이터를 가지고 학습(y의 값)을 하게되면 모델이 쭉 발생하는 거고 이제 학습을 통해 내가 모르던 x가 있는데.. x.test라고 하면 그 값이 [9,3,6]이며, y는 앞의 값이 [9,3,6] 일때 y는 3이다라는 정리를 해낼 수 있다.

alphago => 기존의 바둑데이터를 학습한 것이며, 이 때 이 데이터를 입력을 받아 받는 쪽에 이것을 두면 되겠다 하여 슈퍼바이저 러닝이라고 할 수 있을 것이며, 사용된 데이터가 바로 트레이닝 데이터셋이라고 할 수 있음 

supervised learning의 종류

- 시험 성적 예측에 기초된 타임 스펜트 -> 리그레션 (0 ~100까지 범위가 넓은 것을 예측 regression)

- 점수테스를 했을 때 이것이 pass인지 non-pass인지로 나눠본다면 두 가지로 나눠 볼 경우 똑같은 시간을 사용해서 둘 중에 하나를 고르는 것.. 분류(classification이라고 함! => 2개 중에 하나를 고르는 거라면 binary classification이라고 할 수있음)

- Letter grade(a,b,c,d anf f)에 기초된 time spent => a,b,c,d,e,f 중 하나를 고르것이므로 classification이지만 범위가 많으므로 멀티라벨 클래시피케이션이라고 함!


ex) 시험점수 에측을 하는 데이터가 있다면 10시간 공부해서 90점, 9시간 80점 , 3시간 50점, 2시간 20인 데이터를 가지고 트레이닝 함(regression)=> 예를들어 7시간을 공부했을 때 .. y가 얼마인가!??를 예측함

몇 시간 공부하냐에 따라 pass/faill로 나누는 것을 classification이라고함 => 2개 가지고만 p,f를 구별하면 binary classification이라고 할 수 있음!! 

letter grade (a,b,c,d 등의 여러개의 결과값이 있을 경우 multi level classification이라고 할 수 있음!!)
```

```
tensor는 일반적인 array로 사용 되옵니다.
rank 0 => Scalar s = 100 / rank 1 => vector [1,2,3] 
rank 2 = m = [[1,2],[3,4]] ... n차까지 있음

shape는 각각에 요소에 몇개들어있냐에 따라 0,0-D ([]), 1,1-D [X], 2.2-D [X,Y]
라고 할 수 있음

DT_FLOAT => tf.float32 / DT_DOUBLE => tf.float64
DT_INT8,16,32,64 => 8bit, 16bit, 32bit, 64bit
```

