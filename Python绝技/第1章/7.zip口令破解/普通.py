#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author    :iqiqiya
# @Blog      :iqiqiya.com
# @Time      :2020/6/9
# @FileName  :普通.py
import zipfile


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except:
        return


def main():
    zFile = zipfile.ZipFile('flag.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zFile, password)
        if guess:
            print '[+] Password = ' + password + '\n'
            exit(0)


if __name__ == '__main__':
    main()