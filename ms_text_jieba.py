# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
Date: 2022/1/15 17:00
Desc: Jieba 演示
https://github.com/fxsjy/jieba
https://pypi.org/project/jieba/
"""
# 引入该库
import jieba
# 增加以下两行代码
# Python 版本需要在 3.8 及以下
# pip install paddlepaddle
import paddle
paddle.enable_static()

jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持

strs = ["我来到北京清华大学", "乒乓球拍卖完了", "中国科学技术大学"]
for str in strs:
    seg_list = jieba.cut(str, use_paddle=True)  # 使用paddle模式
    print("Paddle Mode: " + '/'.join(list(seg_list)))

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))
