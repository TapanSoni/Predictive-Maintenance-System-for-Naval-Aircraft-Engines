"""
-----------------------------------------------------------------------------

Rowan Computer Science Dept Spring 2018 Software Engineering Team Ostriches
Predictive Maintenance System for ASRC Federal Mission Solutions Engineering

Team Ostriches Members:
Product Owner:  Craig Wert
 Scrum Master:  John Stranahan
    Developer:  Tapan Soni
    Developer:  Michael Matthews
    Developer:  Joshua Jackson
    Developer:  Nicholas La Sala

-----------------------------------------------------------------------------

Description:
 This is the KNeighbor.py file. It is responsible for creating the K-Neig-
 hbor classifier and predicting the tags from the test data. It also scor-
 es how accurately it's training worked on the validation data set and pr-
 ints out the score.

 Last edit: 4/1/18 @ 2:26 PM by Tapan Soni


-----------------------------------------------------------------------------
"""

# Knearest neighbor is taken extremely long now that our datasize has double see if this can be improved
import pickle
from sklearn.neighbors import KNeighborsClassifier

#This has serialization (pickling) of classifier as well as inputting the data to the classifier
#=======================================================================================================================
def classify(neighbor,trainingData,trainingTags,validationData,validationTags):
    print("Kneighbor:")
    classy = KNeighborsClassifier(n_neighbors=neighbor);
    classy = classy.fit(trainingData, trainingTags) #change name of classy
    #output = open("classy.pkl", 'wb') #open output file
    #pickle.dump(classy, output) #pickle classifier
    # pkl_file = open('classy.pkl', 'rb') #open input file

    # classy = pickle.load(pkl_file) #unpickle pickled file
    print(classy.score(validationData,validationTags)) #how successful the test was

    #output.close() #close output file
    # pkl_file.close() #close input file
#=======================================================================================================================