import param

class Markov:
    def count(self,data):
        for k,v in data.pare.items():
            co = 0
            if k not in data.ItemMap:
                data.ItemMap[k] = {}
            for n,m in data.pare[k].items():
                co += m 
            for n,m in data.pare[k].items(): 
                data.ItemMap[k][n] = float(m)/float(co)

    def set(self,Iset,data,user):
        for i in range(1,len(Iset)):
            if Iset[i-1] not in data.pare:
                data.pare[Iset[i-1]] = {}
            if Iset[i] not in data.pare[Iset[i-1]]:
                data.pare[Iset[i-1]][Iset[i]] = 1
            else:
                data.pare[Iset[i-1]][Iset[i]] += 1 
            data.lastItem[user] = Iset[i]

    def sort(self,data):
        for user in range(data.user_num):
            count = 0
            if data.lastItem[user] in data.ItemMap:
                for item,rec in sorted(data.ItemMap[data.lastItem[user]].items(),key=lambda x:x[1],reverse=True):
                    data.Top_rec[user][count] = item
                    count += 1
                    if count == 20:
                        break

def input(file,markov,data):
    User_list = [0]
    Iset = []
    f = open(file,"r")
    for line in f:
        Udata = line.split(",")
        user = int(Udata[0])
        if int(Udata[0]) not in User_list:
            markov.set(Iset,data,user-1)
            User_list.append(int(Udata[0]))
            Iset = []
            Iset.append(int(Udata[1]))
        else:
            Iset.append(int(Udata[1]))
    f.close()
    markov.count(data)

def output(file,data):
    for user in range(data.user_num):
        f = open(file + str(user) + ".csv","w")
        for rec in range(data.RecommendItem):
            f.write(str(data.Top_rec[user][rec]))
            if rec != (data.RecommendItem-1):
                f.write(",")
        f.close()



if __name__=="__main__":
    file = "/Users/TomonotiHayshi/Desktop/GDrive/TrainData1781re/learning1997sort.csv"
    file2 = "/Users/TomonotiHayshi/Desktop/GDrive/TrainData1781/Result1781/Markov/Markov_Top20/"
    markov = Markov()
    data = param.Parameter(1998,20)
    input(file,markov,data)
    markov.sort(data)
    output(file2,data)
