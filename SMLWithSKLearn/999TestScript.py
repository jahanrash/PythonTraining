import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
from sklearn import svm

x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

plt.scatter(x,y)
plt.show()

X = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11]])

y = [0,1,0,1,0,1]

clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)

test = np.array([0.58, 0.76])
print(test)       # Produces: [ 0.58  0.76]
print(test.shape) # Produces: (2,) meaning 2 rows, 1 col

test = test.reshape(1, -1)
print(test)       # Produces: [[ 0.58  0.76]]
print(test.shape) # Produces (1, 2) meaning 1 row, 2 cols

print(clf.predict(test)) # Produces [0], as expected