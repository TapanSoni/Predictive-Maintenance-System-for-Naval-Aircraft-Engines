from sklearn import tree

#Decision Tree

def classify(trainingData,trainingTags,validationData,validationTags):
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