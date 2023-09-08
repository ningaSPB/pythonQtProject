from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connets()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Здоровье')
        self.resize(400, 400)
    def initUI(self):
        self
    def connets(self):
        pass


