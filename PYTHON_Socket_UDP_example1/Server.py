#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import socket

if __name__ == '__main__':

    # 开始通信 SOCK_DGRAM指定了这个Socket的类型是UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口:
    s.bind(('127.0.0.1', 9999))

    print 'Bind UDP on 9999...'

    #接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
    # 一个循环表示一次开关门
    while True:
        print 'Waiting for client'
        # 接收数据:
        data_start, addr = s.recvfrom(1024)

        # 接收信息(需要等待),收到信息才可以进行下一步.
        if data_start == 'start':
            #              #
            # 启动算法，init #
            #              #
            print '--- Received from %s:%s.' % addr, 'start service ! ---'
            print '                 --- init algorithms ---'
        else:
            print 'received:',data_start
            continue

        # 发送信息(不需要等待)
        s.sendto('server started', addr)

        loopcount=0
        #每个循环表示定期发送 种类和数量
        while True:
            # todo：此处应该是非阻塞的循环
            data, addr = s.recvfrom(1024)
            print 'Received "',data,'" from %s:%s.' % addr

            if data == 'exit' or not data:
                print 'door closed! ,break'
                s.sendto('server closed',addr)
                break

            #         #
            # 发送sku  #
            #         #
            s.sendto('sku id: ... , sku num: ...', addr)
            time.sleep(0.1)
            #         #
            # 发送sku  #
            #         #

            # if data == 'exit' or not data:
            #     break


            print '第 ',loopcount,' 次'
            loopcount+=1

        #向Client_door_open发送'server closed',表示关门。进入下一循环
        data, addr = s.recvfrom(1024)
        s.sendto('server closed', addr)








