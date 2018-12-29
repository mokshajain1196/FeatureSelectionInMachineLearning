import csv
import numpy as np
import matplotlib as plt
import pandas as pd
import seaborn as sb
from sklearn import datasets
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LassoCV
from sklearn.linear_model import Lasso,Ridge
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
dataL = pd.read_csv('E:\Bachelor Thesis\TestLasso\Cars.csv', delimiter=';')
#iris = datasets.load_iris()
#X= iris['data']
#print(X)
#Set Formation
X = np.array(dataL[:])
colNo=len(X[0])
DataWithDots = []
for row in X:
     for elem in row:
         DataWithDots.append(float(str(elem).replace(',', '.')))

ArrayWithDots=np.array(DataWithDots)
CompleteSet=np.reshape(ArrayWithDots,(-1,colNo))
FeatureSet=np.asarray(CompleteSet[:,:colNo-1])
ResultSet=np.asarray(CompleteSet[:,colNo-1])
print('FeatureSet:',FeatureSet)
print('Res Set:',ResultSet)

#LassoCV method
clf=LassoCV(cv=100)

sfm= SelectFromModel(clf,threshold=0.1)
sfm.fit(FeatureSet,ResultSet)
n_features=sfm.transform(FeatureSet)
#ResultTra= np.array([ResultSet])
print('LassoCV',n_features)

#final=np.concatenate((n_features,ResultTra.transpose(1,0)),axis=1)
#final_test = np.c_[n_features,ResultSet]
#print('final ', final.shape)
#print('final_test ', final_test)

X_train,X_test,y_train,y_test=train_test_split(n_features,ResultSet,test_size=0.33)
print('X_train:',X_train)
print('Y_train:',y_train)

clf.fit(X_train,y_train)
acc = clf.score(X_test,y_test)
print(acc)

neigh=KNeighborsClassifier(n_neighbors=5)
neigh.fit(X_train,y_train)
acc1 = neigh.score(X_test,y_test)
print(acc1)