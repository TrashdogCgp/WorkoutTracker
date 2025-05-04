from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os

class UI(QMainWindow):
        def __init__(self):
            super().__init__()
            # Get the absolute path to the current file's directory
            ui_path = os.path.dirname(os.path.abspath(__file__))
            # Load the UI file, joining the path with the UI file name
            uic.loadUi(os.path.join(ui_path, "MainPage.ui"), self)
            self.show()

if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = UI()
        app.exec_()
