#! /usr/bin/env python
# -*- coding: utf-8 -*-


import zipfile
import argparse
from threading import Thread


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print("[+] Password = " + bytes.decode(password) + "\n")
        return password
    except Exception as e:
        return


def main(file, pwd):
    zFile = zipfile.ZipFile(file)
    passFile = open(pwd)

    for line in passFile.readlines():
        password = line.strip('\n')
        password = bytes(password, encoding="utf8")
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.description = "Unzip file use password lists!"
    parser.add_argument("-f", "--file", required=True, help="input zip file name")
    parser.add_argument("-p", "--password", required=True, help="input zip password list file")
    args = parser.parse_args()

    main(args.file, args.password)
