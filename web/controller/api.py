# -*- coding:utf-8 -*-
import json
from flask import request
from frame.utils import random_string
from web.model.test import check
from web import app

@app.route('/api/version')
def api_version():
    return '0.0.0'


@app.route('/api/health')
def api_health():
    return 'ok'

@app.route("/api/test", methods=["POST",])
def api_create_tmpgraph():
    d = request.data
    jdata = json.loads(d)
    urls = jdata.get("urls") or []
    # result = check(urls[0])
    result = {"url1": {0:0.0, 1:0.2}, 
            "url2":{0:0.0, 1:0.2}}

    ret = {
        "ok": False,
        "data": result,
    }

    if len(result) != 0:
        ret['ok'] = True
    return json.dumps(ret)