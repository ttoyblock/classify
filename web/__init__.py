# -*- coding:utf-8 -*-
__author__ = 'ttoyblock'

import logging
from flask import Flask

# -- create app --
app = Flask(__name__)
app.config.from_object("frame.config")

# config log
log_formatter = '%(asctime)s\t[%(filename)s:%(lineno)d] [%(levelname)s: %(message)s]'
log_level = logging.DEBUG if app.config['DEBUG'] else logging.WARNING
logging.basicConfig(format=log_formatter, datefmt="%Y-%m-%d %H:%M:%S", level=log_level)


@app.before_request
def before_request():
    pass


@app.route('/')
def hello_world():
    return 'Hello World!'

from web.controller import api