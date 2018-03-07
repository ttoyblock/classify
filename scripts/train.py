# -*- coding: utf-8 -*-
import os
import time

import numpy as np
import tensorflow as tf
from model import inference, losses, trainning, evaluation
from img import get_files, get_batch

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = PROJECT_DIR[:PROJECT_DIR.rindex('/')+1]

# 要分类的类别数，这里是3分类
N_CLASSES = 3
# 设置图片的size
IMG_W = 208
IMG_H = 208
BATCH_SIZE = 8
CAPACITY = 64
# 迭代一千次，如果机器配置好的话，建议至少10000次以上
MAX_STEP = 1000
# 学习率
learning_rate = 0.0001

TRAIN_DIR = PROJECT_DIR + 'train/'
LOG_DIR = PROJECT_DIR + 'log/'
MODEL_PATH = PROJECT_DIR + "mod/sc/model.ckpt"


def run_training():
    train, train_label = get_files(TRAIN_DIR)
    train_batch, train_label_batch = get_batch(train, train_label,
                                                        IMG_W,
                                                        IMG_H,
                                                        BATCH_SIZE,
                                                        CAPACITY)
    train_logits = inference(train_batch, BATCH_SIZE, N_CLASSES)
    train_loss = losses(train_logits, train_label_batch)
    train_op = trainning(train_loss, learning_rate)
    train_acc = evaluation(train_logits, train_label_batch)

    summary_op = tf.summary.merge_all()
    sess = tf.Session()
    train_writer = tf.summary.FileWriter(LOG_DIR, sess.graph)
    saver = tf.train.Saver()

    sess.run(tf.global_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    try:
        for step in np.arange(MAX_STEP):
            time.sleep(1)
            if coord.should_stop():
                break
            _, tra_loss, tra_acc = sess.run([train_op, train_loss, train_acc])
            if step % 50 == 0:
                print('Step %d, train loss = %.2f, train accuracy = %.2f%%' % (step, tra_loss, tra_acc))
                # 每迭代50次，打印出一次结果
                summary_str = sess.run(summary_op)
                train_writer.add_summary(summary_str, step)

            if step % 200 == 0 or (step + 1) == MAX_STEP:
                checkpoint_path = os.path.join(LOG_DIR, 'model.ckpt')
                saver.save(sess, checkpoint_path, global_step=step)
                # 每迭代200次，利用saver.save()保存一次模型文件，以便测试的时候使用

    except tf.errors.OutOfRangeError:
        print('Done training epoch limit reached')
    finally:
        coord.request_stop()

    coord.join(threads)

    # save model
    saver = tf.train.Saver()
    model_path = MODEL_PATH
    save_path = saver.save(sess, model_path)
    print save_path
    sess.close()


if __name__ == '__main__':
    print 'start training......'
    run_training()
