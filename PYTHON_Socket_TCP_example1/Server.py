#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import socket

if __name__ == '__main__':

    # 开始通信
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    s.bind(('127.0.0.1', 9999))

    s.listen(5)
    print 'Waiting for connection...'

    #接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
    # 一个循环表示一次开关门
    while True:
        # 接受一个新连接，表示开门，如果没有接收到则一直停留在这一行
        sock, addr = s.accept()
        # 处理TCP连接:
        print 'Accept new connection from %s:%s...' % addr

        # 发送信息(不需要等待)
        sock.send('recognition started!')
        # 接收信息(需要等待),收到信息才可以进行下一步.
        data_start = sock.recv(1024)
        if data_start == 'start':
            #              #
            # 启动算法，init #
            #              #
            print 'init algorithms'
            iiii=0
        else:
            print data_start

        loopcount=0
        #每个循环表示定期发送 种类和数量
        while True:
            data = sock.recv(1024)
            if data == 'exit' or not data:
                print 'break'
                break

            #         #
            # 发送状态 #
            #         #

            sock.send('sku id: ... , sku num: ...')
            time.sleep(0.1)
            #         #
            # 发送状态 #
            #         #

            # if data == 'exit' or not data:
            #     break


            print '发送 ',loopcount
            loopcount+=1

        #关闭连接，表示关门。进入下一循环
        sock.close()
        print 'Connection from %s:%s closed.' % addr







