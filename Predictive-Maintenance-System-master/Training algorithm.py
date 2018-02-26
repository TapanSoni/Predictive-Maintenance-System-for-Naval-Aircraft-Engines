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
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

#need to field from the csv file.
# need fields for clasifcation algorithm

#test array 1 represent the training data
X = np.array([[0], [1], [2], [3]])
#test array 2 represents the tags
y = np.array([0,0,1,1])
#test valdation set
v= np.array([[2,1],[3,0],[5,1],[6,1],[9,0]])
#classifier
clf = KNeighborsClassifier(n_neighbors=3);
#training classfier with both arrays

#weighted desired score
dscore =.07;

clf.fit(X, y)
clf.score(X,y,[dscore]);