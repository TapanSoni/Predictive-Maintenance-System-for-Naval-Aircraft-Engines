#install numpy, scipy, scikit to workspace

import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#imports we will use

import random as random
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
xtrain,xtest,ytrain,ytest= train_test_split(X,y,test_size=0.33, random_state=42) #M&M - I don't think we should use this function since it'll randomize the sequence of the data, we want to have it randomized but kept in chronological order
#classifier initilized
clf = KNeighborsClassifier(n_neighbors=3);


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
#Mike's section
#length 589223
whole_data_set = np.genfromtxt('/Users/MM/Downloads/data.txt', delimiter='\t') #File path for file you'd like to import
print("Imported Data")
max_abs_scaler = preprocessing.MaxAbsScaler() #normalizes data
whole_data_set = max_abs_scaler.fit_transform(whole_data_set)
print("Normalized Data")
print(whole_data_set)
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

#print(np.random.randn(500))
x = whole_data_set[:,0]
#values = [go.Histogram(x=x)]
#py.iplot(values, filename='test')
"""
plt.hist(x)
plt.title("Column 1")
plt.xlabel("Value")
plt.ylabel("Frequency")

fig = plt.gcf()

plot_url = py.plot_mpl(fig, filename='testing&432')
"""
#new_data = numpy.zeros(shape=(589223,30))

for column in range(0,30):
    #column = 1
    temp = whole_data_set[0][column]
    temp_min = whole_data_set[0][column]

    flag = False

    for x in range(1,589223):
        """
        current = whole_data_set[x][column]
        if(current> temp):
            temp = current
        if(current< temp_min):
            temp_min = current
        #print(whole_data_set[x][1])
        if(current==whole_data_set[(x+1)%589223][column]):
            flag=True
        else:
            flag=False

    if(flag==True):
        print('Column: ', column, '\n&olumn', column+1)
    """
    #for i in range(0,589223):
    #    new_data[i][column] = random.uniform(temp_min,temp)


    #print('Max:',temp)
    #print('Min: ',temp_min)
    #print(avg/(whole_data_set.size/30))

"""
    print('Range: ', temp - temp_min)
    print('SD: ',np.std(whole_data_set[:,column]))
    print('Var: ',np.var(whole_data_set[:,column]))
    print('Avg: ',np.mean(whole_data_set[:,column]))
"""

#print(whole_data_set.size/30)

trainingData = whole_data_set[:412463] #getting the first 20% of the data set
validationData = whole_data_set[412464:whole_data_set.size//30]

tags = []
for i in range(0, 294616): #making the first half of the tagging array which will all be initilzed to '0'
    tags.append(0)
for i in range(0, 294616): #making the rest of the tagging array which will all be '1'
    tags.append(1)

trainingTags = tags[:412463]
validationTags = tags[412464:whole_data_set.size//30]
print("Generated Tags")

index = 1

while index<100:
    classy = KNeighborsClassifier(n_neighbors=index);
    classy = classy.fit(trainingData, trainingTags) #change name of classy
    print("Testing for Kneighbor:", index)
    print(classy.score(validationData,validationTags)) #how successful the test was
    index += 2