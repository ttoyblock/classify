# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt

from models import inference
from frame.config import LOG_DIR
from tools.download import deal_images


def get_one_image(img_dir):
    # Image.open()好像一次只能打开一张图片
    image = Image.open(img_dir)
    plt.imshow(image)
    image = image.resize([208, 208])
    image_arr = np.array(image)
    return image_arr


def sc_check(image_dir):
    ret = {}
    files = deal_images(image_dir)
    for url, file in files.items():
        image_arr = get_one_image(file)

        with tf.Graph().as_default():
            image = tf.cast(image_arr, tf.float32)
            image = tf.image.per_image_standardization(image)
            image = tf.reshape(image, [1, 208, 208, 3])
            # print(image.shape)
            p = inference(image, 1, 3)
            logits = tf.nn.softmax(p)
            x = tf.placeholder(tf.float32, shape=[208, 208, 3])
            saver = tf.train.Saver()
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(LOG_DIR)
                if ckpt and ckpt.model_checkpoint_path:
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    # 调用saver.restore()函数，加载训练好的网络模型
                    saver.restore(sess, ckpt.model_checkpoint_path)

                    # print('Loading success')
                else:
                    print('No checkpoint')
                prediction = sess.run(logits, feed_dict={x: image_arr})
                # max_index = np.argmax(prediction) 
                # print('预测的标签为：')
                # print(max_index)
                # print('预测的结果为：')
                # print(prediction)

                ret[url] = {'se': round((prediction[0][0]), 2), 'ad': round((prediction[0][1]), 2)}
                # if max_index == 0:
                #     print('This is a SE with possibility %.6f' % prediction[:, 0])
                # elif max_index == 1:
                #     print('This is a AD with possibility %.6f' % prediction[:, 1])
                # else:
                #     print('This is a CM with possibility %.6f' % prediction[:, 2])
    return ret
