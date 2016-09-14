import  random

if __name__=="__main__":

    f = open("/Users/TomonotiHayshi/GitHub/MachineLearning/CollaborativeFiletering/sim.csv","w")

    for i in range(5000):
        f.write(str(random.random()))
        if i != 4999:
            f.write(",")
