# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\LoadFilesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from FeatureSelectionFromCSVFile import Controller

class Ui_LoadFilesDialog(QWidget):
    def setupUi(self, LoadFilesDialog):
        LoadFilesDialog.setObjectName("LoadFilesDialog")
        LoadFilesDialog.resize(447, 285)
        self.ok_cancel_buttonBox = QtWidgets.QDialogButtonBox(LoadFilesDialog)
        self.ok_cancel_buttonBox.setGeometry(QtCore.QRect(60, 240, 341, 32))
        self.ok_cancel_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel_buttonBox.setObjectName("ok_cancel_buttonBox")

        self.TestFileName_Label = QtWidgets.QLabel(LoadFilesDialog)
        self.TestFileName_Label.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.TestFileName_Label.setObjectName("filePath_Label")

        self.TestFileName_lineEdit = QtWidgets.QLineEdit(LoadFilesDialog)
        self.TestFileName_lineEdit.setGeometry(QtCore.QRect(20, 90, 261, 20))
        self.TestFileName_lineEdit.setObjectName("path_lineEdit")

        self.TrainFileName_Label = QtWidgets.QLabel(LoadFilesDialog)
        self.TrainFileName_Label.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.TrainFileName_Label.setObjectName("fileName_Label")

        self.TrainFileName_lineEdit = QtWidgets.QLineEdit(LoadFilesDialog)
        self.TrainFileName_lineEdit.setGeometry(QtCore.QRect(20, 40, 261, 20))
        self.TrainFileName_lineEdit.setObjectName("name_lineEdit")

        self.Test_Browse_pushButton = QtWidgets.QPushButton(LoadFilesDialog)
        self.Test_Browse_pushButton.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.Test_Browse_pushButton.setObjectName("Test_Browse_pushButton")
        self.Train_Browse_pushButton = QtWidgets.QPushButton(LoadFilesDialog)
        self.Train_Browse_pushButton.setGeometry(QtCore.QRect(290, 40, 75, 23))
        self.Train_Browse_pushButton.setObjectName("Train_Browse_pushButton")
        self.MethodTypes_Label = QtWidgets.QLabel(LoadFilesDialog)
        self.MethodTypes_Label.setGeometry(QtCore.QRect(20, 120, 151, 16))
        self.MethodTypes_Label.setObjectName("MethodTypes_Label")

        self.Lasso_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.Lasso_radioButton.setGeometry(QtCore.QRect(20, 150, 82, 17))
        self.Lasso_radioButton.setObjectName("Lasso_radioButton")
        self.Lasso_radioButton.toggled.connect(self.changeState)

        self.LassoCV_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.LassoCV_radioButton.setGeometry(QtCore.QRect(110, 150, 82, 17))
        self.LassoCV_radioButton.setObjectName("LassoCV_radioButton")
        self.LassoCV_radioButton.toggled.connect(self.changeState)

        self.ElasticNet_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.ElasticNet_radioButton.setGeometry(QtCore.QRect(20, 180, 82, 17))
        self.ElasticNet_radioButton.setObjectName("ElasticNet_radioButton")
        self.ElasticNet_radioButton.toggled.connect(self.changeState)

        self.ElasticNetCV_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.ElasticNetCV_radioButton.setGeometry(QtCore.QRect(110, 180, 82, 17))
        self.ElasticNetCV_radioButton.setObjectName("ElasticNetCV_radioButton")
        self.ElasticNetCV_radioButton.toggled.connect(self.changeState)

        self.Ridge_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.Ridge_radioButton.setGeometry(QtCore.QRect(20, 210, 82, 17))
        self.Ridge_radioButton.setObjectName("Ridge_radioButton")
        self.Ridge_radioButton.toggled.connect(self.changeState)

        self.RidgeCV_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.RidgeCV_radioButton.setGeometry(QtCore.QRect(110, 210, 82, 17))
        self.RidgeCV_radioButton.setObjectName("RidgeCV_radioButton")
        self.RidgeCV_radioButton.toggled.connect(self.changeState)

        self.RidgeClassifier_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.RidgeClassifier_radioButton.setGeometry(QtCore.QRect(200, 210, 111, 17))
        self.RidgeClassifier_radioButton.setObjectName("RidgeClassifier_radioButton")
        self.RidgeClassifier_radioButton.toggled.connect(self.changeState)

        self.retranslateUi(LoadFilesDialog)
        self.ok_cancel_buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ok_cancel_buttonBox.accepted.connect(self.ToSelectFeature)
        self.ok_cancel_buttonBox.rejected.connect(LoadFilesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadFilesDialog)

    def retranslateUi(self, LoadFilesDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadFilesDialog.setWindowTitle(_translate("LoadFilesDialog", "Dialog"))
        self.TestFileName_Label.setText(_translate("LoadFilesDialog", "Test File:"))
        self.TrainFileName_Label.setText(_translate("LoadFilesDialog", "Train File:"))
        self.Test_Browse_pushButton.setText(_translate("LoadFilesDialog", "Browse"))
        self.Train_Browse_pushButton.setText(_translate("LoadFilesDialog", "Browse"))
        self.MethodTypes_Label.setText(_translate("LoadFilesDialog", "Method for Feature Selection:"))
        self.Lasso_radioButton.setText(_translate("LoadFilesDialog", "Lasso"))
        self.LassoCV_radioButton.setText(_translate("LoadFilesDialog", "LassoCV"))
        self.ElasticNet_radioButton.setText(_translate("LoadFilesDialog", "Elastic Net"))
        self.ElasticNetCV_radioButton.setText(_translate("LoadFilesDialog", "Elastic NetCV"))
        self.Ridge_radioButton.setText(_translate("LoadFilesDialog", "Ridge"))
        self.RidgeCV_radioButton.setText(_translate("LoadFilesDialog", "RidgeCV"))
        self.RidgeClassifier_radioButton.setText(_translate("LoadFilesDialog", "Ridge Classifier"))

    def loadTrainFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.TrainFileName, _ = QFileDialog.getOpenFileName(self, "Open File", "","CSV Files(*.csv)", options=options)
        if self.TrainFileName:
            self.TrainFileName_lineEdit.setText(self.TrainFileName)

    def loadTestFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.TestFileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files(*.csv)", options=options)
        if self.TestFileName:
            self.TestFileName_lineEdit.setText(self.TestFileName)

    def changeState(self):
        self.ok_cancel_buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def ToSelectFeature(self):
        controller = Controller(self.TrainFileName,self.TestFileName)
        XTrain, yTrain = controller.TrainDataRead()
        XTest, yTest=controller.TestDataRead()
        LoadFilesDialog.close()
        name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', "CSV Files(*.csv)")
        if self.Lasso_radioButton.isChecked():
            controller.LassoInitialise()
        elif self.LassoCV_radioButton.isChecked():
            controller.LassoCVInitialise()
        elif self.ElasticNet_radioButton.isChecked():
            controller.ElasticNetInitialise()
        elif self.ElasticNetCV_radioButton.isChecked():
            controller.ElasticNetCVInitialise()
        elif self.Ridge_radioButton.isChecked():
            controller.RidgeInitialise()
        elif self.RidgeCV_radioButton.isChecked():
            controller.RidgeCVInitialise()
        elif self.RidgeClassifier_radioButton.isChecked():
            controller.RidgeClassifierInitialise()

        controller.selectFeatures(XTrain, yTrain, name, XTest, yTest)
        print('Process finished')
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadFilesDialog = QtWidgets.QDialog()
    ui = Ui_LoadFilesDialog()
    ui.setupUi(LoadFilesDialog)
    LoadFilesDialog.show()
    sys.exit(app.exec_())
