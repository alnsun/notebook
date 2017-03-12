import threading

thread_object = threading.Thread(name=THREAD_NAME, target=FUNCTION_NAME, args=(FUNC_ARGS1,...))
thread_object.start()
thread_object.setDaemon()
thread_object.join()
thread_object.isAlive()
thread_object.currentThread()
threading.enumerate()

class MyThread(threading.Thread):
    def run(self):
        # do something
        pass

threading.Timer(SECONDS, FUNC)
thread_object.cancel()


e = threading.Event()
e.wait() # block, wait Event object set
e.wait(SECONDS)
e.isSet()
e.set()


lock = threading.Lock()
lock.acquire()
lock.release()

