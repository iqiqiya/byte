#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author    :iqiqiya
# @Blog      :77sec.cn
# @Time      :2020/6/5
# @FileName  :图片批量下载.py
import urllib


# https://live.freebuf.com/activity/eb981fa6807c1211d0728dd54728225a/l_aea3958ff2d31b22506e6f78166c8147
url = "https://cnstatic01.e.vhall.com/document/539fa66100c9d36a0b811b6b63443c5d/"
num = 1
for x in range(500):
    picUrl = url + str(x) + '.jpg'
    pic = urllib.urlopen(picUrl)  # 打开图片网址
    picData = pic.read()  # 读取图片数据
    picFile = open('pic-' + str(num) + '.jpg', 'wb')  # 打开本地图片文件
    picFile.write(picData)  # 写入图片数据
    picFile.close()  # 关闭文件
    num += 1