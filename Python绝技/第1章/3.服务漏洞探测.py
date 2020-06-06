#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author    :iqiqiya
# @Blog      :77sec.cn
# @Time      :2020/6/5
# @FileName  :3.服务漏洞探测.py
# 获取banner与文本内容比较
import socket
import sys

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout (2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

# 固定文件名
def checkVulns(banner):
    f = open("vuln_banners.txt", 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+] Server is vulnerable: " + banner.strip('\n')

# 文件名作为命令行参数传入
def checkVulns2(banner):
    filename = sys.argv[1]
    print "[+] Reading Vulnerabilities From: " + filename
    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+] Server is vulnerable: " + banner.strip('\n')


def main():
    portList = [21, 22, 25, 80, 110, 443]
    for x in range(1, 255):
        ip = '192.168.0.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print'[+]' + ip + ': ' + banner
                checkVulns(banner)


if __name__ == '__main__':
    main()