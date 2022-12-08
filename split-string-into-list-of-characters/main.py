import timeit
from itertools import chain

string = "thisisthestringthatwewanttosplitintoalist"

def getCharList(str):
  return list(str)

def getCharListComp(str):
  return [char for char in str]

def getCharListMap(str):
  return list(map(lambda c: c, str))

def getCharListForLoop(str):
  list = []
  for c in str:
    list.append(c)

def getCharListUnpack(str):
  return [*str]

def getCharListExtend(str):
  list = []
  return list.extend(str)

def getCharListChain(str):
  return chain(str)
 
time_list = timeit.timeit(stmt='getCharList(string)', globals=globals(), number=1)
time_listcomp = timeit.timeit(stmt='getCharListComp(string)', globals=globals(), number=1)
time_listmap = timeit.timeit(stmt='getCharListMap(string)', globals=globals(), number=1)
time_listforloop = timeit.timeit(stmt='getCharListForLoop(string)', globals=globals(), number=1)
time_listunpack = timeit.timeit(stmt='getCharListUnpack(string)', globals=globals(), number=1)
time_listextend = timeit.timeit(stmt='getCharListExtend(string)', globals=globals(), number=1)
time_listchain = timeit.timeit(stmt='getCharListChain(string)', globals=globals(), number=1)

print(f"Execution time using list constructor is {time_list} seconds")
print(f"Execution time using list comprehension is {time_listcomp} seconds")
print(f"Execution time using map is {time_listmap} seconds")
print(f"Execution time using for loop is {time_listforloop} seconds")
print(f"Execution time using unpacking is {time_listunpack} seconds")
print(f"Execution time using extend is {time_listextend} seconds")
print(f"Execution time using chain is {time_listchain} seconds")
