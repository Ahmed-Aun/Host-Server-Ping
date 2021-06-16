from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import os
from window import Ui_MainWindow
#from PyQt5.uic import loadUiType
#uiFile, _ = loadUiType('window.ui')

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('ping a server')
        self.setFixedSize(282, 157)
        self.pushButton.clicked.connect(self.ping)

    def ping(self):
      host = self.lineEdit.text()
      if host == '':
        QMessageBox.warning(self, 'Empty field', 'provid a valid IP address')
      else:
          response = os.system("ping -n, 20 " + host)
          if response == 0:
            QMessageBox.information(self, 'ping results', host+' server is up')
          else:
            QMessageBox.information(self, 'ping results', host+' server is down')



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
