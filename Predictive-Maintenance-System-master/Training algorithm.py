#install numpy, scipy, scikit to workspace

import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#imports we will use

import random as random
import sklearn;
import numpy;
import time
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
from sklearn import preprocessing

"""
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
xtrain,xtest,ytrain,ytest= train_test_split(X,y,test_size=0.33, random_state=2, shuffle=False) #M&M - I don't think we should use this function since it'll randomize the sequence of the data, we want to have it randomized but kept in chronological order
#classifier initilized
clf = KNeighborsClassifier(n_neighbors=3);

print("Will it blend?")
print(xtrain)
print(xtest)
print(ytrain)
print(ytest)

#weighted score, tracks accuracy
dscore =[.7,[9]];

#fits sample data sets to classifier, trains classifier
neighbor = clf.fit(X, y);

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

#SVM test,  might be a better shape for our problem

#won't be worth is without support vectors.
#The validation set could be support vectors
print("test SVM")
A= [[2,0],[1,1],[3,0]]
b=[0,0,1]
vector = svm.SVC()

vector.fit(A,b)
s=vector.support_vectors_
print(vector.predict([[2,2]]))
print(s)
print("end svm")
#End SVM
"""
#####################
#####################
#####################
#Mike's section
#Number of Rows in dataset 589223

#Todo: Break up this file into each different type of classifier also data processing, generation

# START TIMER -- DO THE TESTING AFTER THIS
start_time = time.time()

import importCSV as read

whole_data_set = read.readIn('/Users/MM/Downloads/data.txt')

import matplotlib.pyplot as plt
plt.hist(whole_data_set[0])
plt.show()

max_abs_scaler = preprocessing.MaxAbsScaler() #normalizes data
whole_data_set = max_abs_scaler.fit_transform(whole_data_set)

print("Imported Data")

####################
#trying to make a histogram section
"""
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

x = whole_data_set[:,0]
#values = [go.Histogram(x=x)]
#py.iplot(values, filename='test')

plt.hist(x)
plt.title("Column 1")
plt.xlabel("Value")
plt.ylabel("Frequency")

fig = plt.gcf()

plot_url = py.plot_mpl(fig, filename='testing&432')
"""

#####################
#Trying to generate realistic random data section

#new_data = numpy.zeros(shape=(589223,30))

print("Generated New DATa")

print("Normalized Data")

import GenerateTags as tag

tags = tag.generate(.7, whole_data_set.size//30)
print("Generated Tags")

import SplitData as split

data = split.split(whole_data_set,tags,.49)

trainingData = split.getTrainingData()
trainingTags = split.getTrainingTags()
validationData = split.getValidationData()
validationTags = split.getValidationTags()
print("Split DATA")

import FindMinAndMax as find

findingMinAndMax = find.FindMinAndMax(trainingData)
#Todo: Figure out a way to have the main method called automatically
findingMinAndMax.main()

min = findingMinAndMax.getMax()
max = findingMinAndMax.getMin()

import GenerateData as gen
new_data_set = gen.generate(min,max,len(trainingData))

newTags = tag.generate(.7,new_data_set.size//30)

#combines the old and new dataset in that order
#Todo: maybe have it so that it randomly combines the dataset sets whilst maintaining sequential order
trainingData = np.concatenate((trainingData,new_data_set), axis = 0)
trainingTags = np.concatenate((trainingTags,newTags), axis=0)


import KNeighbor as kneighbor

#kneighbor.classify(1,trainingData,trainingTags,validationData,validationTags)

import dtree as tree

tree.classify(trainingData,trainingTags,validationData,validationTags)

from sklearn import tree
from sklearn.linear_model import SGDClassifier
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

#GradientBoostingClassifier
from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
#print("Gradient Boosting Classifier: ")
#clf = GradientBoostingClassifier(n_estimators=50, learning_rate=1.0, max_depth=3, random_state=0).fit(trainingData,trainingTags)
#print(clf.score(validationData, validationTags))

import LinearSVC as linear

#linear.classify(trainingData,trainingTags,validationData,validationTags)

################
#Trying to graph decision tree
import graphviz

# dot_data = StringIO()
# export_graphviz(Dclf, out_file=dot_data, filled=True, rounded=True, special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# Image(graph.create_png())

#dot_data = tree.export_graphviz(Dclf, out_file="test")
#graph = graphviz.Source(dot_data)

print("********* %s seconds *********" % (time.time() - start_time))
# END TIMER -- DO ALL THE TESTING BEFORE