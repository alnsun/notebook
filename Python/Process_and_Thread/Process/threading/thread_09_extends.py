import threading
import logging

logging.basicConfig(level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s')

class MyThread(threading.Thread):
    """
    """
    def run(self):
        logging.debug('running')
        return

for i in range(5):
    t = MyThread()
    t.start()
