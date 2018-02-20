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

import tkinter as tk

window = tk.Tk()
window.geometry("400x400")  # size of the window
window.title("Predictive Maintenance System")  # title of the window -- Predictive Maintenence System

# Label
title = tk.Label(text="Predictive Maintenance System", font=("Inconsolta", 18))
title.grid(column=1, row=0)

# Entry field
output1_field = tk.Text(master=window, height=1, width=40)
output1_field.grid(column=1, row=4)

# File browse button this upload CSV file
fileButton = tk.Button(text="Browse", bg="yellow")
fileButton.grid(column=2, row=4)

# File Run button this will run the application
fileButton_2 = tk.Button(text="Run", bg="green")
fileButton_2.grid(column=1, row=8)

# Output field
output2_field = tk.Text(master=window, height=10, width=30)
output2_field.grid(column=1, row=16)

window.mainloop()
