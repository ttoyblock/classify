# -*- coding:utf-8 -*-
__author__ = 'ttoyblock'
from flask import Flask


#-- create app --
app = Flask(__name__)
app.config.from_object("frame.config")