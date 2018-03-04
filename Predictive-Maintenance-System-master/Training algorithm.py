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

import FindMinAndMax as find

findingMinAndMax = find.FindMinAndMax(whole_data_set)
#Todo: Figure out a way to have the main method called automatically
findingMinAndMax.main()

min = findingMinAndMax.getMax()
max = findingMinAndMax.getMin()

import GenerateData as gen
new_data_set = gen.generate(min,max)
print("Generated New DATa")

#combines the old and new dataset in that order
#Todo: maybe have it so that it randomly combines the dataset sets whilst maintaining sequencal order
whole_data_set = np.concatenate((whole_data_set,new_data_set), axis = 0)

max_abs_scaler = preprocessing.MaxAbsScaler() #normalizes data
whole_data_set = max_abs_scaler.fit_transform(whole_data_set)
print("Normalized Data")

import GenerateTags as tag

tags = tag.generate(.7, whole_data_set.size//30)

index = 0

trainingData = []
trainingTags = []
validationData = []
validationTags = []

import math

indexsForTrainingData = []

#Randomly puts 40% of the data into valdation sequencly
while index < whole_data_set.size//30 and (len(validationData)) < math.floor((whole_data_set.size//30)*.4): #change .4 to whichever percentage you'd like togo to valadation set
    if(random.randint(0,1)==0):
        validationData.append(whole_data_set[index])
        validationTags.append(tags[index])
    else:
        indexsForTrainingData.append(index)
    index += 1

while(index < whole_data_set.size//30):
    indexsForTrainingData.append(index)
    index += 1

index = 0

while index < len(indexsForTrainingData):
    trainingData.append(whole_data_set[indexsForTrainingData[index]])
    trainingTags.append(tags[indexsForTrainingData[index]])
    index += 1

print("Generated Tags")

print("Kneighbor:")
neighbor = 1

#Todo: Knearest neighbor is taken extremely long now that our datasize has double see if this can be imporved
# while neighbor<100:
#classy = KNeighborsClassifier(n_neighbors=neighbor);
#classy = classy.fit(trainingData, trainingTags) #change name of classy
#     print("Testing for Kneighbor:", neighbor)
#print(classy.score(validationData,validationTags)) #how successful the test was
#     neighbor += 2
from sklearn import tree
from sklearn.linear_model import SGDClassifier
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

#Decision Tree
print("Decision Tree: ")
Dclf = tree.DecisionTreeClassifier()
Dclf = Dclf.fit(trainingData, trainingTags)

#index = 0

#Comparing the predicting of 0 vs 1 for dtree
"""
yea = 0
nah = 0

# while index < validationData.size/30:
#     if(Dclf.predict([validationData[index]]) == [0]):
#         nah += 1
#     else:
#         yea += 1
#     print(Dclf.predict([validationData[index]]))
#     index += 1
print("yea: ", yea)
print("nah: ", nah)
"""
print(Dclf.score(validationData,validationTags))


#GradientBoostingClassifier
from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
#print("Gradient Boosting Classifier: ")
#clf = GradientBoostingClassifier(n_estimators=50, learning_rate=1.0, max_depth=3, random_state=0).fit(trainingData,trainingTags)
#print(clf.score(validationData, validationTags))

################
#LinearSVC
from sklearn.svm import LinearSVC

print("LinearSVC:")
clf = LinearSVC()
#clf.fit(trainingData, trainingTags)
#print(clf.score(validationData,validationTags))
#print(clf.decision_function(validationData))

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