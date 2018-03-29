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


random.seed(1331)
def bandr():
    start_time = time.time()

    tagPercentage = .7
    valPercentage = .3


    # Take in input
    anotherWindow.fileName = filedialog.askopenfilename(filetypes=(("txt files", ".txt"), ("CSV files", ".csv"), ("All files", "*.*")))
    print(anotherWindow.fileName)
    fileNameDisplay.config(text=anotherWindow.fileName)

    #Import data into to a multidimenional array
    whole_data_set = np.genfromtxt(anotherWindow.fileName, delimiter='\t')
    print("Data imported")

    # count = 0
    # for index in range(0,whole_data_set.size//30-2):
    #     for secondIndex in range(index+1,whole_data_set.size//30):
    #         if np.array_equal(whole_data_set[index], whole_data_set[secondIndex]):
    #             whole_data_set = np.delete(whole_data_set,secondIndex,0)
    #             count += 1
    # print("Count: ", count)

    max_abs_scaler = preprocessing.MaxAbsScaler()  # normalizes data
    whole_data_set = max_abs_scaler.fit_transform(whole_data_set)
    print("Data Nomalized")

    import GenerateTags as tag

    #Generates an array filled with 0's & 1's
    tags = tag.generate(tagPercentage, whole_data_set.size // 30)
    print("Generated Tags")

    #Splits the data into 2 sections training and validation
    #Note that this is done for both tags and the actual data
    import SplitData as split

    split.split(whole_data_set, tags, valPercentage)

    trainingData = split.getTrainingData()
    trainingTags = split.getTrainingTags()
    validationData = split.getValidationData()
    validationTags = split.getValidationTags()
    print("Split DATA")

    #Finds the minimum and maximum of each feature for the training set
    import FindMinAndMax as find

    findingMinAndMax = find.FindMinAndMax(trainingData)

    min = findingMinAndMax.getMax()
    max = findingMinAndMax.getMin()

    #Generates new random data within the bounds of each feature
    import GenerateData as gen
    new_data_set = gen.generate(min, max, len(trainingData))
    print("Generated New Data")

    #Generates new tags to go along with the new data
    newTags = tag.generate(tagPercentage, new_data_set.size // 30)

    # combines the old and new dataset in that order
    # Todo: maybe have it so that it randomly combines the dataset sets whilst maintaining sequential order
    trainingData = np.concatenate((trainingData, new_data_set), axis=0)
    trainingTags = np.concatenate((trainingTags, newTags), axis=0)

    #The prediction row is the last row of the whole data set that was removed from the file
    #To see if the differnet classifiers would guess the the right tag (tag should be 1, with our current tagging scheme)
    predictionRow = [[ 0.88235484,0.88888889,0.66007962,0.86468924,0.70113635,0.70113635
    ,0.65998294,0.86466262,0.65998294,0.86466262,0.79052779,0.94375827
    ,0.60797992,0.5966,0.78434617,0.91454678,0.99136213,0.7804214
    ,0.60791774,0.93109982,0.86464809,0.93109982,0.86464809,0.65393367
    ,0.65393367,1.,0.90909091,1.,1.,1.]]

    timeForClassifier = time.time() #start timer for the classifier

    from sklearn.neural_network import MLPClassifier

    # neural network (note might not want to use generated data with neural net)
    # net = MLPClassifier(solver='lbfgs', shuffle=False,random_state=1, verbose=True)
    # net.fit(trainingData, trainingTags)
    # print(net.score(validationData,validationTags))
    #
    # percentageVariable = net.predict(predictionRow)

    # Naive Bayes
    from sklearn.naive_bayes import GaussianNB

    guas = GaussianNB()
    guas.fit(trainingData, trainingTags)
    print(guas.score(validationData,validationTags))
    percentageVariable = guas.predict(predictionRow)

    import KNeighbor as kneighbor

    #percentageVariable = kneighbor.classify(1,trainingData,trainingTags,validationData,validationTags,predictionRow)
    import dtree as tree

    #percentageVariable = tree.classify(trainingData,trainingTags,validationData,validationTags,predictionRow)

    from sklearn import tree
    from sklearn.linear_model import SGDClassifier
    from sklearn.externals.six import StringIO
    from IPython.display import Image
    from sklearn.tree import export_graphviz
    import pydotplus

    # GradientBoostingClassifier
    from sklearn.datasets import make_hastie_10_2
    # from sklearn.ensemble import GradientBoostingClassifier
    # print("Gradient Boosting Classifier: ")
    # clf = GradientBoostingClassifier(n_estimators=50, learning_rate=1.0, max_depth=3, random_state=0).fit(trainingData,trainingTags)
    # print(clf.score(validationData, validationTags))
    # percentageVariable = clf.predict(predictionRow)

    import LinearSVC as linear

    #percentageVariable = linear.classify(trainingData,trainingTags,validationData,validationTags,predictionRow)

    timeForClassifier = time.time() - timeForClassifier #end timer for classifier

    if percentageVariable >.5:
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
