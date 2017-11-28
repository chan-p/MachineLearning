import codecs
from math import log
import time

NUM_FILES = 10
INPUT_FILENAMES = ['./input/{}.txt'.format(index) for index in range(NUM_FILES)]
OUTPUT_FILENAMES = ['./output/{}.txt'.format(index) for index in range(NUM_FILES)]
df_dic = {}

def count_up(value):
    return value + 1

def count_tf(index, file_name):
    tf_dic = {}
    global df_dic
    with open(file_name, 'r', encoding='MS932') as f:
        words = f.read()d
        for word in words.split('\n'):
            tf_dic[word] = count_up(tf_dic[word]) if word in tf_dic else 1
            if word not in df_dic:
                df_dic[word] = []
            df_dic[word].append(index)
    return tf_dic

def write(index, file_name, tf):
    with open(file_name, 'w') as f:
        for target_word in tf.keys():
            f.write('{0}    {1}\n'.format(target_word, tf[target_word]*log(NUM_FILES/len(set(df_dic[target_word])))))

def run():
    tf_list = [count_tf(index, file_name) for index, file_name in enumerate(INPUT_FILENAMES)]
    for index, tf in enumerate(tf_list):
        write(index, OUTPUT_FILENAMES[index], tf_list[index])

if __name__=='__main__':
    start = time.time()
    run()
    print('{}sec'.format(time.time()-start))
