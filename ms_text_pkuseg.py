# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
Date: 2022/1/15 17:00
Desc: PKUSEG 演示
https://github.com/lancopku/pkuseg-python
https://pypi.org/project/pkuseg/
"""
import pkuseg

seg = pkuseg.pkuseg()           # 以默认配置加载模型
text = seg.cut('我爱北京天安门')  # 进行分词
print(text)

# 细分领域
# 模型目录：C:\Users\king\.pkuseg
seg = pkuseg.pkuseg(model_name='web')  # 程序会自动下载所对应的细分领域模型
text = seg.cut('房子退租，摄影器材送人，东西打包寄回家，遗书设置微博定时发送，然后独自走向大海，他已经努力做到不给任何人添麻烦了[单身狗]真的是很善良很柔软的一个人')              # 进行分词
print(text)
