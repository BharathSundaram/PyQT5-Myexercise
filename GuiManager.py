import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class AppGui(QWidget):
  def __init__(self):
          super().__init__()
          self.title='NexGenParser'
          self.initUI()
  def initUI(self):
          self.setWindowTitle(self.title)
          self.show()
