import threading
import logging

logging.basicConfig(level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s')

class MyThreadWithArgs(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.args = args,
        self.kwargs = kwargs
        return super(MyThreadWithArgs, self).__init__(*args, **kwargs)

    def run(self):
        logging.debug('running with %s name %s',
                self.args, self.kwargs)
        return

for i in range(5):
    t = MyThreadWithArgs(args=(i,),
            kwargs={'a':'A', 'b':'B'})
    t.start()
