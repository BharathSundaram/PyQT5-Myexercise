import sys
from math import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Init called")
        self.Ui_Init_Gui()

    def Ui_Init_Gui(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex= MyApp()
    sys.exit(app.exec_())
