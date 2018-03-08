#Generates new data randomly based upon lower bound and maxium bound on actual data set
#note this algorithm can be imporved in the followin ways
    #have stages of data that its based upon for the example since the engine is deterioting the frist 10% will look different than the second 10% etc.
    #possibly do somthing with averages and standard deviation

#Todo: when generating new data feature that columns that were only ints in real data set will only be ints in generated data set
# program can run more efficently by
#    1.) parralizing reading of the dataset
#    2.) exporting and importing generated random dataset, columns avgs. etc so it doesn't have to be everytime the progarm is run

import numpy as np
import random
import math

def generate(min, max,size):
    new_data_set = np.zeros((size, 30))

    for x in range(0,30):
        row = []

        for y in range(0,size):
            if(x==0):
                got_a_number = False
                while(not got_a_number):
                    number = random.uniform(min[x],max[x])
                    if (not math.floor(number)==5):
                        got_a_number = True
                        new_data_set[y][x] = number
            else:
                new_data_set[y][x] = random.uniform(min[x], max[x])

    return new_data_set