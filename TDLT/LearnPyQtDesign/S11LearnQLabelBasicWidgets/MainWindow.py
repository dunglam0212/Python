# Form implementation generated from reading ui file 'C:\Users\Dung Lam\PycharmProjects\TDLT\LearnPyQtDesign\S11LearnQLabelBasicWidgets\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelName = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(280, 50, 211, 61))
        self.labelName.setObjectName("labelName")
        self.pushButtonChangeText = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonChangeText.setGeometry(QtCore.QRect(100, 110, 111, 41))
        self.pushButtonChangeText.setObjectName("pushButtonChangeText")
        self.pushButtonFontSize = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonFontSize.setGeometry(QtCore.QRect(230, 110, 111, 41))
        self.pushButtonFontSize.setObjectName("pushButtonFontSize")
        self.pushButtonLeft = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLeft.setGeometry(QtCore.QRect(390, 110, 111, 41))
        self.pushButtonLeft.setObjectName("pushButtonLeft")
        self.pushButtonCenter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCenter.setGeometry(QtCore.QRect(520, 110, 111, 41))
        self.pushButtonCenter.setObjectName("pushButtonCenter")
        self.pushButtonRight = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonRight.setGeometry(QtCore.QRect(640, 110, 111, 41))
        self.pushButtonRight.setObjectName("pushButtonRight")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 190, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 190, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 270, 431, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\Dung Lam\\PycharmProjects\\TDLT\\LearnPyQtDesign\\S11LearnQLabelBasicWidgets\\images/204-LÂM THÙY DUNG-TRƯỜNG ĐẠI HỌC KINH TẾ - LUẬT ĐHQG TP.HCM.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelName.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#aaaaff;\">Lâm Thùy Dung</span></p></body></html>"))
        self.pushButtonChangeText.setText(_translate("MainWindow", "Change Text"))
        self.pushButtonFontSize.setText(_translate("MainWindow", "Font Size A+"))
        self.pushButtonLeft.setText(_translate("MainWindow", "Alignment Left"))
        self.pushButtonCenter.setText(_translate("MainWindow", "Alignment Center"))
        self.pushButtonRight.setText(_translate("MainWindow", "Alignment Right"))
        self.pushButton.setText(_translate("MainWindow", "Show .png Format"))
        self.pushButton_2.setText(_translate("MainWindow", "Show .gif Format"))
