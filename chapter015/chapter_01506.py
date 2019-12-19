import socket


# 客户端函数：TCP
def client_udp():
    BUFSIZE = 1024
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg = input(">> ").strip()
        ip_port = ('127.0.0.1', 9999)
        client.sendto(msg.encode('utf-8'), ip_port)

        data, server_addr = client.recvfrom(BUFSIZE)
        print('客户端 Recvfrom：', data, server_addr)

    client.close()


# 主函数
if __name__ == '__main__':
    client_udp()
