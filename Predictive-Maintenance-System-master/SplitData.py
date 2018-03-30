#
#
#
#
#
#
#

import random
import numpy as np

trainingData = []
trainingTags = []
validationData = []
validationTags = []

#Splits the data into 2 datasets one for training and the other for validation
#Parameters are as follows
#   - The whole entire data set
#   - The tags
#   - The percentage of rows that you want to go to the validation set
def split(whole_data_set,tags, percentage):
    index = 0

    import math

    #Randomly puts 30% of the data into valdation sequencly
    while index < whole_data_set.size//30 and (len(validationData)) < math.floor((whole_data_set.size//30)* percentage): #change .4 to whichever percentage you'd like togo to valadation set
        if(random.randint(0,1)==0):
            validationData.append(whole_data_set[index])
            validationTags.append(tags[index])
        else:
            trainingData.append(whole_data_set[index])
            trainingTags.append(tags[index])
        index += 1

    #This loop finishes going through the whole dataset and adding each row to training set
    while(index < whole_data_set.size//30):
        trainingData.append(whole_data_set[index])
        trainingTags.append(tags[index])
        index += 1


def getTrainingData():
    return trainingData

def getTrainingTags():
    return trainingTags

def getValidationData():
    return validationData

def getValidationTags():
    return validationTags
