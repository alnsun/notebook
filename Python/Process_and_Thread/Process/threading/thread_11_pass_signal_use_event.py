# coding: utf-8
"""
多个线程间进行同步操作
Event可实现线程间安全通信。Event管理一个内部标志，调用时可用set()或者clear()控制这个标志。
其它线程可以使用wait()暂停，直到设置这个标志
"""
import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s')


def wait_for_event(e):
    """wait for the event to be set before doing anything"""
    logging.debug('waite_for_event starting')
    event_is_set = e.wait() # 阻塞
    logging.debug('event set: %s', event_is_set)

def wait_for_event_timeout(e, t):
    """wait t seconds and then timeout"""
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t) # 超时之前等待的秒数
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')

e = threading.Event()
t1 = threading.Thread(name='block',
        target=wait_for_event,
        args=(e,))
t1.start()

t2 = threading.Thread(name='noneblock',
        target=wait_for_event_timeout,
        args=(e, 2))
t2.start()
logging.debug('Waiting before calling Event.set()')
time.sleep(3)
e.set()
logging.debug('Event is set')
