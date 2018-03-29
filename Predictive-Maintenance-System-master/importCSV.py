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

#Written by Michael Matthews
#Reads in dataset as an array.
#Must have numpy installed to run

import numpy as np

def readIn(filePath):
    return np.genfromtxt(filePath, delimiter='\t') #File path for file you'd like to import
