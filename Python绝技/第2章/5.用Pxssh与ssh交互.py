#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author    :iqiqiya
# @Blog      :iqiqiya.com
# @Time      :2020/6/10
# @FileName  :5.用Pxssh与ssh交互.py
from pexpect import pxssh


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before


def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print '[-] Error Connecting'
        exit(0)


def main():
    s = connect('192.168.2.123', 'root', 'toor')
    send_command(s, 'cat /etc/shadow | grep root')


if __name__ == '__main__':
    main()