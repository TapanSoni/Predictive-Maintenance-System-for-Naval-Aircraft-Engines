import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# need to field from the csv file.
# need fields for classification algorithm

# test array 1 represent the training data

# take CSV not functional
# T.get_param([CSV])

X = np.array([[0], [1], [2], [3], [4], [5], [6], [8], [9]])
# test array 2 represents the tags
y = np.array([1, 1, 0, 0, 1, 0, 0, 1, 1])
# test validation set
v = np.array([[2, 1], [3, 0], [5, 1], [6, 1], [9, 0], [5, 1], [4, 0]])
# classifier
clf = KNeighborsClassifier(n_neighbors=9)
# training classifier with both arrays

# weighted desired score
dscore = [.7, [9]]

# fits sample data sets to classifier
clf.fit(X, y)

# sample prediction
print(clf.predict([[2]]))

print(clf.predict_proba([[0.5]]))
# not working scoring
# print(clf.score(X,y,[dscore]));
