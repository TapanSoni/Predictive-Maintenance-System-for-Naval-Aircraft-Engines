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
 This is the importCSV.py file. It is responsible for taking in the .CSV
 file and assigning it to a variable.

 Last edit: 4/1/18 @ 2:26 PM by Tapan Soni


-----------------------------------------------------------------------------
"""

#Written by Michael Matthews
#Reads in dataset as an array.
#Must have numpy installed to run

import numpy as np

#takes in the CSV to obtain the data
#=============================================================================================================
def readIn(filePath):
    return np.genfromtxt(filePath, delimiter='\t') #File path for file you'd like to import
#=============================================================================================================