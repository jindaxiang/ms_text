# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
Date: 2022/1/15 17:02
Desc: 商业接口-百度 AI-自然语言处理
https://cloud.baidu.com/doc/NLP/s/tk6z52b9z
"""
from aip import AipNlp
from cons import APP_ID, API_KEY, SECRET_KEY

""" 你的 APPID AK SK """
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = "苹果手机的电池容量很小但是很经用"
result = client.sentimentClassify(text)
print(result)
