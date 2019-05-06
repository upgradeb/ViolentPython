#! /usr/bin/env python
# -*- coding: utf-8 -*-


import zipfile


def extractFile(zFile, password):
    try:
        # zFile.extractall(pwd=b"apple")
        # print("[*] Password = " + bytes.decode(password) + "\n")
        zFile.extractall(pwd=password)
        # print("[+] Password = " + bytes.decode(password) + "\n")
        return password
    except Exception as e:
        return
        # print("[*] Password = " + bytes.decode(password) + "\n")
        # pass
        # print(e)


def main():
    zFile = zipfile.ZipFile("evil.zip")
    passFile = open('key.txt')

    for line in passFile.readlines():
        password = line.strip('\n')
        password = bytes(password, encoding="utf8")
        guess = extractFile(zFile,password)
        if guess:
            print("[+] Password = " + bytes.decode(password) + "\n")


if __name__ == '__main__':
    main()
