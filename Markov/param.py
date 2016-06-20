class Parameter:
    def __init__(self,User,Rec):
        self.ItemMap = {}
        self.pare = {}
        self.lastItem = [0 for i in range(User)]
        self.user_num = User
        self.Top_rec = [[-1 for i in range(Rec)]for j in range(User)]
        self.RecommendItem = Rec
