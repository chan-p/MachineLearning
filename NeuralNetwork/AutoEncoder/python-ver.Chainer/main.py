# -*- coding: utf-8 -*-
import test
import auto_encoder

if __name__=="__main__":
    # アイテム数
    item = 50
    # 入力次元数
    num_input = 200
    # テストケース生成
    testcase = test.MULTI_CLASS()
    x = testcase.run_onehot(item,num_input)

    # 隠れ層のユニット数
    num_hidden = 100
    # イテレーション回数
    iteration = 5000
    neural = auto_encoder.NeuralNet(num_input,num_hidden,x,iteration,"Denoise")
    neural.run()
    neural.Answer_check()
    neural.check_state()
