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