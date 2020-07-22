from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QWidget,
                             QMainWindow, QVBoxLayout, QSizePolicy)
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        cwidget = QWidget(self)
        self.setCentralWidget(cwidget)
        self.resize(100, 100)

        vbox = QVBoxLayout(cwidget)
        vbox.addWidget(QWidget())
        self.bar = LabelBar(self)
        vbox.addWidget(self.bar)

        timer = QTimer(self)
        timer.timeout.connect(lambda: self.bar.lbl2.setText("a" * 100))
        timer.start(1000)

class LabelBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        hbox = QHBoxLayout(self)
        self.lbl1 = QLabel(text="eggs")
        hbox.addWidget(self.lbl1)
        self.lbl2 = QLabel(text="spam")
        hbox.addWidget(self.lbl2)

if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()