import numpy as np
import time
import sys

# l = range(1000)
# print(sys.getsizeof(5) * len(l))
#
# array = np.arange(1000)
# print(array.size * array.itemsize)

size = 1000000

l1 = range(size)
l2 = range(size)


a1 = np.array(size)
a2 = np.array(size)

# python list
start = time.time()
result = [(x+y) for x,y in zip(l1, l2)]
print("Pythong list took: ", (time.time()-start)* 1000)

#numpy array
start = time.time()
result = a1 + a2
print("Numpy took: ", (time.time()-start)*1000)


a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print(a1+a2)

print(a2-a1)

print(a1*a2)

print(a2/a1)
