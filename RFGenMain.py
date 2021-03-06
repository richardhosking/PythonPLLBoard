"""
Main file to start the RF Generator for a Raspberry Pi Touchscreen interface
Using Python PyQt 
Qt Designer to generate UI - output of this is XML
Convert to Python using Riverbank Computing XML => Python tool 

"""

from PyQt5.QtWidgets import QApplication
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# Main RF Generator Form class generated by Qt Designer
from RFGeneratorUIClass import Ui_MainWindow

# Subclass Ui_MainWindow to customise application's main window


def main():
    app = QApplication(sys.argv)
    form = Ui_MainWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

