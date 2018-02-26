#install numpy, scipy, scikit to workspace

import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#imports we will use

import sklearn;
import numpy;
from sklearn import svm;
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors

#imports we probably won't use

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis;


#need to use data split


#unable to find .csv path issue probably
#test1 = open('dataSpeed1.csv',"rb")
#reader1 = csv.reader(test1)



#test array 1 represent the training data, sample
X = np.array([[0], [1], [2], [3],[4],[5],[6],[8],[9]]);
#target values, sample
y = np.array([1,1,0,0,1,0,0,1,1]);
#test valdation set, not used yet, might not be needed
v= np.array([[2,1],[3,0],[5,1],[6,1],[9,0],[5,1],[4,0]]);
#classifier initilized
clf = KNeighborsClassifier(n_neighbors=9);

#weighted score, tracks accuracy
dscore =[.7,[9]];

#fits sample data sets to classifier, trains classifier
clf.fit(X, y);

#sample prediction, results not always as predicated
print(clf.predict([[2.5]]))
#Shows probability of 0 and 1.
print(clf.predict_proba([[0.5]]))
#not working scoring
#print(clf.score(X,y,[dscore]));


#serialize object, not sure what needs to be added or how to use it
clf.pickle
