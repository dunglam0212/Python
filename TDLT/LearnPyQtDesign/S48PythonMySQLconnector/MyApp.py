from PyQt6.QtWidgets import QApplication, QMainWindow

from LearnPyQtDesign.S48PythonMySQLconnector.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.connectMySQL()
myWindow.selectAllStudent()
myWindow.show()
app.exec()

