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
 This is the NewGUI.py file. It is responsible for generating the GUI win-
 dow and all of its functionality. The functionality consists of a browse
 and run button which allows the user to select an input test data file a-
 nd then the program tests the classifier on the test data. It then shows
 the selected file in the file selection window, and outputs either a "Yes
 - Maintenance Needed" or "No - Everything is OK". The GUI also shows the
 total run time of the whole program, as well as the total run time of the
 classifier.

 Last edit: 4/1/18 @ 2:42 PM by Tapan Soni


-----------------------------------------------------------------------------
"""

from tkinter import *
from tkinter import filedialog

import math
import numpy as np
import random
import time
from sklearn import preprocessing
import pickle

#the seeding allows for the same random at this point in the data every time
#=============================================================================================================
random.seed(1331)
#=============================================================================================================

#=============================================================================================================
def bandr():
    start_time = time.time()

    tagPercentage = .93
    valPercentage = .15

    # Take in input
    anotherWindow.fileName = filedialog.askopenfilename(filetypes=(("txt files", ".txt"), ("CSV files", ".csv"), ("All files", "*.*")))
    print(anotherWindow.fileName)
    fileNameDisplay.config(text=anotherWindow.fileName)

    #Import data into to a multidimenional array
    #whole_data_set = np.genfromtxt(anotherWindow.fileName, delimiter='\t')
    testData = np.genfromtxt(anotherWindow.fileName, delimiter=',')

    #print("datasize: ", whole_data_set.size//30)
    #testData = np.genfromtxt(anotherWindow.fileName, delimiter=',') #the origanl
    print("Data imported")

    #max_abs_scaler = preprocessing.MaxAbsScaler()  # normalizes data
    #whole_data_set = max_abs_scaler.fit_transform(whole_data_set)
    # print("Data Nomalized")

    # testingData = []
    # index = 500000
    # count = 500000
    #
    # while(count<509223):
    #     #testingData.append(whole_data_set[index])
    #     whole_data_set = np.delete(whole_data_set, index, 0)
    #     count += 1
    #     print(count)
    #
    # print(whole_data_set.size//30)

    import pickle
    #outputTest = open("testData_500k_501k.pkl", 'wb') #open output file
    #outputWhole = open("wholeData_500k_501k.pkl", 'wb')
    #pickle.dump(testingData, outputTest)
    #pickle.dump(whole_data_set, outputWhole)

    #pkl_file_test = open('testData.pkl', 'rb') # open input file
    pkl_file_whole = open('wholeData.pkl', 'rb') # open input file

    #testData = pickle.load(pkl_file_test)
    whole_data_set = pickle.load(pkl_file_whole)

    #outputTest.close() #close output file
    #outputWhole.close()
    #pkl_file_test.close() # close input file

    import GenerateTags as tag

    #Generates an array filled with 0's & 1's
    #tags = tag.generate(tagPercentage, whole_data_set.size // 30)
    # print("Generated Tags")

    # Splits the data into 2 sections training and validation
    # Note that this is done for both tags and the actual data
    import SplitData as split

    #split.split(whole_data_set, tags, valPercentage)

    # trainingData = split.getTrainingData()
    # trainingTags = split.getTrainingTags()
    # validationData = split.getValidationData()
    # validationTags = split.getValidationTags()

    # =============================================================================================================
    #print("Split DATA")
    # =============================================================================================================

    #Finds the minimum and maximum of each feature for the training set
    import FindMinAndMax as find

    # findingMinAndMax = find.FindMinAndMax(trainingData)
    #
    # minOf = findingMinAndMax.getMin()
    # maxOf = findingMinAndMax.getMax()
    #range = findingMinAndMax.getRan()

    # for index in range(0,30):
    #     print("Range for row ", index, ": ", maxOf[index]-minOf[index])

    #Generates new random data within the bounds of each feature
    import GenerateData as gen
    # new_data_set = gen.generate(minOf, maxOf, len(trainingData))
    # print("Generated New Data")

    #Generates new tags to go along with the new data
    # newTags = tag.generate(tagPercentage, new_data_set.size // 30)

    # combines the old and new dataset in that order
    # Todo: maybe have it so that it randomly combines the dataset sets whilst maintaining sequential order
    # trainingData = np.concatenate((trainingData, new_data_set), axis=0)
    # trainingTags = np.concatenate((trainingTags, newTags), axis=0)

    timeForClassifier = time.time() #start timer for the classifier

    from sklearn.cluster import KMeans

    data = np.zeros(shape=(whole_data_set.size // 30, 2))

    for row in range(0, whole_data_set.size // 30):
        firstAverage = 0
        secondAverage = 0
        for column in range(0, 15):
            firstAverage += whole_data_set[row][column]
        for column in range(15, 30):
            secondAverage += whole_data_set[row][column]
        data[row][0] = firstAverage / 2
        data[row][1] = secondAverage / 2

    whole_data_set = data
    clusterCenters = [[0, 0]]
    newTest = np.zeros(shape=(len(testData), 2))

    for row in range(0, len(testData)):
        firstAverage = 0
        secondAverage = 0
        for column in range(0, 15):
            firstAverage += testData[row][column]
        for column in range(15, 30):
            secondAverage += testData[row][column]
        newTest[row][0] = firstAverage / 2
        newTest[row][1] = secondAverage / 2

    index = whole_data_set.size // 2

    newTest = np.concatenate((whole_data_set, newTest), axis=0)

    average = 0

    while index < len(newTest):
        ok = KMeans(n_clusters=1, random_state=0).fit(newTest[:index])
        if (ok.cluster_centers_[0][0] + ok.cluster_centers_[0][1] > 4.514):
            average = 1
            break
        clusterCenters.append(ok.cluster_centers_[0])
        index += 100

    clusterCenters.pop(0)

    import matplotlib.pyplot as plt

    # pkl_file_whole = open('clusterCenters.pkl', 'rb') # open input file
    # clusterCenters = pickle.load(pkl_file_whole)
    #
    # pkl_file_whole.close()

    sums = np.zeros(shape=(2, len(clusterCenters)))
    averages = np.zeros(shape=(2, len(clusterCenters)))

    for index in range(0, len(clusterCenters)):
        averages[0][index] = index
        averages[1][index] = (clusterCenters[index][0] + clusterCenters[index][1]) / 2
        sums[0][index] = index
        sums[1][index] = clusterCenters[index][0] + clusterCenters[index][1]

    # plt.plot(averages[0],averages[1])
    # plt.show()

    pkl_file_whole.close()

    import KNeighbor as kneighbor

    #kneighbor.classify(299,trainingData,trainingTags,validationData,validationTags)

    #pkl_file = open('classy.pkl', 'rb') #open input file

    #classy = pickle.load(pkl_file) #unpickle pickled file

    #testData = np.asarray(testData)

    #np.savetxt('testData.csv', testData, delimiter=',')

    #np.savetxt('wholedataset.csv', whole_data_set_pickle, delimiter=',')

    indices = []
    #indices = np.asarray(indices)
    count = 50

    # for index in range(0, len(testData)):
    #     average += classy.predict([testData[index]]).item(0)
    #     if count <= len(testData):
    #         indices.append(testData[count])
    #         count += 100
    #
    # import plotly.plotly as py
    # import plotly.graph_objs as go
    #
    # trace = go.Scatter(
    #     x = indices,
    #     y = testData
    # )
    #
    # data = [trace]
    #
    # py.plot(data, filename='testingResults')
    #
    #print("Average: ", average/len(testData))

    timeForClassifier = time.time() - timeForClassifier #end timer for classifier

    if average <.5:
        outputConsole.config(text="No - Everything is OK")
    else:
        outputConsole.config(text="Yes - Maintenance needed")

    totaltimeTaken = time.time() - start_time
    print("********* %s seconds *********" % totaltimeTaken)
    timestampC.config(text="Classifier Run Time: %s seconds" % timeForClassifier)
    timestamp.config(text="  Total Time Elapsed: %s seconds" % totaltimeTaken)

    # Pickling the classifier
    # fileToStore = "testfile"
    #
    # fileObject = open(fileToStore, 'wb')
    #
    # pickle.dump(kneighbor.classify(1, trainingData, trainingTags, validationData, validationTags, new_data_set), fileObject)
    #
    # fileObject.close()

anotherWindow = Tk()

anotherWindow.iconbitmap(r'RowanLogo.ico')
anotherWindow.geometry("370x200")
anotherWindow.title("Predictive Maintenance System")

fileNamePrompt = Label(anotherWindow, text="Source")
outputConsolePrompt = Label(anotherWindow, text="Maintenance Needed (Yes or No)")

# Labels for output or showing selections
fileNameDisplay = Label(anotherWindow, bg="white", width="30")  # Where the source file will be shown
outputConsole = Label(anotherWindow, bg="white", width="30")  # For the output
classifierConsole = Label(anotherWindow, bg="white", width="30")
fake_1 = Label(anotherWindow)
fake_2 = Label(anotherWindow)
fake_3 = Label(anotherWindow)
timestamp = Label(anotherWindow, bg = "#F0F0F0", width="30")
timestampC = Label(anotherWindow, bg = "#F0F0F0", width="30")

# Buttons
# fileNameBrowseButton = Button(anotherWindow, text="Browse", command=bandr)

runButton = Button(anotherWindow, text="Browse & Run", command=bandr)

# Configurations of the widgets
fileNamePrompt.config(font="fixedsys 9")
outputConsolePrompt.config(font="fixedsys 9")
# fileNameBrowseButton.config(background="#EDDEA4", font="fixedsys 9")
runButton.config(background="#79FF6D", font="fixedsys 9")
fake_1.config(background="#EEF4EB")
fake_2.config(background="#EEF4EB")
anotherWindow.config(background="#EEF4EB")

# Giving position to the widgets and telling them to fill the area if resized
fileNamePrompt.grid(row=0, column=1, sticky=NSEW)
fileNameDisplay.grid(row=1, column=1, sticky=NSEW)
# fileNameBrowseButton.grid(row=0, column=2, sticky=NSEW)
fake_1.grid(row=1, sticky=NSEW)
runButton.grid(row=3, column=1, sticky=NSEW)
outputConsolePrompt.grid(row=4, column=1, sticky=NSEW)
outputConsole.grid(row=5, column=1, sticky=NSEW)
timestampC.grid(row=6, column=1, sticky=NSEW)
timestamp.grid(row=7, column=1, sticky=NSEW)

# The widgets will fill with the parent
anotherWindow.grid_rowconfigure(0, weight=1)
anotherWindow.grid_rowconfigure(1, weight=1)
anotherWindow.grid_rowconfigure(2, weight=1)
anotherWindow.grid_rowconfigure(3, weight=1)
anotherWindow.grid_rowconfigure(4, weight=1)
anotherWindow.grid_rowconfigure(5, weight=1)
anotherWindow.grid_rowconfigure(6, weight=1)
anotherWindow.grid_rowconfigure(7, weight=1)
anotherWindow.grid_rowconfigure(8, weight=1)
anotherWindow.grid_rowconfigure(9, weight=1)
anotherWindow.grid_rowconfigure(10, weight=1)

anotherWindow.grid_columnconfigure(0, weight=1)
anotherWindow.grid_columnconfigure(1, weight=1)
anotherWindow.grid_columnconfigure(2, weight=1)

anotherWindow.mainloop()
#=============================================================================================================