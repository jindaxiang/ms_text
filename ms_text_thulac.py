# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
Date: 2022/1/15 17:00
Desc: THULAC 演示
https://github.com/thunlp/THULAC-Python
https://pypi.org/project/thulac/
"""
import thulac

# 对源码做修改：C:\Anaconda3\envs\ms_text\Lib\site-packages\thulac\character\CBTaggingDecoder.py
thu1 = thulac.thulac()  # 默认模式
text = thu1.cut("我爱北京天安门", text=True)  # 进行一句话分词
print(text)
