import numpy as np

a = np.array([5, 6, 9])
print(a[0])

print(a[1])
print(a.size)
print(a.shape)


a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.int32)
print(a)
print(a.ndim)
print(a.itemsize)
print(a.dtype)


a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)
print(a)
print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a.shape)


a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.complex64)

b =  np.zeros((3, 5))
print(b)

c =  np.ones((3, 5))
print(c)

l = range(5)
print(l[2])

m = range(0, 5)
print(m[3])


d = np.arange(1, 5)
print(d)

e = np.linspace(1, 5, 10)
print(e)

a.reshape(2,3)
print(a)

print(a.sum())

print(a.min())

print(a.max())

print(a.sum(axis=1))

print(np.sqrt(a))

print(np.std(a))

i = np.array([[1, 2], [3, 4]])
j = np.array([[5, 6], [7, 8]])

print(i+j)

print(i*j)

print(j-i)

print(j/i)