# Summary: 简单了解张量(tensor)的知识点
# Author: Amusi
# Date:   2017-11-09
# Version: tensorflow1.4

import tensorflow as tf
# tf.constant是一个计算，这个计算的结果为一个张量，保存在变量ａ中
a = tf.constant([1.0, 2.0], name = "a", dtype=tf.float32)
b = tf.constant([2.0, 3.0], name = "b", dtype=tf.float32)
result = tf.add(a, b, name = "add")

# 输出张量属性
print(result)

# 输出计算结果
print(tf.Session().run(result))