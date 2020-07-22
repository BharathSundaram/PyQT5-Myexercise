from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200,40)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.vlayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("LABEL")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.vlayout.addWidget(self.listView)

        self.vlayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 245, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vlayout.addItem(spacerItem)

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class Window(QtWidgets.QMainWindow):
    resized = QtCore.pyqtSignal()
    def  __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.resized.connect(self.someFunction)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)

    def someFunction(self):
        print("someFunction")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())