import multiprocessing

p = multiprocessing.Process(target=FUNCTION_NAME, args=(ARG,...), name=PROCESS_NAME)
p.start()
multiprocessing.current_process()
p.daemon = True
p.pid
p.name

p.join()
p.join(SECONDS) # 超时期限，期限内未完成也会返回
p.is_alive()
p.terminate()
p.exitcode # 产生异常的进程，会自动得到exitcode为1
p.log_to_stderr(logging.DEBUG) # log

logger = p.get_logger()
logger.setLevel(logging.INFO)


queue = multiprocessing.Queue()
queue.put(obj)
obj = queue.get()
obj.do_something()
obj.close()
obj.join_thread()

condition = multiprocessing.Condition()
cond.notifiy_all()
cond.wait()
