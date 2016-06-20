import random

class parameter:
    def __init__(self,user,item):
        self.num_user = user
        self.num_item = item
        self.Matrix = {}
        self.userSim = {}

    def get_sample(self):
        for u in range(self.num_user):
            for i in range(self.num_item):
                self.Matrix[u] = {}
                self.Matrix[u][i] = float(random.randint(0,5))


