import random

trainingData = []
trainingTags = []
validationData = []
validationTags = []
indexsForTrainingData = []

def split(whole_data_set,tags, percentage):
    index = 0

    import math

    #Randomly puts 40% of the data into valdation sequencly
    while index < whole_data_set.size//30 and (len(validationData)) < math.floor((whole_data_set.size//30)* percentage): #change .4 to whichever percentage you'd like togo to valadation set
        if(random.randint(0,1)==0):
            validationData.append(whole_data_set[index])
            validationTags.append(tags[index])
        else:
            indexsForTrainingData.append(index)
        index += 1

    while(index < whole_data_set.size//30):
        indexsForTrainingData.append(index)
        index += 1

    index = 0

    while index < len(indexsForTrainingData):
        trainingData.append(whole_data_set[indexsForTrainingData[index]])
        trainingTags.append(tags[indexsForTrainingData[index]])
        index += 1

def getTrainingData():
    return trainingData

def getTrainingTags():
    return trainingTags

def getValidationData():
    return validationData

def getValidationTags():
    return validationTags

