import numpy as np



a = np.arange(6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)

print(a)
print(b)

print(np.vstack((a,b)))

print(np.hstack((a,b)))



c = np.arange(30).reshape(2, 15)
result = np.hsplit(c, 3)
print(result[0])
print(result[1])
print(result[2])


# d = np.arange(30).reshape(2, 15)
# result = np.vsplit(d, 2)
# print(result[0])
# print(result[1])
# print(result[2])


m = np.arange(12).reshape(3, 4)
n = m > 4
print(n)

print(m[n])

m[n] = -1

print(m)