# -*- coding:utf-8 -*-
__author__ = 'ttoyblock'

# -- app config --
DEBUG = True

# -- tensor config --
MOD_DIR = ""
LOG_DIR = ""

TRAIN_DIR = ""
TEST_DIR = ""

try:
    from frame.local_config import *
except Exception, e:
    print "[warning] %s" % e
