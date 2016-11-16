from LoadData import *
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.externals import joblib
from WriteResults import *

"""
This module is always available. It provides access to the
RandomForest classifier.
"""

def randomForest(path):
    """
    RandomForest
    :return: void, save model
    """
    #load train data
    train_data = load_train_data()
    #load test data
    test_data = load_test_data()

    print("bla")
    #define specific random forest classifier
    clf = ExtraTreesClassifier(n_estimators=200, max_depth=None, min_samples_split=2, random_state=0)
    print("Juhej")
    scores = cross_val_score(clf, train_data[:, 1:], train_data[:, 0])
    #fit model
    clf.fit(train_data[:, 1:],train_data[:,0])
    #predict results
    y_pred = clf.predict(test_data)

    #save mode
    joblib.dump(clf, path) #../Models/RandomForestModel.pkl'

    #wirte predicted results in file
    write_csv("RandomForestSubmision", y_pred)

randomForest("../Models/RandomForestModel.pkl")












