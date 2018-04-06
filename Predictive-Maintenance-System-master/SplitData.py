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
 This is the SplitData.py file. It is responsible for splliting the entire
 data set into the training data and the validation data. It also generat-
 es the training and validation tags.

 Last edit: 4/1/18 @ 2:44 PM by Tapan Soni


-----------------------------------------------------------------------------
"""
#=============================================================================================================
#importing the library/packages we need

import random
import numpy as np
#=============================================================================================================

#=============================================================================================================
#These varibles are arrays that will hold training and validation data sets and tags

trainingData = []
trainingTags = []
validationData = []
validationTags = []
#=============================================================================================================

#Splits the data into 2 datasets one for training and the other for validation
#Parameters are as follows
#   - The whole entire data set
#   - The tags
#   - The percentage of rows that you want to go to the validation set
def split(whole_data_set,tags, percentage):

    index = 0

    import math

    average = 0

    x = []

    #Randomly puts 40% of the data into valdation sequencly
    while (len(validationData)) < math.floor((whole_data_set.size//30)* percentage) and (len(trainingData) < math.floor((whole_data_set.size//30)* 1-percentage)): #change .4 to whichever percentage you'd like togo to valadation set
        if(random.random()<percentage):
            validationData.append(whole_data_set[index])
            validationTags.append(tags[index])
            average += index
            x.append(index)
        else:
            trainingData.append(whole_data_set[index])
            trainingTags.append(tags[index])
        index += 1

    #This loop finishes going through the whole dataset and adding each row to training set

    if (len(validationData)) < math.floor((whole_data_set.size//30)* percentage):
        while(index < whole_data_set.size//30):
            trainingData.append(whole_data_set[index])
            trainingTags.append(tags[index])
            index += 1
    else:
        while (index < whole_data_set.size // 30):
            validationData.append(whole_data_set[index])
            validationTags.append(tags[index])
            index += 1


    # print(x[len(validationTags)-1])

    print("Validation is this percentage: ", len(validationTags)/(len(validationTags)+len(trainingTags)))

#=============================================================================================================
#The following method will obtain the training data set
def getTrainingData():
    return trainingData
#=============================================================================================================

#The following method will obtain the training tag data set
def getTrainingTags():
    return trainingTags
#=============================================================================================================

#The following method will obtain the validation data set
def getValidationData():
    return validationData
#=============================================================================================================

#The following method will obtain the validation tag data set
def getValidationTags():
    return validationTags
