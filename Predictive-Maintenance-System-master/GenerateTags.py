import math

def generate(percentage,datasize):
    tags = []
    for i in range(0, math.floor(percentage * datasize)): #making the first 70% of tags 0
        tags.append(0)
    for i in range(0, datasize - math.floor(datasize * percentage)): #making the rest of the tagging array which will all be '1'
        tags.append(1)
    return tags
