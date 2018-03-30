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

This is the graphical user interface for the Predictive Maintenance System.
It has an input field for the source file (.csv) file, and a run button
which runs the source file through the predictive algorithm and then
it prints out either a "Yes" or a "No" in the output console window.
"Yes" if the aircraft engine needs maintenance, and "No", if the aircraft
engine doesn't need maintenance.

-----------------------------------------------------------------------------
"""

# Imports
from tkinter import *
from tkinter import filedialog

selection = -1
runClicked = 0

"""
This is the browsefile() function. It is activated when the 
user presses the button "Browse" and it brings up the File
Explorer where the user can select the source file
"""
def browsefile():
    window.fileName = filedialog.askopenfilename(filetypes=( ("txt files", ".txt"), ("CSV files", ".csv"), ("All files", "*.*")))
    print(window.fileName)
    fileNameDisplay.config(text=window.fileName)


def clickKN():
    kn.config(bg="orange")
    dt.config(bg="#F0F0F0")
    lsvc.config(bg="#F0F0F0")
    classifierConsole.config(text="K-Nearest Neighbor SELECTED")
    selection = 1
    print(selection)


def clickDT():
    kn.config(bg="#F0F0F0")
    dt.config(bg="orange")
    lsvc.config(bg="#F0F0F0")
    classifierConsole.config(text="Decision Tree SELECTED")
    selection = 2
    print(selection)


def clickLSVC():
    kn.config(bg="#F0F0F0")
    dt.config(bg="#F0F0F0")
    lsvc.config(bg="orange")
    classifierConsole.config(text="Linear SVC SELECTED")
    selection = 3
    print(selection)


def clickRun():
    runClicked = 1
    print(runClicked)


# Creating the main window
window = Tk()

# Changed the icon to the Rowan University Logo
window.iconbitmap(r'RowanLogo.ico')

# Window configurations
window.geometry("370x300")
window.title("Predictive Maintenance System")

# Entry field for the file
fileNamePrompt = Label(window, text="Source")

# Entry field for output field
outputConsolePrompt = Label(window, text="Maintenance Needed (Yes or No)")

# File name entry window
fileNameDisplay = Label(window, bg="white", width="30")

# File name browse button
fileNameBrowseButton = Button(window, text="Browse", command=browsefile)

# Run button
runButton = Button(window, text="Run", command=clickRun)

# Output console
outputConsole = Label(window, bg="white", width="30")

# Classifier console output

classifierConsole = Label(window, bg="white", width="30")

# KNeighbor Selection Button
kn = Button(window, text="K-Neighbor", width=10, command=clickKN)

# Decision Tree selection button
dt = Button(window, text="Decision Tree", width=10, command=clickDT)

# Linear SVC selection button
lsvc = Button(window, text="Linear SVC", width=10, command=clickLSVC)

# Fake labels for positioning th other widgets correctly
fake_1 = Label(window)
fake_2 = Label(window)
fake_3 = Label(window)

# Configurations of the widgets
fileNamePrompt.config(font="fixedsys 9")
window.config(background="#EEF4EB")
outputConsolePrompt.config(font="fixedsys 9")
fileNameBrowseButton.config(background="#EDDEA4", font="fixedsys 9")
runButton.config(background="#79FF6D", font="fixedsys 9")
kn.config(font="fixedsys 9")
lsvc.config(font="fixedsys 9")
dt.config(font="fixedsys 9")
fake_1.config(background="#EEF4EB")
fake_2.config(background="#EEF4EB")

# Giving position to the widgets and telling them to fill the area if resized
fileNamePrompt.grid(row=0, column=0, sticky=NSEW)
fileNameDisplay.grid(row=0, column=1, sticky=NSEW)
fileNameBrowseButton.grid(row=0, column=2, sticky=NSEW)
fake_1.grid(row=1, sticky=NSEW)

# Classifiers
kn.grid(row=2, column=1, sticky=NSEW)
dt.grid(row=3, column=1, stick=NSEW)
lsvc.grid(row=4, column=1, sticky=NSEW)

fake_3.grid(row=5, sticky=NSEW)
classifierConsole.grid(row=6, column=1, sticky=NSEW)
fake_2.grid(row=7, sticky=NSEW)
runButton.grid(row=8, column=1, sticky=NSEW)
outputConsolePrompt.grid(row=9, column=1, sticky=NSEW)
outputConsole.grid(row=10, column=1, sticky=NSEW)

# The widgets will fill with the parent
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(6, weight=1)
window.grid_rowconfigure(7, weight=1)
window.grid_rowconfigure(8, weight=1)
window.grid_rowconfigure(9, weight=1)
window.grid_rowconfigure(10, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()

# END GUI.py