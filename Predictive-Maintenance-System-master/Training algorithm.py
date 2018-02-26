#version 1.0

#install numpy, scipy, scikit to workspace

import sklearn;
import numpy;
from sklearn import svm;
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis;

#need to field from the csv file.
# need fields for clasifcation algorithm

#test array 1 represent the training data

#take CSV not functional
#T.get_param([CSV])

X = np.array([[0], [1], [2], [3],[4],[5],[6],[8],[9]]);
#test array 2 represents the tags
y = np.array([1,1,0,0,1,0,0,1,1]);
#test valdation set
v= np.array([[2,1],[3,0],[5,1],[6,1],[9,0],[5,1],[4,0]]);
#classifier
clf = KNeighborsClassifier(n_neighbors=9);
#training classfier with both arrays

#weighted desired score
dscore =[.7,[9]];

#fits sample data sets to classifier
clf.fit(X, y);

#sample prediction, results not always as predicated
print(clf.predict([[2.5]]))

print(clf.predict_proba([[0.5]]))
#not working scoring
#print(clf.score(X,y,[dscore]));