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
from sklearn.metrics import accuracy_score
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
xtrain,xtest,ytrain,ytest= train_test_split(X,y,test_size=0.33, random_state=42)
#classifier initilized
clf = KNeighborsClassifier(n_neighbors=3);

#weighted score, tracks accuracy
dscore =[.7,[9]];

#fits sample data sets to classifier, trains classifier
clf.fit(X, y);

def train(xtrain,ytrain):
    return

#sample prediction, results not always as predicated
prediction = clf.predict([[0.5],[2.5],[3.3]]);
print(prediction)
print(ytest)
prediction=prediction.reshape(-1,1)
print(prediction)
ytest=ytest.reshape(-1,1)
print(ytest)
#Shows probability of 0 and 1.  Not sure why it does not seem accurate
print(clf.predict_proba([[0.9]]))

#not working scoring
score= clf.score(ytest, prediction)
print(score)


#serialize object, not sure what needs to be added or how to use it
#clf.pickle



#####################
#Mike's section
whole_data_set = np.genfromtxt('/Users/MM/Downloads/data.txt', delimiter='\t') #File path for file you'd like to import

trainingData_first_half = whole_data_set[:117844] #getting the first 20% of the data set
trainingData_second_half = whole_data_set[589223-117844:589223] #getting the last 20% of the data set

#tags_first_half = np.full((117844,1),0)
#tags_second_half = np.full((117844,1),1)

tags = []
for i in range(0, 117844): #making the first half of the tagging array which will all be initilzed to '0'
    tags.append(0)
for i in range(0, 117844): #making the rest of the tagging array which will all be '1'
    tags.append(1)

data = numpy.concatenate((trainingData_first_half, trainingData_second_half), axis = 0) #concates the first 20% and last 20% of dataset

classy = KNeighborsClassifier(n_neighbors=3);
classy = classy.fit(data, tags)

#an actual row from the dataset note that I manually inputed it, I trying to figure out a way of extracting rows from
#the 'data' variable
print(classy.predict([[7.1481,	21,	39248,	2678,	335.23,	335.23,	4.4812e+05,	117.27,	4.4812e+05,	117.27,	817.95,	9116.1,	0.86869,	47.291,	15.75,	685.13,	1.0361,	2.9983,	43.875,	0.18376,	1.9545,	0.18376,	1.9545,	4.1877e+05,	4.1877e+05,	1,	1,	1.0143,	0.99643,	0.98214]]))

