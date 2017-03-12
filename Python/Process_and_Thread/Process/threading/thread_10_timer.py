# coding: utf-8
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s')

def delayed():
    logging.debug('worker running')
    return

t1 = threading.Timer(3, delayed) # 在指定延时之后开始工作
t1.setName('t1')
t2 = threading.Timer(3, delayed)
t1.setName('t2')

logging.debug('starting timers')
t1.start()
t2.start()

logging.debug('waiting before canceling %s', t2.getName())
time.sleep(2)
logging.debug('canceling %s', t2.getName())
t2.cancel() # 可在延迟期内任意时刻取消
logging.debug('done')
