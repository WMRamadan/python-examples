from timer import start_time, stop_time
from random import sample

from sorting import insertion_sort, bubble_sort, merge_sort, quick_sort


def benchmark(func):

	n = [10, 100, 1000, 10000]

	for i in n:
		unsorted = sample(range(0, i), i)
		start_time()
		func(unsorted)
		print ("{} => ({}) => {}".format(func.__name__, i, stop_time()))

if __name__ == "__main__":
	benchmark(insertion_sort)

	benchmark(bubble_sort)

	benchmark(merge_sort)

	benchmark(quick_sort)
