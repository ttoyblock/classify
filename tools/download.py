# -*- coding: utf-8 -*-

import urllib2

from frame import config


def deal_images(urls):
    files = {}
    for url in urls:
        response = urllib2.urlopen(url)
        img = response.read()

        file = config.IMGS_DIR + url.split('/')[3]+'.jpg'
        files[url] = file
        with open(file, 'wb') as f:
            f.write(img)
    return files
