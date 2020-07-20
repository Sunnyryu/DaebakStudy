import tensorflow as tf

hello = tf.constant("Hello, Tensorflow!")
# 콘스턴트를 만듬, 그래프 속에 노드를 만듬..

#sess = tf.Session() 2.0 부터 세션을 만들고 런하는 과정이 사라짐
#print(sess.run(hello))
tf.print(hello)