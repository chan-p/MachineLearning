import random
import numpy as np

class Parameter:
  def __init__(self,User = 5,Item = 5,K = 3):
    #Generate init RateMatrix
    self.RateMatrix = [[0 for i in range(Item)] for j in range(User)]
    #Generate init Decomposing Matrix
    self.UserMatrix = [[random.random() for i in range(K)] for j in range(User)]
    self.UserMatrix = np.matrix(self.UserMatrix)
    self.ItemMatrix = [[random.random() for i in range(Item)] for j in range(K)]
    self.ItemMatrix = np.matrix(self.ItemMatrix)
    #BaseData
    self.Num_User = User
    self.Num_Item = Item
    self.Num_K = K

  def get_sample(self):
    Mat = np.matrix(self.RateMatrix)
    self.RateMatrix =[[int(random.random()*10) for i in range(Mat.shape[1])] for j in range(Mat.shape[0])]
    print np.matrix(self.RateMatrix)
