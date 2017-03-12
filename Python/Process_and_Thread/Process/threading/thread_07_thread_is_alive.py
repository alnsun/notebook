# coding: utf-8
import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG,
        format='[%(levelname)s (%(threadName)-10s) %(message)s')

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True) # set thread to daemon

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(1) # 默认join会无限阻塞，指定时间（秒）后，时间段内未完成，join()也会返回
# 传入的时间小于睡眠时间，所以join()返回后这个线程仍然“存活”
print 'd.isAlive()', d.isAlive()
