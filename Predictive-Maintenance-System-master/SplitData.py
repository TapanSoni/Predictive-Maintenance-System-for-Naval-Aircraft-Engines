import random
import numpy as np

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
        # for I in range(0,len(validationData)):
        #     if(np.array_equal(whole_data_set[indexsForTrainingData[index]], validationData[I])):
        #         print("We've got serious overfitting going on!")
        #     else:
        trainingData.append(whole_data_set[indexsForTrainingData[index]])
        trainingTags.append(tags[indexsForTrainingData[index]])
        index += 1

    # trainingData = np.asarray(trainingData)
    # trainingTags = np.asarray(trainingTags)
    # validationTags = np.asarray(validationTags)
    # validationData = np.asarray(validationData)

# Figure out what percentge of the rows a exactlly the same
    # for I in range(0,len(validationData)):
    #     for Y in range(I, len(trainingData)):
    #         if(np.array_equal(trainingData[Y], validationData[I])):
    #             print("Overfit!")
    #             print("Y: ", Y/len(trainingData))
    #             print("I: ", I/len(validationData))
    #             np.insert(trainingData, Y, validationData[I], 0)
    #             np.delete(validationData, I, 0)


def getTrainingData():
    return trainingData

def getTrainingTags():
    return trainingTags

def getValidationData():
    return validationData

def getValidationTags():
    return validationTags

# def getData():
#     return np.concatenate((trainingData,trainingTags,validationData,validationTags), axis=0)
