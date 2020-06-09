#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author    :iqiqiya
# @Blog      :iqiqiya.com
# @Time      :2020/6/6
# @FileName  :6.Unix口令破解机.py
import crypt


def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print "[+] Found Password: " + word + "ln"
            return
    print "[-] Password Not Found.\n"
    return


def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*]  Cracking Password For: " + user
            testPass(cryptPass)


if __name__ == '__main__':
    main()