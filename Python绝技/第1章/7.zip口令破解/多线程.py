#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author    :iqiqiya
# @Blog      :iqiqiya.com
# @Time      :2020/6/9
# @FileName  :多线程.py
import zipfile
from threading import Thread


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found Password ' + password + '\n'
    except:
        pass


def main():
    zFile = zipfile.ZipFile('flag.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()