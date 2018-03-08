#goes through dataset looking for column averages, mins, maxs, and Standard Deviation
#also it will tell you which columns have exactly the same data

import numpy as np

min = []
max = []

class FindMinAndMax:

    def __init__(self,data):
        self.data = data
        self.main()

    def main(self):
        for column in range(0, 30):
            # column = 1
            temp = self.data [0][column]
            temp_min = self.data [0][column]

            flag = False

            for x in range(1, len(self.data)):
                current = self.data [x][column]
                if (current > temp):
                    temp = current
                if (current < temp_min):
                    temp_min = current
                if (current == self.data [(x + 1) % len(self.data)][column]):
                    flag = True
                else:
                    flag = False

            if (flag == True):
                print('Column: ', column, '\n&olumn', column + 1)

            max.append(temp)
            min.append(temp_min)
            # print('Max:',temp)
            # print('Min: ',temp_min)
            # print(avg/(whole_data_set.size/30))

            # print('Range: ', temp - temp_min)
            # print('SD: ',np.std(whole_data_set[:,column]))
            # print('Var: ',np.var(whole_data_set[:,column]))
            # print('Avg: ',np.mean(whole_data_set[:,column]))

    @staticmethod
    def getMax():
        return max

    @staticmethod
    def getMin():
        return min
