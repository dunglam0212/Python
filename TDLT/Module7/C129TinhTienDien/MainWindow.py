# Form implementation generated from reading ui file 'C:\Users\Dung Lam\PycharmProjects\TDLT\Module7\C129TinhTienDien\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 535)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(190, 30, 311, 61))
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 100, 411, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelkwh = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelkwh.setObjectName("labelkwh")
        self.gridLayout.addWidget(self.labelkwh, 3, 0, 1, 1)
        self.lineEditkwh = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditkwh.setObjectName("lineEditkwh")
        self.gridLayout.addWidget(self.lineEditkwh, 3, 1, 1, 1)
        self.labelChisomoi = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelChisomoi.setObjectName("labelChisomoi")
        self.gridLayout.addWidget(self.labelChisomoi, 1, 0, 1, 1)
        self.labelChisocu = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelChisocu.setObjectName("labelChisocu")
        self.gridLayout.addWidget(self.labelChisocu, 0, 0, 1, 1)
        self.lineEditChisocu = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditChisocu.setObjectName("lineEditChisocu")
        self.gridLayout.addWidget(self.lineEditChisocu, 0, 1, 1, 1)
        self.labelSoho = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelSoho.setObjectName("labelSoho")
        self.gridLayout.addWidget(self.labelSoho, 2, 0, 1, 1)
        self.lineEditChisomoi = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditChisomoi.setObjectName("lineEditChisomoi")
        self.gridLayout.addWidget(self.lineEditChisomoi, 1, 1, 1, 1)
        self.lineEditSoho = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditSoho.setObjectName("lineEditSoho")
        self.gridLayout.addWidget(self.lineEditSoho, 2, 1, 1, 1)
        self.labelTien = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelTien.setObjectName("labelTien")
        self.gridLayout.addWidget(self.labelTien, 4, 0, 1, 1)
        self.labelTienthu = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelTienthu.setFont(font)
        self.labelTienthu.setStyleSheet("background: rgb(224, 252, 255);")
        self.labelTienthu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTienthu.setObjectName("labelTienthu")
        self.gridLayout.addWidget(self.labelTienthu, 4, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(200, 310, 291, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonSHBT = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButtonSHBT.setFont(font)
        self.pushButtonSHBT.setObjectName("pushButtonSHBT")
        self.gridLayout_2.addWidget(self.pushButtonSHBT, 0, 0, 1, 1)
        self.pushButtonKd = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButtonKd.setFont(font)
        self.pushButtonKd.setObjectName("pushButtonKd")
        self.gridLayout_2.addWidget(self.pushButtonKd, 0, 1, 1, 1)
        self.pushButtonSx = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButtonSx.setFont(font)
        self.pushButtonSx.setObjectName("pushButtonSx")
        self.gridLayout_2.addWidget(self.pushButtonSx, 0, 2, 1, 1)
        self.pushButtonTinhtiep = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButtonTinhtiep.setFont(font)
        self.pushButtonTinhtiep.setObjectName("pushButtonTinhtiep")
        self.gridLayout_2.addWidget(self.pushButtonTinhtiep, 1, 0, 1, 1)
        self.pushButtonHuongdan = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButtonHuongdan.setFont(font)
        self.pushButtonHuongdan.setObjectName("pushButtonHuongdan")
        self.gridLayout_2.addWidget(self.pushButtonHuongdan, 1, 1, 1, 1)
        self.pushButtonThoat = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButtonThoat.setFont(font)
        self.pushButtonThoat.setObjectName("pushButtonThoat")
        self.gridLayout_2.addWidget(self.pushButtonThoat, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonThoat.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#0000ff; font-family: Times New Roman;\">Phần mềm tính tiền điện</span></p></body></html>"))
        self.labelkwh.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">Số kWh dùng:</span></p></body></html>"))
        self.labelChisomoi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">Chỉ số mới:</span></p></body></html>"))
        self.labelChisocu.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-family: Times New Roman;\">Chỉ số cũ:</span></p></body></html>"))
        self.labelSoho.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">Số hộ (SHBT):</span></p></body></html>"))
        self.labelTien.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">Số tiền sẽ thu:</span></p></body></html>"))
        self.labelTienthu.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButtonSHBT.setText(_translate("MainWindow", "SHBT"))
        self.pushButtonKd.setText(_translate("MainWindow", "Kinh doanh"))
        self.pushButtonSx.setText(_translate("MainWindow", "Sản xuất"))
        self.pushButtonTinhtiep.setText(_translate("MainWindow", "Tính tiếp"))
        self.pushButtonHuongdan.setText(_translate("MainWindow", "Hướng dẫn"))
        self.pushButtonThoat.setText(_translate("MainWindow", "Thoát"))