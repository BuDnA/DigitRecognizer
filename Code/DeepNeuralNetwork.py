################
#Neural network#
################
from LoadData import *
from nolearn.dbn import DBN
train_data = load_train_data()
test_data = load_test_data()

print(train_data)
exit(0)
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier


clf = DBN([train_data[:, 1:].shape[1], 300, 10], learn_rates = 0.3, learn_rate_decays = 0.9, epochs = 15)
scores = cross_val_score(clf, train_data[:, 1:], train_data[:, 0])
clf.fit(train_data[:, 1:],train_data[:,0])
y_pred = clf.predict(test_data)

#from sklearn.externals import joblib
#joblib.dump(clf, 'NeuralNetork.pkl')

import csv
with open('submision.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile,
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['ImageId'] + ['Label'])

    for i in range(len(y_pred)):
        spamwriter.writerow([i+1] + [y_pred[i]])

print(scores.mean())
#0.961952637866
#0.966571519031
#0.967

#from sklearn.datasets import make_hastie_10_2
#from sklearn.ensemble import GradientBoostingClassifier
#clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
#     max_depth=1, random_state=0).fit(X_train, y_train)
#clf.score(X, y)
