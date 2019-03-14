import numpy as np


a = np.arange(12).reshape(3, 4)
print(a)
print("--------------------------")
for row in a:
    print(row)

print("--------------------------")
for row in a:
    for cell in row:
        print(cell)
print("--------------------------")


for cell in a.flatten():
    print(cell)
print("--------------------------")

for x in np.nditer(a, order='C'):
    print(x)

print("--------------------------")

for x in np.nditer(a, order='F'):
    print(x)

print("--------------------------")

for x in np.nditer(a, order='F', flags=['external_loop']):
    print(x)

# print("--------------------------")
#
# for x in np.nditer(a, flags=['readwrite']):
#     x[...] = x * x
#
# print(a)

print("--------------------------")
c = np.arange(3, 15, 4).reshape(3, 1)
print(c)
for x,y in np.nditer([a,c]):
    print(x,y)

