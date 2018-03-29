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



-----------------------------------------------------------------------------
"""

from sklearn.svm import LinearSVC

#LinearSVC

def classify(trainingData,trainingTags,validationData,validationTags,predict):
    print("LinearSVC:")
    clf = LinearSVC()
    clf.fit(trainingData, trainingTags)
    print(clf.score(validationData,validationTags))
    #print(clf.decision_function(validationData))
    return clf.predict(predict)