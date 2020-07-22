
import GuiManager
import sys
from PyQt5.QtWidgets import QApplication

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex= GuiManager.AppGui()
    sys.exit(app.exec_())