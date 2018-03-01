# -*- coding:utf-8 -*-
from .bean import Bean


class Alert(Bean):
    _tbl = 'alert'
    _cols = 'id, path, content'

    def __init__(self, _id, path, content):
        self.id = _id
        self.path = path
        self.content = content

