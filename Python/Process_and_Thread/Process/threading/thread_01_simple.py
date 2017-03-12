import threading


def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker) # Thread object
    threads.append(t)
    t.start() # start thread instance
