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

test="test for git";
#need to field from the csv file.
# need fields for clasifcation algorithm

#test array 1
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
#test array 2
y = np.array([1, 1, 2, 2])
#classifier
clf = SVC();
#training classfier with both arrays
clf.fit(X, y)
