import numpy as np
import matplotlib as plt
import pandas as pd
import seaborn as sb
from sklearn import datasets
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import ElasticNetCV,LassoCV,RidgeCV,RidgeClassifierCV,LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.utils.multiclass import type_of_target
from sklearn.svm import SVC,SVR

dataL = pd.read_csv('E:\Bachelor Thesis\TestLasso\Cars.csv', delimiter=';')
#Set Formation
X = np.array(dataL[:])
colNo=len(X[0])
DataWithDots = []
for row in X:
     for elem in row:
         DataWithDots.append(float(str(elem).replace(',', '.')))
#German to English
ArrayWithDots=np.array(DataWithDots)
CompleteSet=np.reshape(ArrayWithDots,(-1,colNo))
#Break in Variable and Target set
FeatureSet=np.asarray(CompleteSet[:,:colNo-1])
ResultSet=np.asarray(CompleteSet[:,colNo-1])
#Split main set in test and train set
X_train, X_test, y_train, y_test = train_test_split(FeatureSet, ResultSet, test_size=0.1, random_state=0)
#print('FeatureSet:',FeatureSet)
#print('Res Set:',ResultSet)

#Detect Type of Target, Regression or Classifier
typeOfTarget=type_of_target(ResultSet)
print(typeOfTarget)
#Discrete
if typeOfTarget=='multiclass':
    #Calculate cccuracy of complete dataset
    clf_complete = SVC(gamma='auto')
    clf_complete.fit(X_train, y_train)
    acc = clf_complete.score(X_test, y_test)
    print('SVC(complete set):', acc)

    # ElasticNetCV method
    clf_FSel = LassoCV(cv=10, alphas= [0.09])
    sfm = SelectFromModel(clf_FSel, threshold=0.25)
    sfm.fit(FeatureSet, ResultSet)
    n_features = sfm.transform(FeatureSet)
    # ResultTra= np.array([ResultSet])
    #print('ElasticNetCV', n_features)
    print('No. of selected features:', len(n_features[0]), ' out of:', len(FeatureSet[0]))

    X_Ftrain, X_Ftest, y_Ftrain, y_Ftest = train_test_split(n_features, ResultSet, test_size=0.1,random_state=0)
    #clf.fit(X_train,y_train)
    #acc = clf.score(X_test,y_test)
    #print('LassoCV',acc)

    # neigh=KNeighborsClassifier(n_neighbors=5)
    # neigh.fit(X_train,y_train)
    # acc1 = neigh.score(X_test,y_test)
    # print(acc1)

    clf_FSel.fit(X_Ftrain,y_Ftrain)
    acc_sameModel=clf_FSel.score(X_Ftest,y_Ftest)
    print('LassoRegression',acc_sameModel)

    clf_Split = SVC(gamma='auto')
    clf_Split.fit(X_Ftrain, y_Ftrain)
    acc_split = clf_Split.score(X_Ftest, y_Ftest)
    print('SVC(split):', acc_split)


elif typeOfTarget=='continuous':
    #Calculate cccuracy of complete dataset
    clf_complete = SVR(gamma='auto')
    clf_complete.fit(X_train, y_train)
    acc = clf_complete.score(X_test, y_test)
    print('SVR(complete set):', acc)

    # ElasticNetCV method
    clf_FSel = LassoCV(cv=10)
    sfm = SelectFromModel(clf_FSel, threshold=0.25)
    sfm.fit(FeatureSet, ResultSet)
    n_features = sfm.transform(FeatureSet)
    # ResultTra= np.array([ResultSet])
    #print('ElasticNetCV', n_features)
    print('No. of selected features:', len(n_features[0]), ' out of:', len(FeatureSet[0]))

    X_Ftrain, X_Ftest, y_Ftrain, y_Ftest = train_test_split(n_features, ResultSet, test_size=0.1,random_state=0)
    #clf.fit(X_train,y_train)
    #acc = clf.score(X_test,y_test)
    #print('LassoCV',acc)

    # neigh=KNeighborsClassifier(n_neighbors=5)
    # neigh.fit(X_train,y_train)
    # acc1 = neigh.score(X_test,y_test)
    # print(acc1)

    clf_FSel.fit(X_Ftrain,y_Ftrain)
    acc_sameModel=clf_FSel.score(X_Ftest,y_Ftest)
    print('LassoRegression',acc_sameModel)

    clf_Split = SVR(gamma='auto')
    clf_Split.fit(X_Ftrain, y_Ftrain)
    acc_split = clf_Split.score(X_Ftest, y_Ftest)
    print('SVR(split):', acc_split)
