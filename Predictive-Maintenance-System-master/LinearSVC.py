from sklearn.svm import LinearSVC

#LinearSVC

def classify(trainingData,trainingTags,validationData,validationTags,predict):
    print("LinearSVC:")
    clf = LinearSVC()
    clf.fit(trainingData, trainingTags)
    print(clf.score(validationData,validationTags))
    #print(clf.decision_function(validationData))
    return clf.predict(predict)