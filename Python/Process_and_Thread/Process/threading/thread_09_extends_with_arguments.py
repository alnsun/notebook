import threading
import logging

logging.basicConfig(level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s')

class MyThreadWithArgs(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
            args=(), kwargs=None, verbose=None): # added args and kwargs
        threading.Thread.__init__(self, group=group, # default init function
                target=target,
                name=name,
                verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('running with %s naem %s',
                self.args, self.kwargs)
        return

for i in range(5):
    t = MyThreadWithArgs(args=(i,),
            kwargs={'a':'A', 'b':'B'})
    t.start()
