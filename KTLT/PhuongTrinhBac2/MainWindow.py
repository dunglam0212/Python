# Form implementation generated from reading ui file 'C:\Users\Dung Lam\PycharmProjects\KTLT\PhuongTrinhBac2\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 553)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 204, 234);\n"
"background: rgb(255, 253, 246);")
        self.label.setObjectName("label")
        self.groupBoxHeSo = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxHeSo.setGeometry(QtCore.QRect(70, 90, 521, 141))
        self.groupBoxHeSo.setStyleSheet("background: rgb(224, 250, 255);")
        self.groupBoxHeSo.setObjectName("groupBoxHeSo")
        self.labelHeSoA = QtWidgets.QLabel(parent=self.groupBoxHeSo)
        self.labelHeSoA.setGeometry(QtCore.QRect(30, 40, 52, 15))
        self.labelHeSoA.setObjectName("labelHeSoA")
        self.lineEditHeSoA = QtWidgets.QLineEdit(parent=self.groupBoxHeSo)
        self.lineEditHeSoA.setGeometry(QtCore.QRect(100, 40, 391, 20))
        self.lineEditHeSoA.setObjectName("lineEditHeSoA")
        self.lineEditHeSoB = QtWidgets.QLineEdit(parent=self.groupBoxHeSo)
        self.lineEditHeSoB.setGeometry(QtCore.QRect(100, 70, 391, 20))
        self.lineEditHeSoB.setObjectName("lineEditHeSoB")
        self.labelHeSoB = QtWidgets.QLabel(parent=self.groupBoxHeSo)
        self.labelHeSoB.setGeometry(QtCore.QRect(30, 70, 52, 15))
        self.labelHeSoB.setObjectName("labelHeSoB")
        self.lineEditHeSoC = QtWidgets.QLineEdit(parent=self.groupBoxHeSo)
        self.lineEditHeSoC.setGeometry(QtCore.QRect(100, 100, 391, 20))
        self.lineEditHeSoC.setObjectName("lineEditHeSoC")
        self.labelHeSoC = QtWidgets.QLabel(parent=self.groupBoxHeSo)
        self.labelHeSoC.setGeometry(QtCore.QRect(30, 100, 52, 15))
        self.labelHeSoC.setObjectName("labelHeSoC")
        self.groupBoxChucNang = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxChucNang.setGeometry(QtCore.QRect(70, 250, 521, 111))
        self.groupBoxChucNang.setStyleSheet("background: rgb(233, 225, 242);")
        self.groupBoxChucNang.setObjectName("groupBoxChucNang")
        self.pushButtonGiai = QtWidgets.QPushButton(parent=self.groupBoxChucNang)
        self.pushButtonGiai.setGeometry(QtCore.QRect(60, 30, 101, 51))
        self.pushButtonGiai.setStyleSheet("background: rgb(255, 231, 188);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Dung Lam\\PycharmProjects\\KTLT\\PhuongTrinhBac2\\images/ic_calculate.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonGiai.setIcon(icon)
        self.pushButtonGiai.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonGiai.setObjectName("pushButtonGiai")
        self.pushButtonTiep = QtWidgets.QPushButton(parent=self.groupBoxChucNang)
        self.pushButtonTiep.setGeometry(QtCore.QRect(210, 30, 101, 51))
        self.pushButtonTiep.setStyleSheet("background: rgb(255, 231, 188);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Dung Lam\\PycharmProjects\\KTLT\\PhuongTrinhBac2\\images/ic_new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonTiep.setIcon(icon1)
        self.pushButtonTiep.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonTiep.setObjectName("pushButtonTiep")
        self.pushButtonThoat = QtWidgets.QPushButton(parent=self.groupBoxChucNang)
        self.pushButtonThoat.setGeometry(QtCore.QRect(350, 30, 101, 51))
        self.pushButtonThoat.setStyleSheet("background: rgb(255, 231, 188);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\Dung Lam\\PycharmProjects\\KTLT\\PhuongTrinhBac2\\images/ic_exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonThoat.setIcon(icon2)
        self.pushButtonThoat.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonThoat.setObjectName("pushButtonThoat")
        self.groupBoxKetQua = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxKetQua.setGeometry(QtCore.QRect(70, 390, 521, 81))
        self.groupBoxKetQua.setObjectName("groupBoxKetQua")
        self.labelKetQua = QtWidgets.QLabel(parent=self.groupBoxKetQua)
        self.labelKetQua.setEnabled(False)
        self.labelKetQua.setGeometry(QtCore.QRect(20, 30, 471, 31))
        self.labelKetQua.setStyleSheet("background: rgb(255, 246, 227);")
        self.labelKetQua.setText("")
        self.labelKetQua.setObjectName("labelKetQua")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 25))
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
        self.label.setText(_translate("MainWindow", "Phương trình bậc 2"))
        self.groupBoxHeSo.setTitle(_translate("MainWindow", "Nhập các hệ số của phương trình:"))
        self.labelHeSoA.setText(_translate("MainWindow", "Hệ số a:"))
        self.labelHeSoB.setText(_translate("MainWindow", "Hệ số a:"))
        self.labelHeSoC.setText(_translate("MainWindow", "Hệ số a:"))
        self.groupBoxChucNang.setTitle(_translate("MainWindow", "Các chức năng:"))
        self.pushButtonGiai.setText(_translate("MainWindow", "Giải"))
        self.pushButtonTiep.setText(_translate("MainWindow", "Tiếp"))
        self.pushButtonThoat.setText(_translate("MainWindow", "Thoát"))
        self.groupBoxKetQua.setTitle(_translate("MainWindow", "Kết quả:"))
