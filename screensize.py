import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit, QLabel, QSplitter, QWidget, QListWidget, QApplication, QTabWidget, QGroupBox, \
    QFormLayout, QSizePolicy, QLayout
from PyQt5.QtCore import Qt


class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_tabs()

        self.main_splitter = QSplitter(Qt.Horizontal)
        some_left_widget = QWidget()
        some_right_widget = QWidget()

        mid = QSplitter(Qt.Vertical)
        mid.addWidget(QListWidget())
        mid.addWidget(self.tabs)

        self.main_splitter.addWidget(some_left_widget)
        self.main_splitter.addWidget(mid)
        self.main_splitter.addWidget(some_right_widget)
        self.setCentralWidget(self.main_splitter)
        self.showMaximized()

    def init_tabs(self):
        self.properties_dict = {}
        self.properties_dict['Text'] = QLineEdit()

        self.tabs = QTabWidget()
        self.properties_groupbox = QGroupBox("Overview")

        layout = QFormLayout()
        for k, v in self.properties_dict.items():
            layout.addRow(QLabel(k + ':'), v)

        self.properties_groupbox.setLayout(layout)
        self.tabs.addTab(self.properties_groupbox, 'Properties')

        # I have no idea how these work
        self.properties_groupbox.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.properties_groupbox.resize(self.properties_groupbox.minimumSizeHint())
        self.properties_groupbox.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())