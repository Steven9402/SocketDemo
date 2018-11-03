# -*- coding: UTF-8 -*-
import socket

# 发送关门信号
s_for_closethedoor=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_for_closethedoor.sendto('exit',('127.0.0.1',9999))
data=s_for_closethedoor.recv(1024)
print data
s_for_closethedoor.close()


