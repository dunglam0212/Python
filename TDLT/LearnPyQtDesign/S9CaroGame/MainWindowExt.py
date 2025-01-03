from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton

from LearnPyQtDesign.S9CaroGame.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.previous = '' #Biến previóu đáh dấu là trước đó 'X' hay 'O' đã được chọn
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonDrawCaro.clicked.connect(self.processDrawCaro)
    def show(self):
        self.MainWindow.show()
    def processDrawCaro(self):
        row = int(self.lineEditRow.text())
        column = int(self.lineEditColumn.text())
        for i in range(row):
            self.gridLayout.setRowStretch(i,1)
            for j in range(column):
                self.gridLayout.setColumnStretch(j,1)
                btn = QPushButton()
                btn.setFixedWidth(50)
                btn.setFixedHeight(50)
                btn.sizePolicy().setHorizontalStretch(1)
                btn.sizePolicy().setVerticalStretch(1)
                self.gridLayout.addWidget(btn,i,j,
                                          alignment = Qt.AlignmentFlag.AlignVertical_Mask|Qt.AlignmentFlag.AlignHorizontal_Mask)
                btn.clicked.connect(partial(self.processClicked,btn))
                #Partial có 2 đối số, đối số 1 là slot xử lý sự kiện khi button được nhấn, đối số 2 truyền đối tượng button vào để qtrinh xử lý ta biết được chính xác button nào được nhấn
    def processClicked(self, btn):
        if len(btn.text()) >0:
            return
        if self.previous == 'X':
            self.previous = 'O'
        else:
            self.previous = 'X'
        if len(btn.text()) == 0:
            btn.setText(self.previous)
        else:
            btn.setText(self.previous)
