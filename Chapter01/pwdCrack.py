#! /usr/bin/env python
# -*- coding: utf-8 -*-

import crypt
import hashlib
import sys


def EnCrypt(word, salt):
    cryptWord = crypt.crypt(word, salt)
    print(cryptWord)
    return cryptWord


def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('key.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        # print(cryptWord)


def main():
    passFile = open('password.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password For: " + user + "\n")
            testPass(cryptPass)


if __name__ == "__main__":
    # main()
    EnCrypt('toor', '$6$SZESLPWZ')
    # EnSha512('toor', '$6$ZESLPWZ$')
