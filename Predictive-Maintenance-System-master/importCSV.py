#Written by Michael Matthews
#Reads in dataset as an array.
#Must have numpy installed to run

import numpy as np

def readIn(filePath):
    return np.genfromtxt(filePath, delimiter='\t') #File path for file you'd like to import
