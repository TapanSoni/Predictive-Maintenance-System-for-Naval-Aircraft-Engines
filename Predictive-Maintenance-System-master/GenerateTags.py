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
 This is the GenerateTags.py file. It is responsible for generating the t-
 ags for each line of data. It does this by assigning the top 70% of the
 data to a 0, meaning, no maintenance required, and the bottom 30% to a 1,
 meaining, maintenance is required for these factors derived from the feat-
 ures.

 Last edit: 4/1/18 @ 2:26 PM by Tapan Soni


-----------------------------------------------------------------------------
"""

import math

#Generate takes two parameters the first is the percentage you want to have the value of 0
#and the second is the size of the dataset
#returns the generated tags as an array
def generate(percentage,datasize):
    tags = []
    for i in range(0, math.floor(percentage * datasize)): #making the first 70% of tags 0
        tags.append(0)
    for i in range(0, datasize - math.floor(datasize * percentage)): #making the rest of the tagging array which will all be '1'
        tags.append(1)
    return tags
