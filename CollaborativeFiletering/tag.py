import random

f = open("/Users/TomonotiHayshi/GitHub/MachineLearning/CollaborativeFiletering/topic.csv")


for j in range(5000):
    have = []
    for i in range(10):
        have.append(random.randint(0,9998))
    for l in range(1000):
        if l in have:
            f.write(1,)
