#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author    :iqiqiya
# @Blog      :iqiqiya.com
# @Time      :2020/6/6
# @FileName  :4.判断文件状态.py
import sys
import os
if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print '[-] ' + filename + ' does not exist.'
    if not os.access(filename, os.R_OK):
        print '[-] ' + filename + ' access denied.'
        exit(0)
    print '[+] Reading Vulnerabilities From: ' + filename