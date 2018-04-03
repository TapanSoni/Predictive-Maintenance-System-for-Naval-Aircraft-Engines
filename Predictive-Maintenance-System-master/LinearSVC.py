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
 This is the LinearSVC.py file. It is responsible for creating the linear-
 SVC classifier and testing it on the test data. It also prints out the
 validation score of the classifier to see how well it does when testing
 on the validation data.

 Last edit: 4/1/18 @ 3:01 PM by Tapan Soni


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
