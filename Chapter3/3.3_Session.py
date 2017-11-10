# Summary: 简单了解会话(session)的知识点
# Author: Amusi
# Date:   2017-11-10
# Version: tensorflow1.4

import tensorflow as tf

# 自定义变量
a = tf.constant(8.0)
b = tf.constant(2.0)
result = tf.add(a, b, "add")

# 方式１(常用)——明确会话生成函数和关闭会话函数
# 创建一个会话
sess = tf.Session()
# 运行会话
# 运行方式１
print("result1:", sess.run(result))
# 运行方式２
print("result2:", result.eval(session=sess))
# 关闭会话
sess.close()

# 方式２(常用)——Python上下文管理器，不需要考虑资源释放问题
with tf.Session() as sess:
    print("result3:", sess.run(result))

# 方式３(不常用)——设定默认会话计算张量的取值
sess = tf.Session()
with sess.as_default():
    print("result4:", result.eval())

# 方式４(适用于Jupyter)——交互式环境下，设定默认会话计算张量的取值
# 可省去将生成会话注册成默认会话的过程
sess = tf.InteractiveSession()
print("result5:", result.eval())
sess.close()

# 方式５()
config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
sess1 = tf.InteractiveSession(config=config)
print("result6:", sess1.run(result))
sess2 = tf.Session(config=config)
print("result7:", sess2.run(result))

