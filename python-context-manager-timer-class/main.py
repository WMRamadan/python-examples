import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = time.time()


with Timer() as timer:
    for i in range(100000000):
        x = 1000*i

print("total time taken:", timer())

