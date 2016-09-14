import random

def makedata():
    vec = [0 for i in range(13)]
    sex = random.randint(0,1)
    vec[sex] = 1
    flame = random.randint(1,4)
    vec[sex+flame] = 1
    site_content = random.randint(1,6)
    vec[sex+flame+site_content] = 1
    return vec


if __name__=="__main__":
    f = open("DB/db.csv","w")
    for i in range(50):
        vec = makedata()
        count=0
        for j in vec:
            f.write(str(j))
            if count != 12:
                f.write(",")
            count+=1
        f.write("\n")
    f.close()
