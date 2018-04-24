from tkinter import *
from tkinter import filedialog

import math
import numpy as np
import random
import time
import webbrowser
from sklearn import preprocessing
import pickle
from passlib import *
from passlib.hash import pbkdf2_sha256
from ilio import read

random.seed(1331)

class loginGUI:
    def __init__(self, root):
        self.parent = root
        self.parent.title("Login")
        self.parent.iconbitmap(r'RowanLogo.ico')
        self.parent.geometry("200x150")
        self.selection = -1
        self.LoginWindow(root)

    def LoginWindow(self, root):
        self.usernamePrompt = Label(root, text="Username")
        self.passwordPrompt = Label(root, text="Password")
        self.errorOrCorrect = Label(root)

        self.radioButtonVariable = IntVar()

        self.predictButt = Radiobutton(root, text = "Predict", variable = self.radioButtonVariable, value = 1,
                                       command = self.selectPredict)
        self.trainButt = Radiobutton(root, text = "Train", variable = self.radioButtonVariable, value = 2,
                                       command = self.selectTrain)

        self.loginButton = Button(self.parent, text="Login", command=self.loginInButtonClicked)
        self.loginButton.grid(row = 5, columnspan=2)
        self.loginButton.config(font="fixedsys 9")

        self.usernamePrompt.config(font="fixedsys 9")
        self.passwordPrompt.config(font="fixedsys 9")

        self.usernameEntry = Entry()
        self.passwordEntry = Entry(show=" ")

        self.usernamePrompt.place(x = 0, y = 10, anchor = "w")
        self.passwordPrompt.place(x = 0, y = 30, anchor = "w")

        self.usernameEntry.place(x = 70, y = 10, anchor = "w")
        self.passwordEntry.place(x = 70, y = 30, anchor = "w")

        self.predictButt.place(x = 70, y = 50, anchor = "w")
        self.trainButt.place(x = 70, y = 70, anchor = "w")

        self.errorOrCorrect.place(x = 100, y = 90, anchor = "center")
        self.loginButton.place(x = 100, y = 115, anchor = "center")


    def loginInButtonClicked(self):
        print("Login Button Clicked")

        self.goodOrNot = False

        self.username = self.usernameEntry.get()
        self.password = self.passwordEntry.get()

        print("Username: ", str(self.username))
        print("Password: ", str(self.password))

        if self.username == "admin" and self.password == "password" and (self.selection == 1 or self.selection == 0):
            print("Correct login")
            self.parent.destroy()
            self.mainWindow()
        elif self.username != "admin" or self.password != "password":
            self.passwordEntry.delete(0, 'end')
            self.usernameEntry.delete(0, 'end')
            self.usernameEntry.focus_set()
            self.errorOrCorrect.config(text = "Incorrect credentials")
        elif self.selection != 0 or self.selection != 1:
            self.errorOrCorrect.config(text = "Select an option")


    def mainWindow(self):
        self.anotherWindow = Tk()
        self.anotherWindow.title("Predictive Maintenance System")
        self.anotherWindow.iconbitmap(r'RowanLogo.ico')
        self.anotherWindow.geometry("400x200")
        self.fileNamePrompt = Label(self.anotherWindow, text="Source")
        self.outputConsolePrompt = Label(self.anotherWindow, text="Maintenance Needed (Yes or No)")

        # Labels for output or showing selections
        self.fileNameDisplay = Label(self.anotherWindow, bg="white", width="30")  # Where the source file will be shown
        self.outputConsole = Label(self.anotherWindow, bg="white", width="30")  # For the output
        self.classifierConsole = Label(self.anotherWindow, bg="white", width="30")
        self.fake_1 = Label(self.anotherWindow)
        self.fake_2 = Label(self.anotherWindow)
        self.fake_3 = Label(self.anotherWindow)
        self.timestamp = Label(self.anotherWindow, bg="#F0F0F0", width="30")
        self.timestampC = Label(self.anotherWindow, bg="#F0F0F0", width="30")

        self.runButton = Button(self.anotherWindow, text="Browse & Run", command=self.trainOrPredict)

        self.aboutButton = Button(self.anotherWindow, text="About", command=self.about)

        # Configurations of the widgets
        self.fileNamePrompt.config(font="fixedsys 9")
        self.outputConsolePrompt.config(font="fixedsys 9")
        # fileNameBrowseButton.config(background="#EDDEA4", font="fixedsys 9")
        self.runButton.config(background="#79FF6D", font="fixedsys 9")
        self.fake_1.config(background="#EEF4EB")
        self.fake_2.config(background="#EEF4EB")
        self.anotherWindow.config(background="#EEF4EB")
        self.aboutButton.config(background="orange", font="fixedsys 9")

        # Giving position to the widgets and telling them to fill the area if resized
        self.fileNamePrompt.grid(row=0, column=1, sticky=NSEW)
        self.fileNameDisplay.grid(row=1, column=1, sticky=NSEW)
        # fileNameBrowseButton.grid(row=0, column=2, sticky=NSEW)
        self.fake_1.grid(row=1, sticky=NSEW)
        self.runButton.grid(row=3, column=1, sticky=NSEW)
        self.outputConsolePrompt.grid(row=4, column=1, sticky=NSEW)
        self.outputConsole.grid(row=5, column=1, sticky=NSEW)
        self.timestampC.grid(row=6, column=1, sticky=NSEW)
        self.timestamp.grid(row=7, column=1, sticky=NSEW)
        self.aboutButton.grid(row=8, column=1, sticky=NSEW)

        # The widgets will fill with the parent
        self.anotherWindow.grid_rowconfigure(0, weight=1)
        self.anotherWindow.grid_rowconfigure(1, weight=1)
        self.anotherWindow.grid_rowconfigure(2, weight=1)
        self.anotherWindow.grid_rowconfigure(3, weight=1)
        self.anotherWindow.grid_rowconfigure(4, weight=1)
        self.anotherWindow.grid_rowconfigure(5, weight=1)
        self.anotherWindow.grid_rowconfigure(6, weight=1)
        self.anotherWindow.grid_rowconfigure(7, weight=1)
        self.anotherWindow.grid_rowconfigure(8, weight=1)

        self.anotherWindow.grid_columnconfigure(0, weight=1)
        self.anotherWindow.grid_columnconfigure(1, weight=1)
        self.anotherWindow.grid_columnconfigure(2, weight=1)

    def about(self):
        self.aboutWindow = Tk()
        self.aboutWindow.iconbitmap(r'RowanLogo.ico')
        self.aboutWindow.title("About")
        self.aboutWindow.geometry("400x550")

        self.titleText = Label(self.aboutWindow, text="Predictive Maintenance System")
        self.titleText.config(bg="#EEF4EB", font="fixedsys 9")
        self.titleText.place(x=200, y=10, anchor="center")

        self.fromText = Label(self.aboutWindow, text="Rowan University - Team Ostriches - Spring 2018")
        self.fromText.config(bg="#EEF4EB", font="fixedsys 9")
        self.fromText.place(x=200, y=30, anchor="center")

        self.forText = Label(self.aboutWindow, text="ASRC Federal Mission Solutions")
        self.forText.config(bg="#EEF4EB", font="fixedsys 9")
        self.forText.place(x=200, y=50, anchor="center")

        # Link to the sample data files
        self.libraryOfCSVFiles = Label(self.aboutWindow, text="Library of Sample Test Data - Drop Box Link",
                                       cursor="hand2",
                                       fg="brown", font="fixedsys 9")
        self.libraryOfCSVFiles.place(x=200, y=70, anchor="center")
        self.libraryOfCSVFiles.bind("<Button-1>", self.callback)

        # Link to the github for our project
        self.linkToGit = Label(self.aboutWindow, text="Source Code - Github Link", cursor="hand2",
                               fg="brown", font="fixedsys 9")
        self.linkToGit.place(x=200, y=90, anchor="center")
        self.linkToGit.bind("<Button-1>", self.callback2)

        """  Purpose of the project 

        The purpose of the PMS is to use machine learning to predict when an engine needs maintenance based on the
        performance data provided by on-board sensors.

         """
        self.purposeTitle = Label(self.aboutWindow, text="Purpose:", fg="brown", font="fixedsys 9")
        self.purposeTitle.place(x=0, y=120, anchor="w")

        self.purpose1 = Label(self.aboutWindow, text="The purpose of the Predictive Maintenance System is to predict")
        self.purpose1.place(x=0, y=140, anchor="w")
        self.purpose2 = Label(self.aboutWindow, text="whether or not a aircraft engine needs maintenance. It uses the")
        self.purpose2.place(x=0, y=160, anchor="w")
        self.purpose3 = Label(self.aboutWindow, text="K-Nearest Neighbor (KNN) Machine Learning algorithm.")
        self.purpose3.place(x=0, y=180, anchor="w")

        self.instructions = Label(self.aboutWindow, text="Instructions:", fg="brown")
        self.instructions.config(bg="#EEF4EB", font="fixedsys 9")
        self.instructions.place(x=0, y=210, anchor="w")

        self.firstInstruction = Label(self.aboutWindow, text="1. Click on the \"Browse & Run\" button")
        self.firstInstruction.place(x=0, y=230, anchor="w")

        self.secondInstruction = Label(self.aboutWindow,
                                       text="2. Once the file explorer pops up, select your .CSV file to test")
        self.secondInstruction.place(x=0, y=250, anchor="w")

        self.thirdInstruction = Label(self.aboutWindow,
                                      text="3. Wait for the program to finish. The output will be shown")
        self.thirdInstruction.place(x=0, y=270, anchor="w")

        self.thirdContinued = Label(self.aboutWindow, text="under the \"Browse & Run\" button")
        self.thirdContinued.place(x=12, y=290, anchor="w")

        self.teamMembers = Label(self.aboutWindow, text="Team Ostriches:", font="fixedsys 9", fg="brown")
        self.teamMembers.place(x=0, y=320, anchor="w")

        self.productOwner = Label(self.aboutWindow, text="Product Owner: Craig Wert")
        self.productOwner.place(x=0, y=340, anchor="w")

        self.scrumMaster = Label(self.aboutWindow, text="Scrum Master: John Stranahan")
        self.scrumMaster.place(x=0, y=360, anchor="w")

        self.devTeam1 = Label(self.aboutWindow, text="Dev Team: Michael Matthews")
        self.devTeam1.place(x=0, y=380, anchor="w")

        self.devTeam2 = Label(self.aboutWindow, text="Dev Team: Tapan Soni")
        self.devTeam2.place(x=0, y=400, anchor="w")

        self.devTeam3 = Label(self.aboutWindow, text="Dev Team: Joshua Jackson")
        self.devTeam3.place(x=0, y=420, anchor="w")

        self.devTeam4 = Label(self.aboutWindow, text="Dev Team: Nicholas La Sala")
        self.devTeam4.place(x=0, y=440, anchor="w")

        self.sponsor = Label(self.aboutWindow, text="Sponsors: ", font="fixedsys 9", fg="brown")
        self.sponsor.place(x=0, y=470, anchor="w")

        self.sponsor1 = Label(self.aboutWindow, text="1. Mike Berenato")
        self.sponsor1.place(x=0, y=490, anchor="w")

        self.sponsor2 = Label(self.aboutWindow, text="2. Rukan Shao")
        self.sponsor2.place(x=0, y=510, anchor="w")

        self.sponsor3 = Label(self.aboutWindow, text="3. Anuradha Bhat")
        self.sponsor3.place(x=0, y=530, anchor="w")

    def callback(self, event):
        webbrowser.open_new(r"https://www.dropbox.com/sh/ettb3cckfm3aus6/AABewPX7pRlnAXokqGAYM414a?dl=0")

    def callback2(self, event):
        webbrowser.open_new("https://github.com/TapanSoni/SoftwareEngineeringFinalProject")

    def selectPredict(self):
        self.selection = 0
        print(self.selection)

    def selectTrain(self):
        self.selection = 1
        print(self.selection)

    def trainOrPredict(self):
        if self.selection == 0:
            self.bandr()
        else:
            self.trainingAlgo()

    # Predicting GUI
    def bandr(self):
        print("Hello World!")

        # Start the count
        self.startTime = time.time()

        # Take in input
        self.fileName = filedialog.askopenfilename(filetypes=(("CSV files", ".csv"), ("All files", "*.*")))
        print(self.fileName)
        self.fileNameDisplay.config(text= self.fileName)

        # Inside a Try/Except block to catch the IO Error thrown when
        # no file is selected - fixed the bug
        try:
            self.testData = np.genfromtxt(self.fileName, delimiter = ",")

            print("Data imported")

            # Start the timer for the classifier
            self.timeForClassifier = time.time()

            self.average = 0

            # Open the input file - the pickled classifier
            self.pkl_file = open('classy.pkl', 'rb')

            # Unpickle the pickled classifier
            self.classy = pickle.load(self.pkl_file)

            for self.index in range(0, len(self.testData)):
                self.average += self.classy.predict([self.testData[self.index]])

            self.average = self.average / len(self.testData)

            print("Average: ", self.average)

            # Compute the time for the classifier
            self.timeForClassifier = time.time() - self.timeForClassifier

            if self.average < .5:
                self.outputConsole.config(text = "No - Everything is OK")
            else:
                self.outputConsole.config(text = "Yes - Maintenance needed")

            self.totalTime = time.time() - self.startTime
            print("********* %s seconds *********" % self.totalTime)
            self.timestampC.config(text="Classifier Run Time: %s seconds" % self.timeForClassifier)
            self.timestamp.config(text="  Total Time Elapsed: %s seconds" % self.totalTime)
        except IOError:
            print("No file selected")
            # self.outputConsole.config(text = "No file selected")
            # self.timestampC.config(text = "Classifier Run Time: %s seconds" % 0)
            # self.timestamp.config(text = "Total Time Elapsed: %s seconds" % 0)


    # Training GUI:
    def trainingAlgo(self):
        print("Goodbye World!")


if __name__ == '__main__':
    root = Tk()
    lf = loginGUI(root)
    root.mainloop()