# -*- coding:utf-8 -*-
__author__ = 'ttoyblock'


def required_chk(p):
    if not p:
        return ''

    for k in p:
        if not p[k]:
            return 'parameter %s is blank' % k
