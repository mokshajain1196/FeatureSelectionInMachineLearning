import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import ElasticNetCV, LassoCV, RidgeCV, RidgeClassifier, Lasso, ElasticNet, Ridge, SGDClassifier
from scipy import stats

#Main Idea: Provide test and train data in differnt .csv files created using EIDOLearner. Feature selection runs on Training set.
#Same features are selected from testing set and the resukting sets from train and testing are concatenated and provided as result
#in .csv file.
class Controller:
    def __init__(self,TrainfileName,TestfileName):
        self.Traindata=None
        self.Testdata=None
        self.TrainFilename=TrainfileName
        self.TestFileName=TestfileName
        self.TraindataSet_Header=None
        self.methodUsed=None

    def TrainDataRead(self):
        #Read as pandas
        self.Traindata = pd.read_csv(self.TrainFilename, delimiter=';')
        #Get all Col names
        self.TraindataSet_Header = list(self.Traindata.columns.values)
        # Set Formation
        #Convert to numpy
        DataArray = np.array(self.Traindata[:])
        colNo = len(DataArray[0])
        #Cant Work with , need to convert sets in english version. With .
        FloatDataEng = []
        for row in DataArray:
            for elem in row:
                FloatDataEng.append(float(str(elem).replace(',', '.')))
        # German to English
        ArraEng = np.array(FloatDataEng)
        CompleteSet = np.reshape(ArraEng, (-1, colNo))
        # Break in Variable and Target set
        FeatureSet = np.asarray(CompleteSet[:, :colNo - 1])
        ResultSet = np.asarray(CompleteSet[:, colNo - 1])
        # Save the Complete set in pandas version. Will be used later
        self.Traindata = pd.DataFrame(CompleteSet, columns=self.TraindataSet_Header)
        #Return X and y in numpy version
        return FeatureSet,ResultSet

    def TestDataRead(self):
        #Read as pandas
        self.Testdata = pd.read_csv(self.TestFileName, delimiter=';')
        #Read all colum names. No need in general though, as header similar to testing data. Could be required later.
        self.TestdataSet_Header = list(self.Testdata.columns.values)

        # Set Formation
        #Convert to numpy
        DataArray = np.array(self.Testdata[:])
        colNo = len(DataArray[0])
        FloatDataEng = []
        for row in DataArray:
            for elem in row:
                FloatDataEng.append(float(str(elem).replace(',', '.')))
        # German to English
        ArraEng = np.array(FloatDataEng)
        CompleteSet = np.reshape(ArraEng, (-1, colNo))
        # Break in Variable and Target set
        FeatureSet = np.asarray(CompleteSet[:, :colNo - 1])
        ResultSet = np.asarray(CompleteSet[:, colNo - 1])
        # Save the Complete set in pandas version. Will be used late
        self.Testdata=pd.DataFrame(CompleteSet,columns=self.TraindataSet_Header)
        #Return X and y as numpy
        return FeatureSet,ResultSet

    #To select type of method for feature selection
    def LassoCVInitialise(self):
        self.methodUsed=LassoCV(cv=10)
    def LassoInitialise(self):
        self.methodUsed=Lasso(alpha=0.01)
    def ElasticNetInitialise(self):
        self.methodUsed=ElasticNet(alpha=0.1)
    def ElasticNetCVInitialise(self):
        self.methodUsed=ElasticNetCV(cv=10)
    def RidgeClassifierInitialise(self):
         self.methodUsed = RidgeClassifier()#alpha=0.75)
    def RidgeCVInitialise(self):
        self.methodUsed = RidgeCV(cv=10)
    def RidgeInitialise(self):
        self.methodUsed = Ridge()

    #This method selects the features from Feature set of training data(TrainX), based on the index numbers of selected features
    #it selects the columns from feature set of testing data. In end it concatenates both sets and provides a .csv file of selected
    #features as output.
    def selectFeatures(self,TrainX,TrainY,ExportFilePathTrain,ExportFilePathTest,TestX,TestY): #
        #SFM: Meta-transformer for selecting features based on importance weights.

        sfm = SelectFromModel(self.methodUsed, threshold=0.5)
        #Fit the data, Complete training set broken in Variable and Result set
        sfm.fit(TrainX, TrainY)
        #Transform the data
        n_features_method_used = sfm.transform(TrainX)
        #print(self.methodUsed)
        sfm_EN= SelectFromModel(ElasticNet(alpha=0.3), threshold=0.3)
        sfm_EN.fit(TrainX,TrainY)
        n_features_elasticNet = sfm_EN.transform(TrainX)
        #print('n_features_elasticNet',n_features_method_used)
        #print(stats.ttest_ind(n_features_method_used,n_features_elasticNet,axis=1))
        #Based on selected feature columns, get index numbers and names of features.
        cols = sfm.get_support()
        feature_idxn = np.append(cols, [False])
        featureName = self.Traindata.columns[feature_idxn]
        print(featureName.values)
        #Create another set from Testing Data for selected features
        testing_featureSet=self.Testdata.iloc[:,feature_idxn]
        ResultName = self.TraindataSet_Header[len(self.TraindataSet_Header) - 1]
        ResultHeader = np.append(featureName.values, ResultName)
        #Complete training set: join features and Result set. Convert to pandas.


        final_Train = pd.DataFrame(np.c_[n_features_method_used, TrainY])
        # Complete testing set: join features and Result set. Convert to pandas.


        final_Test=pd.DataFrame(np.c_[testing_featureSet,TestY])
        #final set in concatination of training and testing set.
        #final_Set=pd.concat([final_Train,final_Test])

        #When file is read by pandas it adds up row of 0's in the end. One must remove it. Can cause problem in classification.
        dfTrain = final_Train[(final_Train.T != 0.0).any()]
        dfTest = final_Test[(final_Test.T != 0.0).any()]
        #Convert dataframe to .csv
        dfTrain.to_csv(ExportFilePathTrain, sep=';', header=ResultHeader, encoding='utf8', index=False)
        dfTest.to_csv(ExportFilePathTest, sep=';', header=ResultHeader, encoding='utf8', index=False)



