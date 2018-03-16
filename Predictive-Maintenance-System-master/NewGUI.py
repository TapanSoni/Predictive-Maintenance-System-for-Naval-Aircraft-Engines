from tkinter import *
from tkinter import filedialog

import math
import numpy as np
import random
import time

def browsefile():

    return np.genfromtxt(anotherWindow.fileName, delimiter='\t')


def readIn():
    whole_data_set = browsefile()
    return whole_data_set

def bandr():

    tags = []
    trainingData = []
    trainingTags = []
    validationData = []
    validationTags = []
    indexesForTrainingData = []


    # Take in input
    anotherWindow.fileName = filedialog.askopenfilename(filetypes=(("txt files", ".txt"), ("CSV files", ".csv"), ("All files", "*.*")))
    print(anotherWindow.fileName)
    fileNameDisplay.config(text=anotherWindow.fileName)
    whole_data_set = np.genfromtxt(anotherWindow.fileName, delimiter='\t')
    print("Data imported")



    #Generate tags
    for i in range (0, math.floor(.7 * (whole_data_set.size//30))):
        tags.append(0)
    for i in range(0, ((whole_data_set.size//30)) - math.floor(.7 * (whole_data_set.size//30))):
        tags.append(1)

    # Split the data

    index = 0
    while index < whole_data_set.size//30 and (len(validationData)) < math.floor(whole_data_set.size//30 * .1):
        if(random.randint(0,1)==0):
            validationData.append(whole_data_set[index])
            validationTags.append(tags[index])
        else:
            indexesForTrainingData.append(index)
        index += 1

    while (index < whole_data_set.size // 30):
        indexesForTrainingData.append(index)
        index += 1

    index = 0

    while index < len(indexesForTrainingData):
        trainingData.append(whole_data_set[indexesForTrainingData[index]])
        trainingTags.append(tags[indexesForTrainingData[index]])
        index += 1


    # Find min and max

    min = []
    max = []

    for column in range(0, 30):
        temp = trainingData[0][column]
        temp_min = trainingData[0][column]

        flag = False

        for x in range(1, len(trainingData)):
            current = trainingData[x][column]
            if(current > temp):
                temp = current
            if(current < temp_min):
                temp_min = current
            if(current == trainingData[(x + 1) % len(trainingData)][column]):
                flag = True
            else:
                flag = False


        if(flag == True):
            print('Column: ', column, '\ncolumn', column + 1)

        max.append(temp)
        min.append(temp_min)


    # Generate Data

    new_data_set = np.zeros((len(trainingData), 30))

    for x in range(0, 30):
        row = []

        for y in range(0, len(trainingData)):
            if (x == 0):
                got_a_number = False
                while (not got_a_number):
                    number = random.uniform(min[x], max[x])
                    if (not math.floor(number) == 5):
                        got_a_number = True
                        new_data_set[y][x] = number
            else:
                new_data_set[y][x] = random.uniform(min[x], max[x])


    newTags = []

    for i in range (0, math.floor(.7 * whole_data_set.size//30)):
        newTags.append(0)
    for i in range(0, (whole_data_set.size//30) - math.floor(.7 * whole_data_set.size//30)):
        newTags.append(1)

    trainingData = np.concatenate((trainingData, new_data_set), axis = 0)
    trainingTags = np.concatenate((trainingTags, newTags), axis=0)

    from sklearn.naive_bayes import GaussianNB

    gaus = GaussianNB()
    gaus.fit(trainingData, trainingTags)
    print(gaus.score(validationData, validationTags))

    # K-Neighbor

    from sklearn.neighbors import KNeighborsClassifier

    print("K-Neighbor")
    classy = KNeighborsClassifier(n_neighbors=1)
    classy = classy.fit(trainingData, trainingTags)
    print(classy.score(validationData, validationTags))


anotherWindow = Tk()


anotherWindow.iconbitmap(r'RowanLogo.ico')
anotherWindow.geometry("370x200")
anotherWindow.title("Predictive Maintenance System")

fileNamePrompt = Label(anotherWindow, text="Source")
outputConsolePrompt = Label(anotherWindow, text="Maintenance Needed (Yes or No)")

# Labels for output or showing selections
fileNameDisplay = Label(anotherWindow, bg="white", width="30") # Where the source file will be shown
outputConsole = Label(anotherWindow, bg="white", width="30") # For the output
classifierConsole = Label(anotherWindow, bg="white", width="30")
fake_1 = Label(anotherWindow)
fake_2 = Label(anotherWindow)
fake_3 = Label(anotherWindow)

# Buttons
fileNameBrowseButton = Button(anotherWindow, text="Browse", command=bandr)

runButton = Button(anotherWindow, text="Run")

# Configurations of the widgets
fileNamePrompt.config(font="fixedsys 9")
outputConsolePrompt.config(font="fixedsys 9")
fileNameBrowseButton.config(background="#EDDEA4", font="fixedsys 9")
runButton.config(background="#79FF6D", font="fixedsys 9")
fake_1.config(background="#EEF4EB")
fake_2.config(background="#EEF4EB")
anotherWindow.config(background="#EEF4EB")

# Giving position to the widgets and telling them to fill the area if resized
fileNamePrompt.grid(row=0, column=0, sticky=NSEW)
fileNameDisplay.grid(row=0, column=1, sticky=NSEW)
fileNameBrowseButton.grid(row=0, column=2, sticky=NSEW)
fake_1.grid(row=1, sticky=NSEW)
runButton.grid(row=2, column=1, sticky=NSEW)
outputConsolePrompt.grid(row=3, column=1, sticky=NSEW)
outputConsole.grid(row=4, column=1, sticky=NSEW)

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

