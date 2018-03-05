# -*- coding: utf-8 -*-
import os
import numpy as np
import tensorflow as tf
# import matplotlib.pyplot as plt


def get_files(file_dir):
    SE = []
    label_SE = []
    AD = []
    label_AD = []
    CM = []
    label_CM = []
    # 定义存放各类别数据和对应标签的列表，列表名对应你所需要分类的列别名
    # SE，AD等是我的数据集中要分类图片的名字

    for dir in os.listdir(file_dir):
        d = file_dir + dir + '/'
        print d
        for file in os.listdir(d):
            if dir == '0':
                SE.append(d+file)
                label_SE.append(0)
            elif dir == '1':
                AD.append(d+file)
                label_AD.append(1)
            else:
                CM.append(d+file)
                label_CM.append(2)
        # 根据图片的名称，对图片进行提取，这里用.来进行划分
        # 这里一定要注意，如果是多分类问题的话，一定要将分类的标签从0开始。
            # 这里是五类，标签为0，1，2，3，4。我之前以为这个标签应该是随便设置的，结果就出现了Target[0] out of range的错误。

    print('There are %d SE\nThere are %d AD\nThere are %d CM' % (len(SE), len(AD), len(CM)))
    # 打印出提取图片的情况，检测是否正确提取

    image_list = np.hstack((SE, AD, CM))
    label_list = np.hstack((label_SE, label_AD, label_CM))
    # 用来水平合并数组

    temp = np.array([image_list, label_list])
    temp = temp.transpose()
    np.random.shuffle(temp)

    image_list = list(temp[:, 0])
    label_list = list(temp[:, 1])
    label_list = [int(i) for i in label_list]

    print image_list
    return image_list, label_list
    # 返回两个list


def get_batch(image, label, image_W, image_H, batch_size, capacity):
    image = tf.cast(image, tf.string)
    label = tf.cast(label, tf.int32)
    # tf.cast()用来做类型转换

    input_queue = tf.train.slice_input_producer([image, label])
    # 加入队列

    label = input_queue[1]
    image_contents = tf.read_file(input_queue[0])
    image = tf.image.decode_jpeg(image_contents, channels=3)
    # jpeg或者jpg格式都用decode_jpeg函数，其他格式可以去查看官方文档

    image = tf.image.resize_image_with_crop_or_pad(image, image_W, image_H)
    # resize

    image = tf.image.per_image_standardization(image)
    # 对resize后的图片进行标准化处理

    image_batch, label_batch = tf.train.batch([image, label], batch_size=batch_size, num_threads=16, capacity=capacity)

    label_batch = tf.reshape(label_batch, [batch_size])
    return image_batch, label_batch
    # 获取两个batch，两个batch即为传入神经网络的数据


# def view():
#     BATCH_SIZE = 5
#     CAPACITY = 64
#     IMG_W = 208
#     IMG_H = 208

#     image_list, label_list = get_files(config.TRAIN_DIR)
#     image_batch, label_batch = get_batch(image_list, label_list, IMG_W, IMG_H, BATCH_SIZE, CAPACITY)

#     with tf.Session() as sess:
#         i = 0
#         coord = tf.train.Coordinator()
#         threads = tf.train.start_queue_runners(coord=coord)
#         try:
#             while not coord.should_stop() and i < 2:
#                 # 提取出两个batch的图片并可视化。
#                 img, label = sess.run([image_batch, label_batch])

#                 for j in np.arange(BATCH_SIZE):
#                     print('label: %d' % label[j])
#                     plt.imshow(img[j, :, :, :])
#                     plt.show()
#                 i += 1
#         except tf.errors.OutOfRangeError:
#             print('done!')
#         finally:
#             coord.request_stop()
#         coord.join(threads)