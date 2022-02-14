import os
from os.path import abspath
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn import svm
#import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
#from sklearn.externals import joblib
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


x_train = np.load('output/pairwise/x_train.npy')
y_train = np.load('output/pairwise/y_train.npy')

x_val = np.load('output/pairwise/x_val.npy')
y_val = np.load('output/pairwise/y_val.npy')

print(x_train.shape)
print(y_train.shape)
print(x_val.shape)
print(y_val.shape)
#print(x_test.shape)
#print(y_test.shape)

x_train = np.concatenate((x_train, x_val), axis=1)
y_train = np.concatenate((y_train, y_val), axis=1)

x_test = np.load('output/pairwise/x_test.npy')
y_test = np.load('output/pairwise/y_test.npy')

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

x_train = np.swapaxes(x_train, 0, 1)
x_test = np.swapaxes(x_test, 0, 1)

x_train = x_train.reshape(4680, -1)
#x_train = np.mean(x_train, axis=0)
y_train = y_train[0]
x_test = x_test.reshape(1620, -1)
#x_test = np.mean(x_test, axis=0)
y_test = y_test[0]

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

svm_clas1 = svm.SVC(kernel='linear', C=0.01)
svm_clas1.fit(x_train, y_train) 
y_pred = svm_clas1.predict(x_test)
print("Accuracy: ",metrics.accuracy_score(y_test, y_pred)*100,"%")

