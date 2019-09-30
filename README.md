## 我的环境

- MAC IOS 系统
- python 2.7.4
- docker

### 运行于 CLI

## 1.开发环境准备
#### 参考 https://cloud.tencent.com/document/product/583/37510

## 2.配置 SCF CLI
- cf configure set --region ap-shanghai --appid [appid] --secret-id  [secret-id] --secret-key [secret-key]
- 核实配置:
~~~
(tencent) ➜  duty_scheduler scf configure get
[>] USER_1
[>] appid = 12570***
[>] region = ap-shanghai
[>] secret-id = ********************************l3Th
[>] secret-key = ****************************YzA6
[>] using-cos = False (By default, it isn't deployed by COS.)
[>] python2-path = None
[>] python3-path = None
[>] no-color = False
(tencent) ➜  duty_sche
~~~
- 访问控制
https://console.cloud.tencent.com/cam/overview

## 3.编写函数
- scf init --runtime python2.7 --name duty_scheduler --output-dir ./
- 编写你的代码逻辑 

## 4.本地测试
- scf native generate-event cos post | scf native invoke

## 5.发布函数并确认
- scf deploy
- scf function list
- web端确认 https://console.cloud.tencent.com/scf/list?rid=4&ns=default

## 6.云函数控制台 设置定时任务
- https://console.cloud.tencent.com/scf/index?rid=4
- 函数服务> 选项上传的函数> 触发方式> 定时触发> 编写CRON
- cron 配置参考 https://cloud.tencent.com/document/product/583/9708#cron-.E8.A1.A8.E8.BE.BE.E5.BC.8F


### Python API  参考

- https://cloud.tencent.com/document/product/583/11061


### 机器人 请求配置 参考

- https://work.weixin.qq.com/help?doc_id=13376&helpType=undefined
- curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=acd8cabe-xxx-xxx' -H 'Content-Type: application/json' -d '{"msgtype":"text","text":{"content":"hello world"}}'
- message example:
~~~ 

{
    "msgtype": "text",
    "text": {
        "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
        "mentioned_list":["wangqing","@all"],
        "mentioned_mobile_list":["13800001111","@all"]
    }
}
~~~

### 参考链接
- https://cloud.tencent.com/developer/article/1452633?s=original-sharing


