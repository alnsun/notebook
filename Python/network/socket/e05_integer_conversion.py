# coding: utf-8
"""
低层网络应用，有时或许需要处理通过电缆在两台设备之间传送低层数据。
在这种操作中，需要把主机操作系统发出的数据转换成网络格式，或者做逆向转换，
因为这两种数据的表示方式不一样。
"""
import socket

def convert_integer():
    data = 1234
    # 32-bit
    print 'Original: %s => Long host byte order: %s, Network byte order: %s' \
            % (data, socket.ntohl(data), socket.htonl(data))
    # 16-bit
    print 'Original: %s => Short host byte order: %s, Network byte order: %s' \
            % (data, socket.ntohs(data), socket.htons(data))


if __name__ == '__main__':
    convert_integer()
