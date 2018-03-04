# -*- coding:utf-8 -*-
__author__ = 'ttoyblock'
import os

# -- app config --
DEBUG = True

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    PROJECT_DIR = PROJECT_DIR[:PROJECT_DIR.rindex('/')+1]
except Exception, e:
    print "[warning] %s" % e

# -- tensor config --
MOD_DIR = PROJECT_DIR + 'mod/'
LOG_DIR = PROJECT_DIR + 'log/'

TRAIN_DIR = PROJECT_DIR + 'train/'
TEST_DIR = PROJECT_DIR + 'test/'
IMGS_DIR = PROJECT_DIR + 'images/'


IMAGE_LOADER_TENSORFLOW = "tensorflow"
IMAGE_LOADER_YAHOO = "yahoo"