import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Define a new signal called 'trigger' that has no arguments.
        trigger = pyqtSignal()

        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        #self.connect(self.lineedit, SIGNAL("returnPressed()"),self.updateUi)
        self.lineedit.returnPressed.connect(self.updateUi)
    def updateUi(self):
        text = str(self.lineedit.text())
        try:
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()