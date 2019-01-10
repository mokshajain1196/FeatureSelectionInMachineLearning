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
feature_names = list(dataL.columns.values)
print(dataL)
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
print(CompleteSet)
#Break in Variable and Target set
FeatureSet=np.asarray(CompleteSet[:,:colNo-1])
ResultSet=np.asarray(CompleteSet[:,colNo-1])
# ElasticNetCV method
clf_FSel = LassoCV(cv=10, alphas= [0.09])
sfm = SelectFromModel(clf_FSel, threshold=0.25)
sfm.fit(FeatureSet, ResultSet)
n_features = sfm.transform(FeatureSet)

#n_features |= ResultSet
#n_features.add(ResultSet)
#print(final_test)
#np.savetxt("E:\Bachelor Thesis\TestLasso\foo.csv", final_test, delimiter=",")
cols= sfm.get_support()
#for bool, feature in zip(cols, feature_names):
 #   if bool:
  #      n_features.append(feature)
#final_test = np.c_[n_features, ResultSet]
#df = pd.DataFrame(final_test)
#df.to_csv("E:\Bachelor Thesis\TestLasso\Cars2.csv",sep=';', header=True)
