import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from FantasyCricket.UI import *
from FantasyCricket.UI.EvaluateTeam import *
from FantasyCricket.DB import *
from FantasyCricket.DB.Database import *
import sqlite3

from FantasyCricket.UI.FantasyCricket import Ui_FantasyCricket

db = ".\DB\FantasyCricket.db"


class MainWindow(QMainWindow, Ui_FantasyCricket):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # calling the trigger functions for menu items
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)

# populate players in the available list according to category(BAT,BOWL,AR,WK)
    def populatePlayers(self, category):
        self.avlist.clear()
        print('populateplayers')
        playerslist = selectPlayers(category,db)
        self.avlist.addItems(playerslist)

    def menufunction(self, action):
        txt = str(action.text())
        print(txt)
        if txt == 'NEW Team':
            text, result = QInputDialog.getText(self, 'Input Dialog', 'Enter the new Team name:')
            print(result)
            if result == True:
                print(str(text))
                self.teamname.setText((str(text)))
                self.rbat.setEnabled(True)
                self.rbat.setChecked(True)
                self.populatePlayers('BAT')
                self.rbow.setEnabled(True)
                self.rar.setEnabled(True)
                self.rwk.setEnabled(True)
                #self.populatePlayers('BAT')
                self.rbat.toggled.connect(self.radiofunction)
                self.rbow.toggled.connect(self.radiofunction)
                self.rar.toggled.connect(self.radiofunction)
                self.rwk.toggled.connect(self.radiofunction)
        if txt == 'OPEN Team':
            print(' in open team')
            self.testfunction()
        if txt == 'SAVE Team':
            print(' in save team')
        if txt == 'EVALUATE Team':
            print(' in evaluate team')
            dialog = QtWidgets.QDialog()
            dialog.ui = Ui_Dialog()
            dialog.ui.setupUi(dialog)
            dialog.exec_()
            dialog.show()

    # populate the correspondig players on the available list on click of button
    def radiofunction(self):
        category = 'BAT'
        if self.rbat.isChecked() == True:
            print('bat checked')
            category = 'BAT'
            self.populatePlayers(category)
        if self.rbow.isChecked() == True:
            print('bowl checked')
            category = 'BWL'
            self.populatePlayers(category)
            
        if self.rar.isChecked() == True:
            print('ar checked')
            category = 'AR'
            self.populatePlayers(category)
        if self.rwk.isChecked() == True:
            print('wk checked')
            category = 'WK'
            self.populatePlayers(category)
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
