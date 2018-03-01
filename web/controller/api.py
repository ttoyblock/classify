# -*- coding:utf-8 -*-
import json
from flask import request
from web import app
from frame.utils import random_string
from web.model.alert import Alert
from web.model.test import test


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
    result = test(urls)

    ret = {
        "ok": False,
        "id": id_,
    }

    if id_:
        ret['ok'] = True
        return json.dumps(ret)
    else:
        return json.dumps(ret)