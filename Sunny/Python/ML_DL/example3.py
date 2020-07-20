import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() # 2.0에서는 placeholder와 Session이 사라지고 바로 할 수 있도록 바뀜.. 그래서 1.0을 사용하고 싶다면 위에 처럼 해결할 수 있음!
sess = tf.Session()
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
add_node = a + b # + provide tf.add(a,b)

print(sess.run(add_node, feed_dict={a:3, b:4.5}))
print(sess.run(add_node, feed_dict={a: [1,3], b: [3.5]}))
print(sess.run(add_node, feed_dict={a:[1,3,5], b: [2,4,6]}))
