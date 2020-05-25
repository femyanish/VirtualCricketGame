import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import FantasyCricket.*
from UI import EvaluateTeam.*



class MainWindow(QMainWindow, Ui_FantasyCricket):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Pophelp.triggered.connect(self.Ui_Help)
        self.actionEVALUATE_TEAM.triggered.connect(self.help_window)


   def help_window(self):        
          dialog=QtWidgets.QDialog()
          dialog.ui=Ui_Dialog()
          dialog.ui.setupUi(dialog)
          dialog.exec_()
          dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
