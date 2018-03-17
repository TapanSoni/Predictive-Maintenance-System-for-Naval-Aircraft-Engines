#Goes through dataset looking for column averages, mins, maxs, and Standard Deviation

min = []
max = []

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
