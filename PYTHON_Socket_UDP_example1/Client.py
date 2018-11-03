#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import socket
import time

opendoorcount=0
#每次循环表示一次开门时间
while True:
    print '第',opendoorcount,'次开门'
    opendoorcount+=1

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 发送一次start信号，注意可能收不到
    s.sendto('start', ('127.0.0.1', 9999))
    # 发送开始信号,发送一定要有sleep时间间隔
    time.sleep(0.1)

    # 如果循环超过5次，表示关门
    # 如何触发关门事件，需要重新定义，使用python多线程通信？
    loopcount=0
    while loopcount<5:
        # 每隔 0.01接收一次信号,即服务器发送的sku
        # 如果收到,则进入下一个0.01秒,否则卡在这里！
        # 0.01 秒这个时间间隔由服务器定义
        s.sendto('request', ('127.0.0.1', 9999))
        time.sleep(0.1)
        print s.recv(1024)

        loopcount+=1

    s.sendto('exit', ('127.0.0.1', 9999))
    s.close()
