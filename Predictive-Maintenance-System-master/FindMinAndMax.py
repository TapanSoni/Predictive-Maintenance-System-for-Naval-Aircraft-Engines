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
 This is the FindMinAndMax.py file. It is responsible for going through e-
 ach of the columns or features and finding the min and max of each colum-
 n and the standard deviations of each of the features.

 Last edit: 4/1/18 @ 2:26 PM by Tapan Soni
-----------------------------------------------------------------------------
"""

#Goes through dataset looking for column averages, mins, maxs, and Standard Deviation

minOf = []
maxOf = []
#rangeOf = []

class FindMinAndMax:

    #The one parameter number for this function is the actual dataset
    def __init__(self,data):
        self.data = data
        self.main()

    def main(self):
        for column in range(0, 30):
            temp = self.data [0][column]
            temp_min = self.data [0][column]

            flag = False

            for x in range(1, len(self.data)):
                current = self.data [x][column]
                if (current > temp):
                    temp = current
                if (current < temp_min):
                    temp_min = current

            maxOf.append(temp)
            minOf.append(temp_min)

    # =============================================================================================================
    @staticmethod
    def getMax():
        return maxOf
    # =============================================================================================================

    # =============================================================================================================
    @staticmethod
    def getMin():
        return minOf
    # =============================================================================================================

    #@staticmethod
    #def getRan():
        #return rangeOf
