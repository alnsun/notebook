import multiprocessing

class Worker(multiprocessing.Process):
    """
    """
    def run(self):
        print 'In %s' % self.name
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()

    for i in jobs:
        i.join()
