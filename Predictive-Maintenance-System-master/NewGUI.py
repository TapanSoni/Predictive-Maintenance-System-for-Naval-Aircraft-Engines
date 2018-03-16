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

    import GenerateTags as tag

    tags = tag.generate(.7, whole_data_set.size // 30)
    print("Generated Tags")

    import SplitData as split

    data = split.split(whole_data_set, tags, .1)

    trainingData = split.getTrainingData()
    trainingTags = split.getTrainingTags()
    validationData = split.getValidationData()
    validationTags = split.getValidationTags()
    print("Split DATA")

    import FindMinAndMax as find

    findingMinAndMax = find.FindMinAndMax(trainingData)

    min = findingMinAndMax.getMax()
    max = findingMinAndMax.getMin()

    import GenerateData as gen
    new_data_set = gen.generate(min, max, len(trainingData))
    print("Generated New DATa")

    # row = int(sys.argv[1])
    #
    # print(type(row))
    #
    # plt.hist(new_data_set[:,row])
    # plt.ylabel('# of T= imes')
    # plt.xlabel('Row #: ' + str(row))
    # plt.savefig("generated row" + str(row) + ".png")
    # print("Saved row: " + str(row))

    newTags = tag.generate(.7, new_data_set.size // 30)

    # combines the old and new dataset in that order
    # Todo: maybe have it so that it randomly combines the dataset sets whilst maintaining sequential order
    trainingData = np.concatenate((trainingData, new_data_set), axis=0)
    trainingTags = np.concatenate((trainingTags, newTags), axis=0)

    # oldIndex = 0
    # newIndex = 0
    # newtrainingData = numpy.empty()
    # newtrainingTags = numpy.empty()
    #
    # while(oldIndex < len(trainingData) and newIndex < len(new_data_set)):
    #     if (oldIndex < len(trainingData) and random.randint(0, 1) == 0):
    #         newtrainingData.append(trainingData[oldIndex])
    #         newtrainingTags.append(trainingTags[oldIndex])
    #         oldIndex += 1
    #     else:
    #         newtrainingData.append(new_data_set[newIndex])
    #         newtrainingData.append(newTags[newIndex])
    #         newIndex += 1
    #

    from sklearn.neural_network import MLPClassifier

    # neural network
    # net = MLPClassifier(solver='lbfgs', shuffle=False,random_state=1, verbose=True)
    # net.fit(trainingData, trainingTags)
    # print(net.score(validationData,validationTags))

    # Naive Bayes
    from sklearn.naive_bayes import GaussianNB

    guas = GaussianNB()
    guas.fit(trainingData, trainingTags)
    print(guas.score(validationData, validationTags))

    import KNeighbor as kneighbor

    # kneighbor.classify(1,trainingData,trainingTags,validationData,validationTags)

    import dtree as tree

    # tree.classify(trainingData,trainingTags,validationData,validationTags)

    from sklearn import tree
    from sklearn.linear_model import SGDClassifier
    from sklearn.externals.six import StringIO
    from IPython.display import Image
    from sklearn.tree import export_graphviz
    import pydotplus

    # GradientBoostingClassifier
    from sklearn.datasets import make_hastie_10_2
    from sklearn.ensemble import GradientBoostingClassifier
    # print("Gradient Boosting Classifier: ")
    # clf = GradientBoostingClassifier(n_estimators=50, learning_rate=1.0, max_depth=3, random_state=0).fit(trainingData,trainingTags)
    # print(clf.score(validationData, validationTags))

    import LinearSVC as linear

    # linear.classify(trainingData,trainingTags,validationData,validationTags)

    ################
    # Trying to graph decision tree
    import graphviz

    # dot_data = StringIO()
    # export_graphviz(Dclf, out_file=dot_data, filled=True, rounded=True, special_characters=True)
    # graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    # Image(graph.create_png())

    # dot_data = tree.export_graphviz(Dclf, out_file="test")
    # graph = graphviz.Source(dot_data)


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

