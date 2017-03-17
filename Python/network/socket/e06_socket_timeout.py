# coding: utf-8
"""
创建套接字实例，调用方法设置或者获取超时时间
"""
import socket

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Default socket timeout: %s' % s.gettimeout()
    s.settimeout(100)
    print 'Current socket timeout: %s' % s.gettimeout()


if __name__ == '__main__':
    test_socket_timeout()

