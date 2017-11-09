# Summary: 简单了解计算图的知识点
# Author: Amusi
# Date:   2017-11-05
# Version: tensorflow1.4
import tensorflow as tf

g1 = tf.Graph()
with g1.as_default():
    # 在计算图ｇ１中定义变量"v"，并初始化为０
    v = tf.get_variable(
        "v", initializer= tf.zeros_initializer, shape=(1.)
    )



g2 = tf.Graph()
with g2.as_default():
    # 在计算图g2中定义变量"v"，并初始化为１
    v = tf.get_variable(
        "v", initializer=tf.ones_initializer, shape=(1.)
    )

# 在计算图g1中读取变量的取值
with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        # 在计算图g1中，变量"v"的取值应该为０，所以下面这行会输出[0.]
        print(sess.run(tf.get_variable("v")))

# 在计算图g2中读取变量的取值
with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        # 在计算图g2中，变量"v"的取值应该为１，所以下面运行会输出[1.]
        print(sess.run(tf.get_variable("v")))
