import random
import math

class ubcf:
    def __init__(self,user,item,matrix):
        self.num_user = user
        self.num_item = item
        self.Matrix = matrix
        self.all_ave = {}

    def __up(self,A_user,O_user):
        Sum = 0.0
        for item,rate in self.Matrix[A_user].items():
            if item in self.Matrix[O_user]:
                Sum += self.Matrix[A_user][item] * self.Matrix[O_user][item]
        return Sum

    def __bottom(self,user):
        sum = 0.0
        for item,rate in self.Matrix[user].items():
                sum += math.pow(rate,2)
        return math.sqrt(sum)

    def __cosineSim(self,A_user,O_user):
        return self.__up(A_user,O_user)/(self.__bottom(A_user) * self.__bottom(O_user))

    def __Similarity_calc(self,A_user):
        for O_user in range(self.num_user):
            if A_user == O_user:
                continue
            self.userSim[O_user] = self.__cosineSim(A_user,O_user)
            print self.userSim[O_user]

    def __All_Average(self):
        for A_user in range(self.num_user):
            Sum = 0.0
            for item,rate in self.Matrix[A_user].items():
                Sum += rate
            self.all_ave[A_user] = Sum/len(self.Matrix[A_user])

    def __predict(self,A_user,item):
        up = 0.0
        bottom = 0.0
        for O_user in range(self.num_user):
            if O_user != A_user and item in self.Matrix[O_user]:
                up += self.userSim[O_user] * (self.Matrix[O_user][item] - self.all_ave[O_user])
                bottom += self.userSim[O_user]

        return self.all_ave[A_user] + (up/bottom)

    def recommend_calc(self,A_user):
        for item in range(self.num_item):
            if item not in self.Matrix[A_user]:
                self.recommendList[item] = self.__predict(A_user,item)

    def run(self):
        self.__All_Average()
        for user in range(self.num_user):
            self.userSim = {}
            self.recommendList = {}

            print "User:" + str(user)
            self.__Similarity_calc(user)
            self.recommend_calc(user)
            print self.recommendList

if __name__=="__main__":
    test = {}
    user = 5
    item = 5
    for i in range(user):
        test[i] = {}
        print "User:" + str(i)
        for j in range(item):
            test[i][j] = random.randint(1,5)
        del(test[i][random.randint(0,item-1)])
        print test[i]

    cf = ubcf(user,item,test)
    cf.run()
