import param

class ubcf:
    def usersim(self,data,x,y):
        return 1 - scipy.spatial.distance.cosine(x,y)

    def recommend_calc(self,data):
        for u,i in data.Matrix.items():
            for item,rate in data.Matrix[u].items():
                print rate


if __name__=="__main__":
    data = param.parameter(5,5)
    data.get_sample()
    print data.Matrix

