from time import time

mark = 0


def start_time():
    global mark
    mark = time()


def stop_time():
    global mark
    elapsed_time = time() - mark
    return elapsed_time
