classify: 图片分类器

## Install dependency

    # yum install -y python-virtualenv

    $ cd /home/work/open-falcon/links/
    $ virtualenv ./env

    # use douban pypi
    $ ./env/bin/pip install -r pip_requirements.txt -i http://pypi.douban.com/simple


## Start

    $ ./env/bin/python wsgi.py

    --> goto http://127.0.0.1:5090


## Run with gunicorn

    $ . env/bin/activate
    $ bash run.sh
    
    --> goto http://127.0.0.1:5090

