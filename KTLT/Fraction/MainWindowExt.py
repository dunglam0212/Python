from PyQt6.QtWidgets import QMessageBox

from Fraction.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonThoat.clicked.connect(self.processThoat)
        self.pushButtonTiep.clicked.connect(self.processTiep)
        self.pushButtonCong.clicked.connect(self.processCong)
    def processThoat(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Xác nhận thoát')
        msgBox.setText('Bạn có chắc chắn muốn thoát không?')
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes |
                                  QMessageBox.StandardButton.No)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()

    def processTiep(self):
        self.lineEditTuSo1.setText('')
        self.lineEditMauSo1.setText('')
        self.lineEditTuSo2.setText('')
        self.lineEditMauSo2.setText('')
        self.labelKetQua.setText('')
    def processCong(self):
        TuSo1 = int(self.lineEditTuSo1.text())
        MauSo1 = int(self.lineEditMauSo1.text())
        TuSo2 = int(self.lineEditMauSo1.text())
        MauSo2 = int(self.lineEditMauSo2.text())
        if MauSo1 != 0 and MauSo2!=0:
            kq = (TuSo1*MauSo2 + TuSo2*MauSo1)/(MauSo1*MauSo2)
            self.labelKetQua.setText(f'{TuSo1}/{MauSo1} + {TuSo2}/{MauSo2} = {kq}')
        else:
            pass

