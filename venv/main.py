import sys

import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton ,QLineEdit,QLabel,QMessageBox
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 500))
        self.setWindowTitle("JailbreakUX")

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 32)

        self.button = QPushButton('Directory', self)
        self.button.clicked.connect(self.directorymain)
        self.button.move(20, 80)


        pybutton = QPushButton('Jailbreak Checkm8 X', self)
        pybutton.clicked.connect(self.jailbreakme)
        pybutton.resize(200, 32)
        pybutton.move(50, 100)
        pybutton.setToolTip('Click here to jailbreak')

        # change to the jailbreak main directory to checkm8

    def directorymain(self):
        try:
            pathToDirectory = self.textbox.text()
            os.chdir(pathToDirectory)
            print("Your Chosen Directory is : " ,pathToDirectory)
        except OSError as e:
         print(e.errno)
              ######### completey jailbreak via button click ###########

    def jailbreakme(self):
        directoryres = "/Users/rdunlocked/Desktop/Jailbreak/dfu" #/Users/rdunlocked/Desktop/Jailbreak/dfu
        cmd2 = "./ipwndfu -p"
        maincode = os.system(cmd2)
        QMessageBox.question(self, 'Jailbreak Status !! ', "Jailbreak Timeout\n after 5 seconds : NO DFU Device", QMessageBox.Ok,
                             QMessageBox.Ok)
        print('jailbreak status : ',maincode)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
