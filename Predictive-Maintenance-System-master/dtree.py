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
 This is the dtree.py file. It is responsible for creating the decision t-
 ree classifer and using the classifier to predict over a set of test data
 . It also scores how accurately it's training worked on the validation d-
 ata set and prints out the score.

 Last edit: 4/1/18 @ 2:26 PM by Tapan Soni


-----------------------------------------------------------------------------
"""

from sklearn import tree

#Decision Tree Classifier

#=============================================================================================================
def classify(trainingData,trainingTags,validationData,validationTags,predict):
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

    return Dclf.predict(predict)
    # =============================================================================================================

    # tree.export_graphviz(Dclf,out_file = 'tree.dot')
    # import graphviz
    # dot_data = tree.export_graphviz(Dclf, out_file=None)
    # graph = graphviz.Source(dot_data)
    # graph.render("iris")
