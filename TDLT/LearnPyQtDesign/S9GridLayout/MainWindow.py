# Form implementation generated from reading ui file 'C:\Users\Dung Lam\PycharmProjects\TDLTC4\LearnPyQtDesign\S9GridLayout\MainWindow.ui'
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayout.addWidget(self.pushButtonLogin)
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.horizontalLayout.addWidget(self.pushButtonExit)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 2, 1, 1)
        self.labelPassword = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.gridLayout.addWidget(self.labelPassword, 3, 1, 1, 1)
        self.labelUserName = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelUserName.setFont(font)
        self.labelUserName.setObjectName("labelUserName")
        self.gridLayout.addWidget(self.labelUserName, 2, 1, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 3, 2, 1, 1)
        self.checkBoxSaveInfor = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBoxSaveInfor.setObjectName("checkBoxSaveInfor")
        self.gridLayout.addWidget(self.checkBoxSaveInfor, 4, 2, 1, 1)
        self.lineEditUserName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.gridLayout.addWidget(self.lineEditUserName, 2, 2, 1, 1)
        self.labelTitle = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
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
        self.pushButtonLogin.setText(_translate("MainWindow", "Login"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
        self.labelPassword.setText(_translate("MainWindow", "Password:"))
        self.labelUserName.setText(_translate("MainWindow", "User Name:"))
        self.checkBoxSaveInfor.setText(_translate("MainWindow", "Save login information"))
        self.labelTitle.setText(_translate("MainWindow", "Login Screen"))
