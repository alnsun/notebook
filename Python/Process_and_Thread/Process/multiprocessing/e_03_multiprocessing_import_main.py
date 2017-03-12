# coding: utf-8
""" 可导入的目标函数 """
import multiprocessing
import multiprocessing_import_worker


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(
                target=multiprocessing_import_worker.worker)
        jobs.append(p)
        p.start()

