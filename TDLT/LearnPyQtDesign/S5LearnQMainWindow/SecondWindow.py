# Form implementation generated from reading ui file 'C:\Users\Dung Lam\PycharmProjects\TDLTC4\LearnPyQtDesign\S5LearnQMainWindow\SecondWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

class SecondWindow(object):
    def __init__(self, parent):
        self.parent = parent

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelChangeName = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelChangeName.setGeometry(QtCore.QRect(110, 140, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelChangeName.setFont(font)
        self.labelChangeName.setObjectName("labelChangeName")
        self.lineEditName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(110, 210, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.pushButtonRed = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonRed.setGeometry(QtCore.QRect(110, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonRed.setFont(font)
        self.pushButtonRed.setObjectName("pushButtonRed")
        self.pushButtonYellow = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonYellow.setGeometry(QtCore.QRect(280, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonYellow.setFont(font)
        self.pushButtonYellow.setObjectName("pushButtonYellow")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(440, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setObjectName("pushButtonExit")
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

        self.lineEditName.textChanged.connect(self.parent.lineEditName.setText)
        self.pushButtonExit.clicked.connect(self.processClose)
        self.pushButtonRed.clicked.connect(self.parent.changeRedColor)
        self.pushButtonYellow.clicked.connect(self.parent.changeYellowColor)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelChangeName.setText(_translate("MainWindow", "Change Name:"))
        self.lineEditName.setText(_translate("MainWindow", "Lâm Thùy Dung"))
        self.pushButtonRed.setText(_translate("MainWindow", "Red"))
        self.pushButtonYellow.setText(_translate("MainWindow", "Yellow"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))

    def processClose(self):
        self.MainWindow.close()
        self.parent.secondWindow = None
