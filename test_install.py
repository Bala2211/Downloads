import tensorflow as tf
session=tf.Session()
hello=tf.constant(" Hello Bala to Tensorflow")
print(session.run(hello))
a=tf.constant(22)
b=tf.constant(12)
print(session.run(a*b))
