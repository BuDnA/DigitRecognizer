from csv import DictReader
import collections
import numpy as np

"""
This module is always available. It provides access to the
load data functions.
"""

def load_train_data():
    """
    Load training data.
    :return: input data as numpy array
    """

    fp = open("../Files/train.csv", "rt")
    train = DictReader(fp)
    z = 0

    data = []
    for i in fp:
        if(z == 0):
            z+=1
            continue
        data.append(map(float, i.split(",")))
        #Yy.append(map(int, i.split(",")[0]))
        z += 1

    #return np.array(data)
    return np.round((np.array(data) / 255)*256)



#function which load testing data and return as numpy array
def load_test_data():
    fp = open("../Files/test.csv", "rt")
    train = DictReader(fp)
    z = 0

    data = []
    for i in fp:
        if(z == 0):
            z+=1
            continue
        data.append(map(float, i.split(",")))
        z += 1

    #return np.array(data)
    return np.round((np.array(data) / 255)*256)
