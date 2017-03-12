# coding: utf-8
import multiprocessing

def worker(num):
    """process worker function"""
    print 'Worker:', num
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,)) #与threading不同，参数必须能够使用pickle序列化
        jobs.append(p)
        p.start()
