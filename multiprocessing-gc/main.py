import gc
import time
from multiprocessing import Process, current_process


def test():
    """Simple test function"""
    lst = []
    for i in range(100000000):
        lst.append(i)

if __name__ == '__main__':
    starttime = time.time()
    worker_count = 8
    worker_pool = []
    for _ in range(worker_count):
        p = Process(target=test, args=())
        worker_pool.append(p)
        p.start()
        worker_pool.append(p)
    for p in worker_pool:
        p.join()
        gc.collect()

    print("That took {} seconds".format(time.time() - starttime))

