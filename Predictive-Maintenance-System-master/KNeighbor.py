# Knearest neighbor is taken extremely long now that our datasize has double see if this can be improved

from sklearn.neighbors import KNeighborsClassifier

def classify(neighbor,trainingData,trainingTags,validationData,validationTags, predict):
    print("Kneighbor:")
    classy = KNeighborsClassifier(n_neighbors=neighbor);
    classy = classy.fit(trainingData, trainingTags) #change name of classy
    print(classy.score(validationData,validationTags)) #how successful the test was

    return classy.predict(predict)