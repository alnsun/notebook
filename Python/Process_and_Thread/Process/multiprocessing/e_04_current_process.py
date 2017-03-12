import multiprocessing
import time

def worker():
    name = multiprocessing.current_process().name
    print name, 'Starting'
    time.sleep(2)
    print name, 'Exiting'

def my_service():
    name = multiprocessing.current_process().name
    print name, 'Starting'
    time.sleep(3)
    print name, 'Exiting'

if __name__ == '__main__':
    s = multiprocessing.Process(name='my_service',
            target=my_service)
    w1 = multiprocessing.Process(name='worker 1',
            target=worker)
    w2 = multiprocessing.Process(target=worker)

    w1.start()
    w2.start()
    s.start()
