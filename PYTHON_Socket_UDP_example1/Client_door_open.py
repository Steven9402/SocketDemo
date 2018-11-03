# -*- coding: UTF-8 -*-
import socket

server_started=False

#发送开门信号 ‘starts’
s_for_openthedoor=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_for_openthedoor.sendto('start',('127.0.0.1',9999))
data=s_for_openthedoor.recv(1024)
if data=='server started':
    server_started=True
    print 'Server has not started!'
else:
    print 'Server has not started, please resend signal!'
s_for_openthedoor.close()


# 如果上面的程序接收到了'hello',则开始取数据
# 如果取到的数据是'server closed',则结束循环,关闭socket
s_for_fetch_sku = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if server_started==True:
    while True:
        s_for_fetch_sku.sendto('fetch',('127.0.0.1',9999))
        data=s_for_fetch_sku.recv(1024)

        if data[0:3]=='sku':
            print data
        else:
            print '..',data

        if data == 'server closed':
            print 'server has closed, exit loop!'
            break
s_for_fetch_sku.close()
print 'close'

