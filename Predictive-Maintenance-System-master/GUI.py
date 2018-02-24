"""
-----------------------------------------------------------------------------

Rowan Computer Science Dept Spring 2018 Software Engineering Team Ostriches
Predictive Maintenance System for ASRC Federal Mission Solutions Engineering

Team Ostriches Members:
Product Owner:  Craig Wert
Scrum Master:   John Stranahan
Developer:      Tapan Soni
Developer:      Michael Matthews
Developer:      Joshua Jackson
Developer:      Nicholas La Sala

-----------------------------------------------------------------------------

Description:
This is the graphical user interface for the Predictive Maintenance System.
It has an input field for the source file (.csv) file, and a run button
which runs the source file through the predictive algorithm and then
it prints out either a "Yes" or a "No" in the output console window.
"Yes" if the aircraft engine needs maintenance, and "No", if the aircraft
engine doesn't need maintenance.

-----------------------------------------------------------------------------

Manual:
To use this program, launch the program. Next, use the browse button, by
clicking on it, to select the source file. It has to be a .csv file. After
that, click the run button, and then the program will do some magic behind
the scenes, and output either a "Yes" for yes - the engine needs maintenance,
or "No" for no - the engine doesn't need maintenance.

-----------------------------------------------------------------------------
"""

# Imports
from tkinter import *
from tkinter import filedialog

"""
This is the browsefile() function. It is activated when the 
user presses the button "Browse" and it brings up the File
Explorer where the user can select the source file
"""
def browsefile():
    window.fileName = filedialog.askopenfilename(filetypes=(("CSV files", ".csv"), ("All files", "*.*")))
    print(window.fileName)
    fileNameDisplay.config(text=window.fileName)


# Creating the main window
window = Tk()

# Changed the icon to the Rowan University Logo
window.iconbitmap(
    r'C:\Users\Tapan\PycharmProjects\SoftwareEngineeringFinalProject\Predictive-Maintenance-System-master\RowanLogo.ico')

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
runButton = Button(window, text="Run")

# Output console
outputConsole = Label(window, bg="white", width="30")

# Fake labels for positioning th other widgets correctly
fake_1 = Label(window)
fake_2 = Label(window)

# Configurations of the widgets
fileNamePrompt.config(font="fixedsys 9")
window.config(background="#EEF4EB")
outputConsolePrompt.config(font="fixedsys 9")
fileNameBrowseButton.config(background="#EDDEA4", font="fixedsys 9")
runButton.config(background="#79FF6D", font="fixedsys 9")
fake_1.config(background="#EEF4EB")
fake_2.config(background="#EEF4EB")

# Giving position to the widgets and telling them to fill the area if resized
fileNamePrompt.grid(row=0, column=0, sticky=NSEW)
fileNameDisplay.grid(row=0, column=1, sticky=NSEW)
fileNameBrowseButton.grid(row=0, column=2, sticky=NSEW)
fake_1.grid(row=1, sticky=NSEW)
runButton.grid(row=2, column=1, sticky=NSEW)
fake_2.grid(row=3, sticky=NSEW)
outputConsolePrompt.grid(row=4, column=1, sticky=NSEW)
outputConsole.grid(row=5, column=1, sticky=NSEW)

# The widgets will fill with the parent
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()

# END GUI.py
