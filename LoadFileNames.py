# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadFilesWindow.ui'
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
        LoadFilesDialog.resize(400, 245)

        self.ok_cancel_buttonBox = QtWidgets.QDialogButtonBox(LoadFilesDialog)
        self.ok_cancel_buttonBox.setGeometry(QtCore.QRect(40, 180, 341, 32))
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

        self.Train_Browse_pushButton_2 = QtWidgets.QPushButton(LoadFilesDialog)
        self.Train_Browse_pushButton_2.setGeometry(QtCore.QRect(290, 40, 75, 23))
        self.Train_Browse_pushButton_2.setObjectName("Train_Browse_pushButton_2")

        self.MethodTypes_Label = QtWidgets.QLabel(LoadFilesDialog)
        self.MethodTypes_Label.setGeometry(QtCore.QRect(20, 120, 151, 16))
        self.MethodTypes_Label.setObjectName("MethodTypes_Label")

        self.Lasso_checkBox = QtWidgets.QCheckBox(LoadFilesDialog)
        self.Lasso_checkBox.setEnabled(True)
        self.Lasso_checkBox.setGeometry(QtCore.QRect(20, 150, 70, 17))
        self.Lasso_checkBox.stateChanged.connect(self.changeState_lasso)
        self.Lasso_checkBox.setObjectName("Lasso_checkBox")

        self.ElasticNet_checkBox = QtWidgets.QCheckBox(LoadFilesDialog)
        self.ElasticNet_checkBox.setGeometry(QtCore.QRect(110, 150, 70, 17))
        self.ElasticNet_checkBox.setObjectName("ElasticNet_checkBox")
        self.ElasticNet_checkBox.stateChanged.connect(self.changeState_elasticnet)

        self.LassoCV_checkBox_3 = QtWidgets.QCheckBox(LoadFilesDialog)
        self.LassoCV_checkBox_3.setGeometry(QtCore.QRect(210, 150, 70, 17))
        self.LassoCV_checkBox_3.setObjectName("LassoCV_checkBox_3")
        self.LassoCV_checkBox_3.toggled.connect(self.changeState_lassocv)

        self.ElasticNetCVcheckBox_4 = QtWidgets.QCheckBox(LoadFilesDialog)
        self.ElasticNetCVcheckBox_4.setGeometry(QtCore.QRect(290, 150, 91, 17))
        self.ElasticNetCVcheckBox_4.setObjectName("ElasticNetCVcheckBox_4")
        self.ElasticNetCVcheckBox_4.toggled.connect(self.changeState_elasticnetcv)

        self.retranslateUi(LoadFilesDialog)
        self.ok_cancel_buttonBox.accepted.connect(self.ToSelectFeature)
        self.ok_cancel_buttonBox.rejected.connect(LoadFilesDialog.reject)
        self.Train_Browse_pushButton_2.clicked.connect(self.loadTrainFile)
        self.Test_Browse_pushButton.clicked.connect(self.loadTestFile)

        QtCore.QMetaObject.connectSlotsByName(LoadFilesDialog)

    def retranslateUi(self, LoadFilesDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadFilesDialog.setWindowTitle(_translate("LoadFilesDialog", "Dialog"))
        self.TestFileName_Label.setText(_translate("LoadFilesDialog", "Test File:"))
        self.TrainFileName_Label.setText(_translate("LoadFilesDialog", "Train File:"))
        self.Test_Browse_pushButton.setText(_translate("LoadFilesDialog", "Browse"))
        self.Train_Browse_pushButton_2.setText(_translate("LoadFilesDialog", "Browse"))
        self.MethodTypes_Label.setText(_translate("LoadFilesDialog", "Method for Feature Selection:"))
        self.Lasso_checkBox.setText(_translate("LoadFilesDialog", "Lasso"))
        self.ElasticNet_checkBox.setText(_translate("LoadFilesDialog", "Elastic Net"))
        self.LassoCV_checkBox_3.setText(_translate("LoadFilesDialog", "Lasso CV"))
        self.ElasticNetCVcheckBox_4.setText(_translate("LoadFilesDialog", "Elastic Net CV"))

    def loadTrainFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.TrainFileName, _ = QFileDialog.getOpenFileName(self, "Open File", "E:/Bachelor Thesis",
                                                       "CSV Files(*.csv)", options=options)
        if self.TrainFileName:
            self.TrainFileName_lineEdit.setText(self.TrainFileName)

    def loadTestFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.TestFileName, _ = QFileDialog.getOpenFileName(self, "Open File", "E:/Bachelor Thesis",
                                                       "CSV Files(*.csv)", options=options)
        if self.TestFileName:
            self.TestFileName_lineEdit.setText(self.TestFileName)

    def changeState_lasso(self):
        if self.Lasso_checkBox.isChecked():
            self.ElasticNet_checkBox.setChecked(False)
            self.LassoCV_checkBox_3.setChecked(False)
            self.ElasticNetCVcheckBox_4.setChecked(False)

    def changeState_elasticnet(self):
        if self.ElasticNet_checkBox.isChecked():
            self.Lasso_checkBox.setChecked(False)
            self.LassoCV_checkBox_3.setChecked(False)
            self.ElasticNetCVcheckBox_4.setChecked(False)

    def changeState_lassocv(self):
        if self.LassoCV_checkBox_3.isChecked():
            self.ElasticNet_checkBox.setChecked(False)
            self.Lasso_checkBox.setChecked(False)
            self.ElasticNetCVcheckBox_4.setChecked(False)

    def changeState_elasticnetcv(self):
        if self.ElasticNetCVcheckBox_4.isChecked():
            self.ElasticNet_checkBox.setChecked(False)
            self.Lasso_checkBox.setChecked(False)
            self.LassoCV_checkBox_3.setChecked(False)

    def ToSelectFeature(self):
        controller = Controller(self.TrainFileName,self.TestFileName)
        XTrain, yTrain = controller.TrainDataRead()
        XTest, yTest=controller.TestDataRead()
        LoadFilesDialog.close()
        name, _ = QFileDialog.getSaveFileName(self, 'Save File', 'E:/Bachelor Thesis', "CSV Files(*.csv)")
        if self.Lasso_checkBox.isChecked():
            controller.LassoInitialise()
        elif self.LassoCV_checkBox_3.isChecked():
            controller.LassoCVInitialise()
        elif self.ElasticNet_checkBox.isChecked():
            controller.ElasticNetInitialise()
        elif self.ElasticNetCVcheckBox_4.isChecked():
            controller.ElasticNetCVInitialise()
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

