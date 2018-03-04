# -*- coding:utf-8 -*-
import json
from flask import request
# from web.yahoo.classify_nsfw import check_images
from web.sc.check import sc_check
from web import app


@app.route('/api/version')
def api_version():
    return '0.0.0'


@app.route('/api/health')
def api_health():
    return 'ok'


@app.route("/api/test", methods=["POST",])
def api_create_tmpgraph():
    d = request.get_data()
    jdata = json.loads(d)

    urls = jdata.get("urls") or []
    se_result = sc_check(urls)
    # result = {"url1": {"se": 0.0, "ad": 0.2}, 
    #     "url2": {"se": 0.0, "ad": 0.2}}

    ret = {
        "ok": False,
        "data": se_result,
    }

    if len(se_result) != 0:
        ret['ok'] = True
    return json.dumps(ret)
