# -*- coding: utf-8 -*-

import urllib2

from frame import config


def deal_images(urls):
    files = {}
    for url in urls:
        # URL处理
        arr = url.split('/')
        if len(arr) == 4:
            url = url + '?imageMogr2/format/jpg/size-limit/800k!'

        response = urllib2.urlopen(url)
        img = response.read()

        file = config.IMGS_DIR + arr[3]+'.jpg'
        files[url] = file
        with open(file, 'wb') as f:
            f.write(img)
    return files
