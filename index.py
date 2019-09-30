# -*- coding: utf8 -*-
import urllib3
import json

MESSAGE="明天谁值班，请举手!"
WEBHOOK_URL="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=[替换你的KEY]"


def main_handler(event, context):
    http = urllib3.PoolManager()
    data = {
        "msgtype": "text",
        "text": {
            "content": MESSAGE,
            "mentioned_list":["@all"]
        }
    }
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request(
        method='POST',
        url=WEBHOOK_URL,
        body=encoded_data,
        headers={'Content-Type': 'application/json'})
    return r.status

