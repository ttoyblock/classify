classify: 图片分类器


## Install dependency

    # yum install -y python-virtualenv

    ...

    $ cd path to classify/
    $ virtualenv ./env

    # use douban pypi
    $ ./env/bin/pip install -r pip_requirements.txt -i http://pypi.douban.com/simple


## Start

    $ ./env/bin/python wsgi.py


## Run with gunicorn

    $ . env/bin/activate
    $ ./control start
    

## Test
    # curl -d '{}' '127.0.0.1:8888/api/test'


## 训练脚本使用 ---------
    1  run run.sh 初始化相关目录 
    train/0/  第一类图片
    train/1/  第二类图片
    train/2/  第三类图片
    log/      训练日志

    2  倒入图片

    3  run train.py 开始训练

    4  训练完成 运行：

    #  tensorboard --logdir=./log

    goto: 127.0.0.1:6006 查看训练结果 评价模型

    5  run test.py 测试一张图片