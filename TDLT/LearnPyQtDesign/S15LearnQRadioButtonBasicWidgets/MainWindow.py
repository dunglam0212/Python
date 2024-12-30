# Form implementation generated from reading ui file 'C:\Users\Dung Lam\PycharmProjects\TDLT\LearnPyQtDesign\S15LearnQRadioButtonBasicWidgets\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 705)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxPersonal = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxPersonal.setGeometry(QtCore.QRect(150, 80, 611, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxPersonal.setFont(font)
        self.groupBoxPersonal.setStyleSheet("background: rgb(220, 215, 255);")
        self.groupBoxPersonal.setObjectName("groupBoxPersonal")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBoxPersonal)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 40, 541, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.fullNameLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.fullNameLabel.setObjectName("fullNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.fullNameLabel)
        self.fullNameLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.fullNameLineEdit.setObjectName("fullNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fullNameLineEdit)
        self.emailLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.emailLabel.setObjectName("emailLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.emailLabel)
        self.emailLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.emailLineEdit)
        self.labelGender = QtWidgets.QLabel(parent=self.groupBoxPersonal)
        self.labelGender.setGeometry(QtCore.QRect(30, 130, 101, 31))
        self.labelGender.setObjectName("labelGender")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.groupBoxPersonal)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 120, 291, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_Male = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.radioButton_Male.setObjectName("radioButton_Male")
        self.horizontalLayout.addWidget(self.radioButton_Male)
        self.radioButtonFemale = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.radioButtonFemale.setObjectName("radioButtonFemale")
        self.horizontalLayout.addWidget(self.radioButtonFemale)
        self.groupBoxOther = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxOther.setGeometry(QtCore.QRect(150, 300, 621, 201))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxOther.setFont(font)
        self.groupBoxOther.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.groupBoxOther.setStyleSheet("background: rgb(210, 255, 199);")
        self.groupBoxOther.setObjectName("groupBoxOther")
        self.labelAddress = QtWidgets.QLabel(parent=self.groupBoxOther)
        self.labelAddress.setGeometry(QtCore.QRect(30, 30, 101, 41))
        self.labelAddress.setObjectName("labelAddress")
        self.lineEditAddress = QtWidgets.QLineEdit(parent=self.groupBoxOther)
        self.lineEditAddress.setGeometry(QtCore.QRect(150, 40, 411, 31))
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.labelEducation = QtWidgets.QLabel(parent=self.groupBoxOther)
        self.labelEducation.setGeometry(QtCore.QRect(30, 80, 111, 41))
        self.labelEducation.setObjectName("labelEducation")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBoxOther)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 90, 160, 104))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonBachelor = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.radioButtonBachelor.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.radioButtonBachelor.setObjectName("radioButtonBachelor")
        self.verticalLayout.addWidget(self.radioButtonBachelor)
        self.radioButtonMaster = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.radioButtonMaster.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.radioButtonMaster.setObjectName("radioButtonMaster")
        self.verticalLayout.addWidget(self.radioButtonMaster)
        self.radioButtonDoctoral = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.radioButtonDoctoral.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.radioButtonDoctoral.setObjectName("radioButtonDoctoral")
        self.verticalLayout.addWidget(self.radioButtonDoctoral)
        self.pushButtonSendData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSendData.setGeometry(QtCore.QRect(400, 520, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSendData.setFont(font)
        self.pushButtonSendData.setObjectName("pushButtonSendData")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 25))
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
        self.groupBoxPersonal.setTitle(_translate("MainWindow", "Personal Information: "))
        self.fullNameLabel.setText(_translate("MainWindow", "Full Name:"))
        self.emailLabel.setText(_translate("MainWindow", "Email:"))
        self.labelGender.setText(_translate("MainWindow", "Gender:"))
        self.radioButton_Male.setText(_translate("MainWindow", "Male"))
        self.radioButtonFemale.setText(_translate("MainWindow", "Female"))
        self.groupBoxOther.setTitle(_translate("MainWindow", "Other Information"))
        self.labelAddress.setText(_translate("MainWindow", "Address:"))
        self.labelEducation.setText(_translate("MainWindow", "Education:"))
        self.radioButtonBachelor.setText(_translate("MainWindow", "Bachelor"))
        self.radioButtonMaster.setText(_translate("MainWindow", "Master"))
        self.radioButtonDoctoral.setText(_translate("MainWindow", "Doctoral"))
        self.pushButtonSendData.setText(_translate("MainWindow", "Send Data"))