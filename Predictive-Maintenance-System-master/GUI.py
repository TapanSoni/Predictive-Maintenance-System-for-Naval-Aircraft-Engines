# # Tutorial  2 -- Organizing the Layout
# import tkinter
# from tkinter import *
#
# root = tkinter.Tk()  # Main window
#
# # Frame -- Invisible rectangle that can be a basic layout to put things into -- goes into
# # the main window of the root
# topFrame = Frame(root)
#
# topFrame.pack()
#
# # Bottom frame
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# # Param1: Where do you want to put it
# # Param2: What do you want the button to say
# # Param3: fg --> Color of the text, not the button
# testButton1 = Button(topFrame,    text="Test 1", fg="red")
# testButton2 = Button(topFrame,    text="Test 2", fg="green")
# testButton3 = Button(topFrame,    text="Test 3", fg="blue")
# testButton4 = Button(bottomFrame, text="Test 4", fg="purple")
#
# # Nothing is going to display if you ran the program right now
# # We have to tell the program to display them
#
# # So tell the program to display the buttons on the screen
# # Pack has parameters
# # side=LEFT makes sure that the buttons are place to the far left as
# # possible. Put it as far left as possible
# testButton1.pack(side=LEFT)
# testButton2.pack(side=LEFT)
# testButton3.pack(side=LEFT)
# testButton4.pack(side=LEFT)
#
# # Constant loop, therefore it's always visible until the user closes it
# root.mainloop()

# # Tutorial 3 - Fitting Widgets in your Layout
# import tkinter
# from tkinter import *
#
# root = tkinter.Tk()
#
# # Background color and foreground color (font color) can be changed for labels
# one = Label(root, text = "1", bg = "red", fg = "white")
# one.pack()
# two = Label(root, text = "2", bg = "green", fg = "black")
#
# # New param -- Fill X means -- Fill the label to the X value of the parent (in this case, the whole root X value)
# # Fills the widget as wide as the parent
# two.pack(fill=X)
#
# three = Label(root, text = "3", bg = "blue", fg = "yellow")
#
# # Puts it on the left hand side and fills the Y value of that "div" -- under the two label
# # Also it's relative, so if you change the size of the window, they will grow dynamically with the window size change
# three.pack(side=LEFT,fill=X)
#
# root.mainloop()

# import tkinter
# from tkinter import *
#
# root = tkinter.Tk()
#
# root.geometry("480x500")
#
# root.title("Predictive Maintenance System")
#
# substituteLabelForFile = Label(root, text = "Sample", bg = "white", fg = "black")
#
# substituteLabelForFile.pack(side=LEFT)
#
#
# root.mainloop()


# label_1 = Label(window, text="Name")
# label_2 = Label(window, text="Password")
#
# entry_1 = Entry(window)
# entry_2 = Entry(window)
#
# label_1.grid(row=0, sticky=E) # Text prompt - stick parameter is right aligned or left aligned -- Takes param as N E S W
# label_2.grid(row=1, sticky=E) # Text prompt
#
# entry_1.grid(row=0, column=1) # Text entry
# entry_2.grid(row=1, column=1)# Text entry
#
# checkBox = Checkbutton(window, text="Keep me logged in")
# checkBox.grid(columnspan=2, sticky=W)
#
# window.mainloop()

# def printName(event):
#     print("Hello this is Darth Vader")
#
#
# # command -- param that says that when the button is clicked call this function - in this case, it's printName
# button_1 = Button(window, text="Print name")
# # <Button-1> is left mouse click
# button_1.bind("<Button-1>", printName) # Takes 2 param - 1) What event you are waiting on to occur, and 2) what function you want to call when that happens
# button_1.pack()
#
# window.mainloop()

#
# def leftClick(event):
#     print("Left")
#
#
# def rightClick(event):
#     print("Right")
#
#
# def midClick(event):
#     print("Middle")
#
#
# frame = Frame(window, width=350, height=400)
# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-2>", midClick)
# frame.bind("<Button-3>", rightClick)
#
# frame.grid()


# class SWENGButtons:
#
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#
#         self.printButton = Button(frame, text="Print message", command=self.printMessage)
#         self.printButton.pack(side=LEFT)
#
#         self.quitButton = Button(frame, text="Quit", command=frame.quit)
#         self.quitButton.pack(side=LEFT)
#
#     def printMessage(self):
#         print("WOW! This works!")
#
#
# window = tk.Tk()
# someObject = SWENGButtons(window)
# window.mainloop()


# import tkinter as tk
# from tkinter.filedialog import *
# from tkinter import *
#
# class GUI:
#
#     def __init__(self, masterWindow):
#         masterWindow.geometry("400x400")
#         masterWindow.title("Predictive Maintenance System")
#
#         # Everything will be added to the frame
#         frame = Frame(masterWindow)
#         frame.pack()
#
#         # GUI for asking for a file
#         self.getFileNameButton = Button(frame, text="Browse", side=LEFT, command=self.getFileInput)
#         self.getFileNameButton.grid(row=0, column=0, sticky=E)
#
#     def getFileInput(self):
#         self.directory = askdirectory()
#         print(self.directory)
#
#
# masterWindow = tk.Tk()
# someObject = GUI(masterWindow)
# masterWindow.mainloop()


# window = tk.Tk()
# window.geometry("400x300")  # size of the window
# window.title("Predictive Maintenance System")  # title of the window -- Predictive Maintenence System
#
# # Label
# title = tk.Label(text="Predictive Maintenance System", font=("Inconsolta", 18))
# title.grid(column=1, row=0)
#
# # Entry field
# output1_field = tk.Text(master=window, height=1, width=40)
# output1_field.grid(column=1, row=4)
#
# # File browse button this upload CSV file
# fileButton = tk.Button(text="Browse", bg="yellow")
# fileButton.grid(column=2, row=4)
#
#
# # File Run button this will run the application
# fileButton_2 = tk.Button(text="Run", bg="green")
# fileButton_2.grid(column=1, row=8)
#
# # Output field
# output2_field = tk.Text(master=window, height=10, width=30)
# output2_field.grid(column=1, row=16)
#
# window.mainloop()

from tkinter import *
from tkinter import filedialog

window = Tk()


def browseFile():
    window.fileName = filedialog.askopenfilename(filetypes=(("CSV files", ".csv"), ("All files", "*.*")))
    print(window.fileName)
    fileNameDisplay.config(text=window.fileName)


# Window configurations

window.geometry("350x150")
window.title("Predictive Maintenance System")
window.config(background="#EEF4EB")

# Entry field for the file
fileNamePrompt = Label(window, text="Input file")

# Entry field for output field
outputConsolePrompt = Label(window, text="Maintenance Needed (Yes or No)")

# File name entry window
fileNameDisplay = Label(window, bg="white", width="30")

# File name browse button
fileNameBrowseButton = Button(window, text="Browse", command=browseFile)
fileNameBrowseButton.config(background="#EDDEA4")

# Run button
runButton = Button(window, text="Run")
runButton.config(background="#79FF6D")

# Output console
outputConsole = Label(window, bg="white", width="30")

# Fake labels
fake_1 = Label(window)
fake_2 = Label(window)

fake_1.config(background="#EEF4EB")
fake_2.config(background="#EEF4EB")

# Gridding the widgets in the window using grid

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