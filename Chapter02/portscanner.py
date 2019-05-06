#! /usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
from socket import *
from threading import *


screenLock = Semaphore(value=1)

# Function connection scanner
def conn_scan(tghost, tgport):
    try:
        conn_socket = socket(AF_INET, SOCK_STREAM)
        conn_socket.connect((tghost, tgport))
        conn_socket.send(b'ViolentPython\r\n')
        results = conn_socket.recv(100)
        screenLock.acquire()
        print("[+] " + tghost + " /tcp open in port: " + tgport)
        print("[+] " + str(results))
        conn_socket.close()
    except ConnectionError as e:
        # print(e)
        # print("Connection error: " + e)
        screenLock.acquire()
        print("[-] " + tgport.__str__() + "/tcp closed.")
    finally:
        # screenLock.release()
        conn_socket.close()

def port_scan(tghost, tgports):
    try:
        tg_ip = gethostbyname(tghost)
        # print(tghost)
    except ConnectionError as e:
        print("[+] Cannot resolve " + tghost + " : Unknown host.")
        return

    # try:
    #     tg_name = gethostbyaddr(tg_ip)
    #     print("[+] Scan Results for : " + tg_name[0])
    # except ConnectionError as e:
    #     print("[+] Scan Results for :" + tg_ip)

    setdefaulttimeout(1)

    for tgport in tgports:
        # print("Scanning Port " + tgport)
        # conn_scan(tghost, int(tgport))
        t = Thread(target=conn_scan, args=(tghost, int(tgport)))
        t.start()


def main(host, port):
    tgports = str(port).split(',')
    # print(tgports)
    port_scan(host, tgports)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = "Port Scanner input Host and Ports, Go!!!"
    parser.add_argument("-H", "--host", required=True, help="Input host name")
    parser.add_argument("-P", "--port", required=True, help="Input Ports eg:21,25,80")
    args = parser.parse_args()
    # print(args.host)
    # print(args.port)

    main(args.host, args.port)
