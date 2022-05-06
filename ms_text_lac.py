# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
Date: 2022/1/15 16:47
Desc: LAC 演示
https://github.com/baidu/lac
https://pypi.org/project/LAC/
https://mp.weixin.qq.com/s/ePYwprZd4NbvGkdtOgrI7w
"""
from LAC import LAC

# 装载分词模型
lac = LAC(mode='seg')

# 单个样本输入，输入为Unicode编码的字符串
text = "LAC是个优秀的分词工具"
seg_result = lac.run(text)

# 批量样本输入, 输入为多个句子组成的list，平均速率会更快
texts = ["LAC是个优秀的分词工具", "百度是一家高科技公司"]
seg_result = lac.run(texts)
