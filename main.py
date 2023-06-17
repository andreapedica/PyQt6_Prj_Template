import sys
from threading import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QGraphicsScene, QGraphicsView, QSizePolicy, QFileDialog, QMessageBox, QSlider
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap, QImage, QPalette, QColor, QCursor, QClipboard
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QMetaObject, pyqtSignal
import pkg_resources
import time
import json
import base64
from io import BytesIO
import unicodedata
import os
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        gui_file = pkg_resources.resource_filename(__name__, "qt/mainpanel.ui")
        loadUi(gui_file, self) # load the ui file from Qt Designer directly
        self.show()

        # set window title name
        self.setWindowTitle("project - v0.0.1")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
