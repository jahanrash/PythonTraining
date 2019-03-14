import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
print("#####################################")
print("digits.data ", digits.data)
print("#####################################")
print("digits.target ", digits.target)
print("#####################################")
print("digits.image[0] ", digits.images[0])
print("#####################################")
print("lenght of digits ", len(digits.data))
print("#####################################")

print("#####################################")
print("Fitting the model")

clf = svm.SVC(gamma=0.0001, C=100)
X,y = digits.data[:-10], digits.target[:-10]
clf.fit(X,y)

print("#####################################")
print("Prediction: ", clf.predict(digits.data)[-4])
plt.imshow(digits.images[-6], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
print("#####################################")