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
        self.Test_Browse_pushButton.clicked.connect(self.loadTestFile)

        self.Train_Browse_pushButton = QtWidgets.QPushButton(LoadFilesDialog)
        self.Train_Browse_pushButton.setGeometry(QtCore.QRect(290, 40, 75, 23))
        self.Train_Browse_pushButton.setObjectName("Train_Browse_pushButton")
        self.Train_Browse_pushButton.clicked.connect(self.loadTrainFile)

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
        self.LassoCV_radioButton.toggled.connect(self.changeStateCV)

        self.ElasticNet_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.ElasticNet_radioButton.setGeometry(QtCore.QRect(20, 180, 82, 17))
        self.ElasticNet_radioButton.setObjectName("ElasticNet_radioButton")
        self.ElasticNet_radioButton.toggled.connect(self.changeState)

        self.ElasticNetCV_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.ElasticNetCV_radioButton.setGeometry(QtCore.QRect(110, 180, 82, 17))
        self.ElasticNetCV_radioButton.setObjectName("ElasticNetCV_radioButton")
        self.ElasticNetCV_radioButton.toggled.connect(self.changeStateCV)

        self.RidgeClassifier_radioButton = QtWidgets.QRadioButton(LoadFilesDialog)
        self.RidgeClassifier_radioButton.setGeometry(QtCore.QRect(20, 210, 111, 17))
        self.RidgeClassifier_radioButton.setObjectName("RidgeClassifier_radioButton")
        self.RidgeClassifier_radioButton.toggled.connect(self.changeState)

        self.threshold_label = QtWidgets.QLabel(LoadFilesDialog)
        self.threshold_label.setGeometry(QtCore.QRect(250, 130, 61, 16))
        self.threshold_label.setObjectName("threshold_label")

        self.alpha_label = QtWidgets.QLabel(LoadFilesDialog)
        self.alpha_label.setGeometry(QtCore.QRect(250, 170, 47, 13))
        self.alpha_label.setObjectName("alpha_label")

        self.threshold_lineEdit = QtWidgets.QLineEdit(LoadFilesDialog)
        self.threshold_lineEdit.setGeometry(QtCore.QRect(310, 130, 61, 20))
        self.threshold_lineEdit.setObjectName("threshold_lineEdit")
        self.threshold_lineEdit.setText("0,25")

        self.alpha_lineEdit = QtWidgets.QLineEdit(LoadFilesDialog)
        self.alpha_lineEdit.setGeometry(QtCore.QRect(310, 170, 61, 20))
        self.alpha_lineEdit.setObjectName("alpha_lineEdit")
        self.alpha_lineEdit.setText("1")

        self.retranslateUi(LoadFilesDialog)
        self.ok_cancel_buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ok_cancel_buttonBox.accepted.connect(self.ToSelectFeature)
        self.ok_cancel_buttonBox.rejected.connect(LoadFilesDialog.close)
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
        self.RidgeClassifier_radioButton.setText(_translate("LoadFilesDialog", "Ridge Classifier"))
        self.threshold_label.setText(_translate("LoadFilesDialog", "Threshold"))
        self.alpha_label.setText(_translate("LoadFilesDialog", "Alpha"))

    def loadTrainFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.TrainFileName, _ = QFileDialog.getOpenFileName(self, "Open File", "E:\Bachelor Thesis\Data Sets","CSV Files(*.csv)", options=options)
        if self.TrainFileName:
            self.TrainFileName_lineEdit.setText(self.TrainFileName)

    def loadTestFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.TestFileName, _ = QFileDialog.getOpenFileName(self, "Open File", "","CSV Files(*.csv)", options=options)
        if self.TestFileName:
            self.TestFileName_lineEdit.setText(self.TestFileName)

    def changeState(self):
        self.ok_cancel_buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        self.alpha_lineEdit.setText("1")
        self.alpha_lineEdit.setReadOnly(False)

    def changeStateCV(self):
        self.ok_cancel_buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        self.alpha_lineEdit.setText("")
        self.alpha_lineEdit.setReadOnly(True)

    def ToSelectFeature(self):
        threshold = float(self.threshold_lineEdit.text().replace(',', '.'))
        controller = Controller(self.TrainFileName,self.TestFileName, threshold= threshold)
        XTrain, yTrain = controller.TrainDataRead()
        XTest, yTest=controller.TestDataRead()
        LoadFilesDialog.close()
        nameTrain, _ = QFileDialog.getSaveFileName(self, 'Save Train File', '', "CSV Files(*.csv)")
        nameTest, _ = QFileDialog.getSaveFileName(self, 'Save Test File', '', "CSV Files(*.csv)")
        alpha = float(self.alpha_lineEdit.text().replace(',', '.'))

        print("Alpha: ", alpha)
        print("Threshold: ", threshold)

        if self.Lasso_radioButton.isChecked():
            controller.LassoInitialise(alpha)
        elif self.LassoCV_radioButton.isChecked():
            controller.LassoCVInitialise()
        elif self.ElasticNet_radioButton.isChecked():
            controller.ElasticNetInitialise(alpha)
        elif self.ElasticNetCV_radioButton.isChecked():
            controller.ElasticNetCVInitialise()
        elif self.RidgeClassifier_radioButton.isChecked():
            controller.RidgeClassifierInitialise(alpha)

        controller.selectFeatures(XTrain, yTrain,nameTrain, nameTest, XTest, yTest) #
        print('Process finished')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadFilesDialog = QtWidgets.QDialog()
    ui = Ui_LoadFilesDialog()
    ui.setupUi(LoadFilesDialog)
    LoadFilesDialog.show()
    sys.exit(app.exec_())

