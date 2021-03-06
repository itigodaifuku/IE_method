import cv2
import gzip
import argparse
import numpy as np
import os
import random
import pickle
import copy
import chainer
from chainer.datasets import tuple_dataset
from sklearn.datasets import load_iris
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


def make2class(data, class0, class1):
    image = [] # x
    label = []
    dataset = copy.deepcopy(data) # 参照渡し -> train_allの上書き防止
    for dt in dataset:
        img = dt[0]
        lbl = dt[1]
        if lbl in class0 or lbl in class1:
            if lbl in class0:
                label.append(0)
                image.append(img)
            elif lbl in class1:
                label.append(1)
                image.append(img)
    return chainer.datasets.TupleDataset(image, label)



def shuffle(data1, data2):
    shuffle_data1 = data1
    shuffle_data2 = data2
    random.shuffle(shuffle_data1)
    random.shuffle(shuffle_data2)

    train = data1
    test = data2
    return train, test

def load_data(data, gpu_id):
    if gpu_id == 0:
        datapath = ''
    else:
        datapath = './data/'
    if data == 'mnist':
        with open('./data/mnist/mnist.pkl', mode="rb") as f:
            train_all, test_all = pickle.load(f)
        
        
        # # debug
        # train_all = train_all[1:1000]
        # test_all = test_all[1:1000] 


        train = []

        print("- train1" , flush = True, end="")
        train.append(make2class(train_all, [0], [1]))  # task1's train data
        print("_num: {}".format(len(train[1])))

        print("- train2", flush = True, end="")
        train.append(make2class(train_all, [0], [2]))  # task2's train data
        print("_num: {}".format(len(train[2])))

        print("- train3", flush = True, end="")
        train.append(make2class(train_all, [0], [3]))  # task0's train data
        print("_num: {}".format(len(train[3])))
         
        print("- train4", flush = True, end="")
        train.append(make2class(train_all, [0], [4]))  # task1's train data
        print("_num: {}".format(len(train[4])))

        print("- train5", flush = True, end="")
        train.append(make2class(train_all, [0], [5]))  # task2's train data
        print("_num: {}".format(len(train[5])))

        print("- train6", flush = True, end="")
        train.append(make2class(train_all, [0], [6]))  # task0's train data
        print("_num: {}".format(len(train[6])))
       
        print("- train7", flush = True, end="")
        train.append(make2class(train_all, [0], [7]))  # task1's train data
        print("_num: {}".format(len(train[7])))

        print("- train8", flush = True, end="")
        train.append(make2class(train_all, [0], [8]))  # task2's train data
        print("_num: {}".format(len(train[8])))

        print("- train9", flush = True, end="")
        train.append(make2class(train_all, [0], [9]))  # task2's train data
        print("_num: {}".format(len(train[9])))



        test = []
        
        print("- test1", flush = True, end="")
        test.append(make2class(test_all, [0], [1]))  # task1's test data
        print("_num: {}".format(len(test[1])))

        print("- test2", flush = True, end="")
        test.append(make2class(test_all, [0], [2]))  # task2's test data
        print("_num: {}".format(len(test[2])))

        print("- test3", flush = True, end="")
        test.append(make2class(test_all, [0], [3]))  # task0's test data
        print("_num: {}".format(len(test[3])))
         
        print("- test4", flush = True, end="")
        test.append(make2class(test_all, [0], [4]))  # task1's test data
        print("_num: {}".format(len(test[4])))

        print("- test5", flush = True, end="")
        test.append(make2class(test_all, [0], [5]))  # task2's test data
        print("_num: {}".format(len(test[5])))

        print("- test6", flush = True, end="")
        test.append(make2class(test_all, [0], [6]))  # task0's test data
        print("_num: {}".format(len(test[6])))
       
        print("- test7", flush = True, end="")
        test.append(make2class(test_all, [0], [7]))  # task1's test data
        print("_num: {}".format(len(test[7])))

        print("- test8", flush = True, end="")
        test.append(make2class(test_all, [0], [8]))  # task2's test data
        print("_num: {}".format(len(test[8])))

        print("- test9", flush = True, end="")
        test.append(make2class(test_all, [0], [9]))  # task2's test data
        print("_num: {}".format(len(test[9])))

        pkl_data = []
        pkl_data.append(train)
        pkl_data.append(test)
        pickle.dump(pkl_data, open("mnist_2class.pkl", "wb"), -1)

        return train, test