#!/usr/bin/python3
# -*-coding:utf-8 -*-
# 时间同步程序：服务器端
from socket import *
from time import ctime


# 客户端函数：TCP
def client_tcp():
    HOST = '127.0.0.1'  # 服务端ip
    PORT = 21566        # 服务端端口号
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)   # 创建socket对象
    tcpCliSock.connect(ADDR)    # 连接服务器
    while True:
        data = input('>>').strip()
        if not data:
            break
        tcpCliSock.send(data.encode('utf-8'))   # 发送消息
        data = tcpCliSock.recv(BUFSIZ)          # 读取消息
        if not data:
            break
        print(data.decode('utf-8'))
    tcpCliSock.close()                          # 关闭客户端


# 主函数
if __name__ == '__main__':
    client_tcp()